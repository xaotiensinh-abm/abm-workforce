# Code Standards & Best Practices

## Coding Rules
- TypeScript strict mode cho mọi project
- ESLint + Prettier enforced
- No `any` type — use proper generics
- Error handling: try-catch cho mọi async operation
- Input validation tại boundary layers

## Architecture Patterns
- **Clean Architecture**: Controllers → Services → Repositories
- **Component Pattern**: Atomic Design (Atoms → Molecules → Organisms)
- **API Design**: RESTful conventions, proper HTTP methods & status codes
- **State Management**: Minimal global state, prefer local/derived

## Security (delegate to W6 for deep review)
- Never hard-code secrets → env variables
- Sanitize all user input
- CORS configuration explicit
- Rate limiting on public endpoints

## Performance
- Lazy loading for routes and heavy components
- Image optimization (WebP, responsive images)
- Bundle splitting (vendor, app, lazy chunks)
- Database: indexes on filtered/sorted columns, avoid N+1
