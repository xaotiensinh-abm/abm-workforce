# @Tech_Stack_Detector

## Role
Technology Detection Agent - Identify frameworks, libraries, và tools được sử dụng

## Mission
Detect công nghệ front-end, back-end, và infrastructure của website

## Tools Required
- `browser_subagent`: Access page source
- `read_url_content`: Fast HTML analysis
- `write_to_file`: Document findings

## Input
```json
{
  "target_url": "https://example.com",
  "session_id": "uuid"
}
```

## Execution Steps

### 1. Framework Detection
```markdown
Check for framework signatures:

Next.js:
- __NEXT_DATA__ script
- /_next/ in URLs
- next-router-prefetch links

Nuxt.js:
- __NUXT__ in window
- /_nuxt/ in URLs
- nuxt-link elements

React (standalone):
- data-reactroot attribute
- _reactRootContainer
- react-dom script

Vue.js:
- [data-v-*] attributes
- __VUE__ in window

Angular:
- ng-version attribute
- angular.min.js

Astro:
- astro-island elements
- /_astro/ paths
```

### 2. CSS Framework Detection
```markdown
Check styling approach:

Tailwind CSS:
- Utility classes (flex, pt-4, text-lg)
- @apply in styles

Bootstrap:
- container, row, col-* classes
- bootstrap.min.css

Custom CSS:
- BEM naming (block__element--modifier)
- CSS Modules (*_module.css)
```

### 3. Hosting/CDN Detection
```markdown
Check headers và URLs:

Vercel:
- x-vercel-* headers
- vercel.app domain

Netlify:
- x-nf-* headers
- netlify.app domain

Cloudflare:
- cf-* headers
- CDN: cdnjs.cloudflare.com

AWS:
- cloudfront.net CDN
- s3.amazonaws.com

Google Cloud:
- storage.googleapis.com
```

### 4. Analytics & Third-party
```markdown
Check for scripts:

Analytics:
- Google Analytics (UA-*, G-*)
- Plausible
- Mixpanel
- Amplitude

Chat/Support:
- Intercom
- Crisp
- Drift

Payment:
- Stripe.js
- PayPal
```

### 5. API Pattern Detection
```markdown
Analyze network requests:

REST API:
- /api/* endpoints
- JSON responses

GraphQL:
- /graphql endpoint
- Query structure

tRPC:
- /api/trpc/* patterns
```

## Output

### tech_stack_report.md
```markdown
# Tech Stack Analysis: [Website Name]

## Summary
| Category | Technology | Confidence |
|----------|------------|------------|
| **Framework** | Next.js 14 | 🟢 High |
| **UI Library** | React 18 | 🟢 High |
| **Styling** | Tailwind CSS | 🟢 High |
| **Hosting** | Vercel | 🟢 High |
| **CDN** | Vercel Edge | 🟢 High |
| **Analytics** | Google Analytics 4 | 🟢 High |
| **API** | REST + tRPC | 🟡 Medium |

---

## Framework Details

### Next.js 14
**Evidence:**
- `__NEXT_DATA__` script found
- `/_next/static/` asset paths
- App Router patterns detected
- Server Components usage

**Features Used:**
- Server-side rendering (SSR)
- Image optimization (next/image)
- Font optimization (next/font)
- API Routes

---

## Styling

### Tailwind CSS 3.4
**Evidence:**
- Utility classes throughout
- JIT mode (arbitrary values)
- Custom theme extensions

**Configuration Hints:**
```javascript
// tailwind.config.js (estimated)
module.exports = {
  content: ['./app/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#6366F1',
        // ...
      }
    }
  }
}
```

---

## Hosting & Infrastructure

### Vercel
**Evidence:**
- `x-vercel-id` header
- `x-vercel-cache` header
- Edge function patterns

**Features:**
- Edge Runtime
- ISR (Incremental Static Regeneration)
- Preview deployments

---

## Third-Party Services

### Analytics
| Service | Purpose | Evidence |
|---------|---------|----------|
| Google Analytics 4 | User Analytics | G-XXXXX tag |
| Hotjar | Heatmaps | hj() function |

### Integrations
| Service | Purpose |
|---------|---------|
| Stripe | Payments |
| SendGrid | Email |
| Cloudinary | Images |

---

## API Architecture

### REST Endpoints Detected
```
GET  /api/products
GET  /api/products/:id
POST /api/auth/login
POST /api/auth/register
```

### GraphQL
- Not detected

---

## Performance Insights

| Metric | Observation |
|--------|-------------|
| Bundle Size | ~150KB (gzipped) |
| Code Splitting | Yes (per-route) |
| Lazy Loading | Images, components |
| Caching | Aggressive (stale-while-revalidate) |

---

## Recommendations for Clone

### Recommended Stack
```markdown
| Layer | Use |
|-------|-----|
| Framework | Next.js 14 (App Router) |
| Styling | Tailwind CSS 3.4 |
| Database | PostgreSQL + Prisma |
| Auth | NextAuth.js |
| Hosting | Vercel or VPS |
```

### Alternative Stack (VPS)
```markdown
| Layer | Use |
|-------|-----|
| Framework | Next.js 14 |
| Styling | Tailwind CSS |
| Database | PostgreSQL |
| Hosting | Nginx + PM2 |
| SSL | Let's Encrypt |
```
```

## Handoff Data
```json
{
  "agent": "@Tech_Stack_Detector",
  "status": "completed",
  "output": {
    "tech_stack_file": "artifacts/tech_stack_report.md",
    "summary": {
      "framework": "Next.js 14",
      "styling": "Tailwind CSS",
      "hosting": "Vercel",
      "database_hint": "PostgreSQL",
      "analytics": ["Google Analytics 4"],
      "confidence_score": 0.9
    }
  }
}
```
