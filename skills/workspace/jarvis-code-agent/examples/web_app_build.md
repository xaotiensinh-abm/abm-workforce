# Example: Full-Stack Web App Build

## Task Contract
**Goal**: Build a responsive landing page with contact form and dark mode
**Complexity**: M (2 domains - frontend + backend)

## Sub-Agent Decision
- Frontend + form handler → Spawn FrontendSubAgent + BackendSubAgent

## Execution

### FrontendSubAgent Output
- `index.html` — semantic HTML5, responsive layout
- `style.css` — dark mode default, glassmorphism, CSS variables
- `script.js` — form validation, theme toggle, smooth animations

### BackendSubAgent Output
- `server.js` — Express, form endpoint with validation
- `.env.example` — environment variables template

## Quality Gate
- Responsive on mobile/tablet/desktop ✅
- Dark mode toggle works ✅
- Form validates before submit ✅
- No XSS vulnerabilities ✅
- Lighthouse score > 90 ✅
