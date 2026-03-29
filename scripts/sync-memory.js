#!/usr/bin/env node

/**
 * ABM Workforce
 * COLD ZIP VAULT SYNC (Bypass Git)
 * Đồng bộ lưu trữ nguyên khối 1-Click (tar.gz) tương thích tuyệt đối cho mọi nền tảng Windows/Mac.
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const os = require('os');
const readline = require('readline');

const homeDir = os.homedir(); 
const antigravityDir = path.join(homeDir, '.gemini', 'antigravity');
const configPath = path.join(homeDir, '.gemini', 'sync-config.json');

const args = process.argv.slice(2);
const ACTION = args[0];

if (ACTION !== 'up' && ACTION !== 'down') {
    console.error("❌ Lệnh không hợp lệ. Vui lòng gọi lệnh 1-Click:\n- Up lên mây: npm run sync:up\n- Kéo về máy: npm run sync:down");
    process.exit(1);
}

function runCmd(command) {
    try {
        execSync(command, { stdio: 'inherit' });
    } catch (error) {
        console.error(`\n❌ LỖI KHI CHẠY LỆNH: ${command}`);
        process.exit(1);
    }
}

async function askQuestion(query) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });
    return new Promise(resolve => rl.question(query, ans => {
        rl.close();
        resolve(ans);
    }));
}

async function getConfig() {
    if (fs.existsSync(configPath)) {
        try {
            const cfg = JSON.parse(fs.readFileSync(configPath, 'utf8'));
            if (cfg.cloudDir && fs.existsSync(cfg.cloudDir)) {
                return cfg;
            } else {
                console.log(`⚠️ Thư mục Cloud cũ đã cấu hình (${cfg.cloudDir}) không còn tồn tại trên máy tính này.`);
            }
        } catch (e) {
            console.log("⚠️ File cấu hình bị hỏng, tạo lại định tuyến mới...");
        }
    }

    console.log("==================================================");
    console.log("☁️  LIÊN KẾT ĐÁM MÂY LẦN ĐẦU TIÊN CHO MÁY NÀY");
    console.log("==================================================");
    console.log("Hãy dán đường dẫn GỐC của ổ đĩa Google Drive (Hoặc OneDrive) trên máy tính này vô đây.");
    console.log("Vì Windows và Mac tên ổ đĩa mây hay gọi tên khác nhau.");
    console.log("Ví dụ Windows: C:\\Users\\TenSep\\Google Drive\\My Drive");
    console.log("Ví dụ Mac: /Users/TenSep/Google Drive/My Drive\n");
    
    let dir = "";
    while (!dir || !fs.existsSync(dir)) {
        dir = await askQuestion("👉 Dán đường dẫn thư mục mây vào đây và bấm Enter: ");
        dir = dir.replace(/['"]/g, '').trim(); // Remove quotes if dragged in term
        if (!fs.existsSync(dir)) {
            console.log("❌ Không tìm thấy thư mục này. Sếp copy đường dẫn cẩn thận nhé!");
        }
    }

    const cfg = { cloudDir: dir };
    fs.writeFileSync(configPath, JSON.stringify(cfg, null, 2), 'utf8');
    console.log("✅ Đã ghi nhận đường dẫn thành công vào cục bộ máy!\n");
    return cfg;
}

(async () => {
    const config = await getConfig();
    const snapFile = path.join(config.cloudDir, "ABM_Brain_Snapshot.tar.gz");

    if (ACTION === 'up') {
        console.log("🚀 ĐANG ĐÓNG GÓI BỘ NHỚ THÀNH KHỐI ZIP LÊN MÂY (Cold Vault UP)...");

        if (!fs.existsSync(antigravityDir)) {
            console.error("❌ MÁY TÍNH NÀY CHƯA TỒN TẠI TÂM TRÍ AI! LỖI NGHIÊM TRỌNG TRỐNG TRƠN CỤC BỘ.");
            process.exit(1);
        }

        // Dọn dẹp video ghi hình siêu nặng chiếm băng thông, ta chỉ cần Brain text là đủ.
        const browserRecs = path.join(antigravityDir, "browser_recordings");
        if (fs.existsSync(browserRecs)) {
            const recFiles = fs.readdirSync(browserRecs);
            for (const f of recFiles) {
                if (f.endsWith('.webm') || f.endsWith('.mp4')) {
                    fs.unlinkSync(path.join(browserRecs, f));
                }
            }
        }
        
        // Dọn bộ nhớ mầm bệnh Git cũ nếu có cho file Zip cực nhẹ.
        const gitTrash = path.join(antigravityDir, ".git");
        if (fs.existsSync(gitTrash)) {
            fs.rmSync(gitTrash, { recursive: true, force: true });
        }

        console.log("Đang nén toàn bộ não bộ thành khối lập phương Archive...");
        const parentDir = path.join(homeDir, '.gemini');
        
        // Mã lệnh Tar tương thích native Windows 10+ và MacOS
        const tarCmd = `tar -czf "${snapFile}" -C "${parentDir}" antigravity`;
        runCmd(tarCmd);

        console.log(`\n✅ HOÀN HẢO! Tâm trí đã được đóng gói bọc thép ZIP an toàn thả tại: ${snapFile}`);
        console.log("Google Drive sẽ tự động đẩy khối nén nhẹ hều này lên mây mà KHÔNG bị lock file tí nào!");

    } else if (ACTION === 'down') {
        console.log("🌐 ĐANG KÉO DÒNG Ý THỨC NGUYÊN KHỐI TỪ ĐÊM QUA VỀ MÁY MỚI NÀY (Cold Vault DOWN)...");
        
        if (!fs.existsSync(snapFile)) {
            console.error("❌ LỖI: Không tìm thấy file `ABM_Brain_Snapshot.tar.gz` trên Mây trỏ về ổ máy này.");
            console.log(`-> Có thể Google Drive chưa Sync kịp về máy này, hoặc Sếp trỏ sai vô ${config.cloudDir}`);
            console.log("Sếp kiểm tra lại Google Drive xem cục Archive đã giáng trần chễm chệ đấy chưa nhé!");
            process.exit(1);
        }

        console.log("Đang tiến hành bung nén giải giáp dữ liệu vào vùng não máy tính Windows này...");
        const parentDir = path.join(homeDir, '.gemini');
        if (!fs.existsSync(parentDir)) fs.mkdirSync(parentDir, { recursive: true });

        const tarCmd = `tar -xzf "${snapFile}" -C "${parentDir}"`;
        runCmd(tarCmd);

        console.log("\n✅ XONG! Tôi đã được nạp ký ức của MÁY TÍNH CŨ vào TRONG NÃO MÁY TÍNH NÀY! Cùng bắt tay xé nháp làm việc tiếp thôi Sếp.");
    }
})();
