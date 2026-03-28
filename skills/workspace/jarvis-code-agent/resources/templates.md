# Code Output Templates

## Project Setup Template
```
project/
├── src/
│   ├── components/     # UI components
│   ├── pages/          # Route pages
│   ├── services/       # API / business logic
│   ├── utils/          # Shared utilities
│   ├── types/          # TypeScript types
│   └── styles/         # CSS / design tokens
├── tests/              # Test files
├── public/             # Static assets
├── package.json
├── tsconfig.json
└── README.md
```

## Component Template
```typescript
interface Props {
  // Define clear props with JSDoc
}

export function ComponentName({ ...props }: Props) {
  // 1. Hooks
  // 2. Derived state
  // 3. Handlers
  // 4. Render
  return (/* JSX */);
}
```

## API Route Template
```typescript
export async function handler(req: Request): Promise<Response> {
  try {
    // 1. Validate input
    // 2. Business logic
    // 3. Return response
    return Response.json({ data }, { status: 200 });
  } catch (error) {
    // 4. Error handling with proper status codes
    return Response.json({ error: message }, { status: 500 });
  }
}
```
