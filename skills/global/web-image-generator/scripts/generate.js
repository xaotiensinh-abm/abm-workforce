#!/usr/bin/env node
/**
 * Web Image Generator v2.0 — Gemini Image API
 * 
 * Tạo ảnh nhẹ, tối ưu cho website. Xuất WebP mặc định.
 * Zero dependencies — chỉ cần Node.js.
 * 
 * Usage:
 *   node generate.js <preset> "<prompt>" [output_path]
 *   node generate.js <preset> --ref <image> "<prompt>" [output]
 *   node generate.js <preset> --hq "<prompt>" [output]
 *   node generate.js <preset> --pro "<prompt>" [output]
 *   node generate.js --custom --ratio 4:5 --size 1K "<prompt>" [output]
 * 
 * Flags:
 *   --hq          High quality (2K resolution)
 *   --pro         Use Gemini 3 Pro model (professional assets)
 *   --ref <path>  Reference image for editing
 *   --format <f>  Output format: webp (default), png, jpeg
 *   --quality <n> WebP/JPEG quality 1-100 (default: 80)
 * 
 * Environment:
 *   GEMINI_API_KEY — Required
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

// ─── Web-Optimized Presets (512 default, lightweight) ───
const PRESETS = {
  'hero':     { aspectRatio: '16:9',  imageSize: '1K',  hqSize: '2K',  desc: 'Hero banner (target <200KB)' },
  'cover':    { aspectRatio: '3:4',   imageSize: '512', hqSize: '1K',  desc: 'Book/novel cover (target <80KB)' },
  'card':     { aspectRatio: '4:3',   imageSize: '512', hqSize: '1K',  desc: 'Horizontal card (target <60KB)' },
  'square':   { aspectRatio: '1:1',   imageSize: '512', hqSize: '1K',  desc: 'Avatar/icon (target <50KB)' },
  'thumb':    { aspectRatio: '3:4',   imageSize: '512', hqSize: '1K',  desc: 'Thumbnail (target <40KB)' },
  'og':       { aspectRatio: '16:9',  imageSize: '1K',  hqSize: '2K',  desc: 'OpenGraph social (target <150KB)' },
  'story':    { aspectRatio: '9:16',  imageSize: '512', hqSize: '1K',  desc: 'Mobile story (target <60KB)' },
  'banner':   { aspectRatio: '21:9',  imageSize: '1K',  hqSize: '2K',  desc: 'Ultra-wide header (target <150KB)' },
  'portrait': { aspectRatio: '2:3',   imageSize: '1K',  hqSize: '2K',  desc: 'Tall poster (target <120KB)' },
  'wide':     { aspectRatio: '3:2',   imageSize: '1K',  hqSize: '2K',  desc: 'Detail header (target <130KB)' },
};

const MODELS = {
  flash: 'gemini-3.1-flash-image-preview',
  pro:   'gemini-3-pro-image-preview',
};

// Valid aspect ratios from Gemini 3.1 Flash docs
const VALID_RATIOS = ['1:1','1:4','1:8','2:3','3:2','3:4','4:1','4:3','4:5','5:4','8:1','9:16','16:9','21:9'];
const VALID_SIZES = ['512','1K','2K','4K'];

// ─── CLI Parsing ───
const args = process.argv.slice(2);

if (args.length < 2 || args[0] === '--help' || args[0] === '-h') {
  console.log(`
╔═══════════════════════════════════════════════════╗
║  🖼️  Web Image Generator v2.0                     ║
║  Optimized for web performance · WebP default     ║
║  Powered by Gemini 3.1 Flash Image Preview        ║
╚═══════════════════════════════════════════════════╝

Usage: node generate.js <preset> "<prompt>" [output_path]

Web-Optimized Presets:
${Object.entries(PRESETS).map(([k, v]) => 
  `  ${k.padEnd(12)} ${v.aspectRatio.padEnd(6)} ${v.imageSize.padEnd(4)} ${v.desc}`
).join('\n')}

Flags:
  --hq             2K resolution (for print/marketing)
  --pro            Gemini 3 Pro model (professional, 4K capable)
  --ref <path>     Reference image for editing
  --search         Google Search grounding (novel info, real data)
  --text           Enable Vietnamese text rendering on image
  --format <fmt>   Output: webp (default), png, jpeg
  --quality <1-100> Compression quality (default: 80)

Custom:
  node generate.js --custom --ratio 4:5 --size 1K "<prompt>" [output]

Valid Aspect Ratios:
  ${VALID_RATIOS.join(' · ')}

Valid Sizes: ${VALID_SIZES.join(' · ')}

Environment:
  GEMINI_API_KEY    Your Google AI API key (required)
  `);
  process.exit(0);
}

// ─── Parse Flags ───
function getFlag(name) {
  const idx = args.indexOf(name);
  return idx !== -1 ? idx : -1;
}

function getFlagValue(name) {
  const idx = getFlag(name);
  if (idx === -1 || idx + 1 >= args.length) return null;
  return args[idx + 1];
}

function hasFlag(name) {
  return args.includes(name);
}

// Parse options
const useHQ = hasFlag('--hq');
const usePro = hasFlag('--pro');
const useSearch = hasFlag('--search');
const useText = hasFlag('--text');
const refPath = getFlagValue('--ref');
const outputFormat = getFlagValue('--format') || 'webp';
const quality = parseInt(getFlagValue('--quality') || '80', 10);

// Collect all flag positions to exclude from positional args
const flagPositions = new Set();
['--hq', '--pro', '--search', '--text'].forEach(f => {
  const i = getFlag(f);
  if (i !== -1) flagPositions.add(i);
});
['--ref', '--format', '--quality', '--ratio', '--size'].forEach(f => {
  const i = getFlag(f);
  if (i !== -1) { flagPositions.add(i); flagPositions.add(i + 1); }
});

let preset, prompt, outputPath, aspectRatio, imageSize;

if (args[0] === '--custom') {
  flagPositions.add(0);
  const customRatio = getFlagValue('--ratio');
  const customSize = getFlagValue('--size');
  
  if (!customRatio || !customSize) {
    console.error('❌ Custom mode requires --ratio and --size');
    process.exit(1);
  }
  if (!VALID_RATIOS.includes(customRatio)) {
    console.error(`❌ Invalid ratio: "${customRatio}". Valid: ${VALID_RATIOS.join(', ')}`);
    process.exit(1);
  }
  if (!VALID_SIZES.includes(customSize)) {
    console.error(`❌ Invalid size: "${customSize}". Valid: ${VALID_SIZES.join(', ')}`);
    process.exit(1);
  }
  
  aspectRatio = customRatio;
  imageSize = customSize;
  preset = `custom-${customRatio.replace(':', 'x')}`;
  
  const remaining = args.filter((_, i) => !flagPositions.has(i));
  prompt = remaining[0];
  outputPath = remaining[1];
} else {
  preset = args[0];
  flagPositions.add(0);
  
  if (!PRESETS[preset]) {
    console.error(`❌ Unknown preset: "${preset}"`);
    console.error(`Available: ${Object.keys(PRESETS).join(', ')}`);
    process.exit(1);
  }
  
  aspectRatio = PRESETS[preset].aspectRatio;
  imageSize = useHQ ? PRESETS[preset].hqSize : PRESETS[preset].imageSize;
  
  const remaining = args.filter((_, i) => !flagPositions.has(i));
  prompt = remaining[0];
  outputPath = remaining[1];
}

if (!prompt) {
  console.error('❌ Missing prompt. Usage: node generate.js <preset> "<prompt>" [output]');
  process.exit(1);
}

// ─── Validate API Key ───
const API_KEY = process.env.GEMINI_API_KEY;
if (!API_KEY) {
  console.error('❌ Missing GEMINI_API_KEY environment variable');
  console.error('Set: $env:GEMINI_API_KEY = "your-key"');
  process.exit(1);
}

// ─── Output Path ───
const ext = outputFormat === 'jpeg' ? 'jpg' : outputFormat;
if (!outputPath) {
  const ts = Date.now();
  const safeName = preset.replace(/[^a-z0-9-]/gi, '_');
  outputPath = `./generated_${safeName}_${ts}.${ext}`;
}

// Ensure correct extension
if (!path.extname(outputPath)) {
  outputPath += `.${ext}`;
}

const outputDir = path.dirname(path.resolve(outputPath));
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

// ─── Model Selection ───
const MODEL = usePro ? MODELS.pro : MODELS.flash;

// ─── Build Request Body ───
function buildRequest() {
  const parts = [];
  
  // Add reference image if provided
  if (refPath) {
    if (!fs.existsSync(refPath)) {
      console.error(`❌ Reference image not found: ${refPath}`);
      process.exit(1);
    }
    const imgBuffer = fs.readFileSync(refPath);
    const imgBase64 = imgBuffer.toString('base64');
    const mimeType = refPath.endsWith('.png') ? 'image/png' 
                   : refPath.endsWith('.webp') ? 'image/webp'
                   : 'image/jpeg';
    
    parts.push({
      inlineData: { mimeType, data: imgBase64 }
    });
  }
  
  // Add text prompt
  parts.push({ text: prompt });
  
  // Use TEXT+IMAGE when search grounding or text rendering enabled
  const modalities = (useSearch || useText) ? ['TEXT', 'IMAGE'] : ['IMAGE'];
  
  const body = {
    contents: [{ parts }],
    generationConfig: {
      responseModalities: modalities,
      imageConfig: {
        aspectRatio: aspectRatio,
        imageSize: imageSize,
      }
    }
  };
  
  // Add Google Search grounding tool
  if (useSearch) {
    body.tools = [{ google_search: {} }];
  }
  
  return JSON.stringify(body);
}

const requestBody = buildRequest();

// ─── Display Info ───
console.log(`\n🖼️  Web Image Generator v2.0`);
console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`);
console.log(`📐 Preset:  ${preset}${useHQ ? ' (HQ)' : ''}`);
console.log(`📏 Ratio:   ${aspectRatio}`);
console.log(`🔍 Size:    ${imageSize}`);
console.log(`🤖 Model:   ${MODEL.split('-').slice(0,3).join('-')}`);
console.log(`📁 Format:  ${outputFormat.toUpperCase()}`);
if (useSearch) console.log(`🔍 Search:  Google Search grounding ON`);
if (useText) console.log(`🔤 Text:    Vietnamese text rendering ON`);
if (refPath) console.log(`🖼️ Ref:     ${path.basename(refPath)}`);
console.log(`📝 Prompt:  ${prompt.substring(0, 80)}${prompt.length > 80 ? '...' : ''}`);
console.log(`📂 Output:  ${path.resolve(outputPath)}`);
console.log(`━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━`);
console.log(`⏳ Generating...`);

const startTime = Date.now();

// ─── Make Request ───
const bodyBytes = Buffer.byteLength(requestBody, 'utf8');
const options = {
  hostname: 'generativelanguage.googleapis.com',
  path: `/v1beta/models/${MODEL}:generateContent`,
  method: 'POST',
  headers: {
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': bodyBytes,
    'x-goog-api-key': API_KEY,
  },
};

const req = https.request(options, (res) => {
  const chunks = [];
  let receivedBytes = 0;
  
  // Response-level timeout (separate from socket timeout)
  const responseTimeout = setTimeout(() => {
    console.error('\n❌ Response download timeout (180s)');
    res.destroy();
    process.exit(1);
  }, 180000);
  
  res.on('data', (chunk) => {
    chunks.push(chunk);
    receivedBytes += chunk.length;
    const kb = Math.round(receivedBytes / 1024);
    process.stdout.write(`\r⏳ Downloading... ${kb} KB`);
  });
  
  res.on('end', () => {
    clearTimeout(responseTimeout);
    process.stdout.write('\r');
    const data = Buffer.concat(chunks).toString();
    const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
    
    try {
      const response = JSON.parse(data);
      
      if (response.error) {
        console.error(`\n❌ API Error [${response.error.code}]: ${response.error.message}`);
        process.exit(1);
      }
      
      const candidates = response.candidates;
      if (!candidates || candidates.length === 0) {
        console.error('\n❌ No candidates in response');
        if (response.promptFeedback) {
          console.error('Feedback:', JSON.stringify(response.promptFeedback, null, 2));
        }
        process.exit(1);
      }
      
      const parts = candidates[0].content?.parts || [];
      let imageFound = false;
      
      for (const part of parts) {
        if (part.inlineData) {
          const { mimeType, data: base64Data } = part.inlineData;
          const rawBuffer = Buffer.from(base64Data, 'base64');
          const rawSizeKB = Math.round(rawBuffer.length / 1024);
          
          // Save based on output format
          let finalBuffer = rawBuffer;
          let finalPath = outputPath;
          let savedFormat = mimeType;
          
          // Gemini returns PNG. For web perf, convert if possible.
          // Zero-dependency approach: try sharp, fallback to PNG + hint
          if (outputFormat === 'webp' || outputFormat === 'jpeg') {
            let converted = false;
            try {
              const sharp = require('sharp');
              const pipeline = outputFormat === 'webp'
                ? sharp(rawBuffer).webp({ quality })
                : sharp(rawBuffer).jpeg({ quality });
              finalBuffer = pipeline.toBuffer({ resolveWithObject: false });
              // sharp .toBuffer() is sync-like when called this way in older versions
              // For safety, handle both Promise and Buffer returns
              if (finalBuffer && typeof finalBuffer.then === 'function') {
                // async path — can't await in sync cb, save PNG
                throw new Error('async sharp');
              }
              savedFormat = outputFormat === 'webp' ? 'image/webp' : 'image/jpeg';
              converted = true;
            } catch (e) {
              // sharp not available or async — save as PNG with conversion hint
              const targetPath = finalPath;
              finalPath = finalPath.replace(/\.(webp|jpg|jpeg)$/i, '.png');
              savedFormat = 'image/png';
              console.log(`\n💡 Saved as PNG (sharp not available for auto-conversion)`);
              console.log(`   Convert manually: npx -y sharp-cli -i "${path.resolve(finalPath)}" -o "${path.resolve(targetPath)}" --format ${outputFormat}`);
            }
          }
          
          fs.writeFileSync(finalPath, finalBuffer);
          
          const finalSizeKB = Math.round(finalBuffer.length / 1024);
          const target = PRESETS[preset]?.desc?.match(/target <(\d+)KB/)?.[1];
          
          console.log(`\n✅ Image saved: ${path.resolve(finalPath)}`);
          console.log(`📊 Size: ${finalSizeKB} KB (${savedFormat})`);
          if (rawSizeKB !== finalSizeKB) {
            console.log(`📉 Compressed: ${rawSizeKB} KB → ${finalSizeKB} KB (-${Math.round((1 - finalSizeKB/rawSizeKB) * 100)}%)`);
          }
          if (target) {
            const status = finalSizeKB <= parseInt(target) ? '✅ PASS' : '⚠️ OVER';
            console.log(`🎯 Budget: ${status} (target <${target}KB)`);
          }
          console.log(`⏱️ Time: ${elapsed}s`);
          imageFound = true;
        } else if (part.text) {
          console.log(`\n💬 Model: ${part.text}`);
        }
      }
      
      // Display grounding metadata if Google Search was used
      if (useSearch && candidates[0].groundingMetadata) {
        const gm = candidates[0].groundingMetadata;
        if (gm.groundingChunks && gm.groundingChunks.length > 0) {
          console.log(`\n📚 Sources (Google Search):`);
          gm.groundingChunks.forEach((chunk, i) => {
            if (chunk.web) {
              console.log(`   ${i+1}. ${chunk.web.title || chunk.web.uri}`);
              console.log(`      ${chunk.web.uri}`);
            }
          });
        }
      }
      
      if (!imageFound) {
        console.error('\n❌ No image data in response');
        process.exit(1);
      }
      
      console.log(`\n🎉 Done!`);
      
    } catch (e) {
      console.error(`\n❌ Parse error: ${e.message}`);
      console.error('Response (first 500 chars):', data.substring(0, 500));
      process.exit(1);
    }
  });
});

req.on('error', (e) => {
  console.error(`\n❌ Request failed: ${e.message}`);
  process.exit(1);
});

// Socket-level timeout (connection + initial response)
req.setTimeout(60000, () => {
  console.error('\n❌ Connection timeout (60s) — API not responding');
  req.destroy();
  process.exit(1);
});

req.write(requestBody);
req.end();
