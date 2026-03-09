---
name: "vercel-composition-patterns"
description: "React composition patterns từ Vercel — compound components, state lifting, composition internals, React 19 APIs. Tránh boolean prop proliferation."
---

# 🧩 Vercel Composition Patterns — React Kiến Trúc

Skill chính thức từ **Vercel** — composition patterns cho React components scalable. Tránh boolean prop proliferation qua **compound components, state lifting, composition internals**.

## Sử dụng khi

- Refactoring components có nhiều boolean props
- Xây dựng reusable component libraries
- Thiết kế flexible component APIs
- Review component architecture

## KHÔNG sử dụng khi

- Cần tối ưu performance React → dùng `vercel-react-best-practices`
- Cần audit UI design/accessibility → dùng `web-design-guidelines`
- Cần code frontend từ đầu → dùng `frontend-developer`
- Cần chọn style/palette → dùng `ui-ux-pro-max`

## VÍ DỤ NHANH

```
Input:  "Dialog component có 8 boolean props: isLarge, isFullscreen, hasFooter..."
Output:
  [architecture-compound-components] → Refactor thành:
  <Dialog>
    <Dialog.Header><Dialog.Close /></Dialog.Header>
    <Dialog.Body>Content</Dialog.Body>
    <Dialog.Footer>Actions</Dialog.Footer>
  </Dialog>
```

---

## QUY TẮC THEO PRIORITY

### 1. 🟡 Component Architecture (HIGH)

#### `architecture-avoid-boolean-props`
❌ KHÔNG thêm boolean props để customize behavior:
```tsx
// ❌ Bad — boolean props proliferation
<Dialog isLarge isFullscreen hasFooter showClose />
```
✅ Dùng composition:
```tsx
// ✅ Good — compound components
<Dialog>
  <Dialog.Header>
    <Dialog.Close />
  </Dialog.Header>
  <Dialog.Body>Content</Dialog.Body>
  <Dialog.Footer>Actions</Dialog.Footer>
</Dialog>
```

#### `architecture-compound-components`
Structure complex components với shared context:
```tsx
const DialogContext = createContext()

function Dialog({ children }) {
  const [open, setOpen] = useState(false)
  return (
    <DialogContext.Provider value={{ open, setOpen }}>
      {children}
    </DialogContext.Provider>
  )
}

Dialog.Trigger = function Trigger({ children }) {
  const { setOpen } = useContext(DialogContext)
  return <button onClick={() => setOpen(true)}>{children}</button>
}
```

### 2. 🟢 State Management (MEDIUM)

#### `state-decouple-implementation`
Provider là nơi DUY NHẤT biết cách state được quản lý:
```tsx
// Consumer không cần biết dùng useState, Zustand, hay Redux
const { items, addItem } = useCart()
```

#### `state-context-interface`
Define generic interface: state + actions + meta:
```tsx
interface CartContext {
  state: { items: Item[]; total: number }
  actions: { add: (item: Item) => void; remove: (id: string) => void }
  meta: { isLoading: boolean; error: Error | null }
}
```

#### `state-lift-state`
Move state vào provider components cho sibling access:
```tsx
// ✅ State ở provider level — cả Header và Sidebar đều access được
<CartProvider>
  <Header />  {/* hiện cart count */}
  <Sidebar /> {/* hiện cart items */}
</CartProvider>
```

### 3. 🟢 Implementation Patterns (MEDIUM)

#### `patterns-explicit-variants`
Tạo explicit variant components thay vì boolean modes:
```tsx
// ❌ Bad
<Button primary large outline />

// ✅ Good
<Button variant="primary" size="lg" />
// hoặc
<PrimaryButton size="lg" />
```

#### `patterns-children-over-render-props`
Dùng `children` cho composition thay vì `renderX` props:
```tsx
// ❌ Bad
<Card renderHeader={() => <h2>Title</h2>} renderFooter={() => <Button />} />

// ✅ Good
<Card>
  <Card.Header><h2>Title</h2></Card.Header>
  <Card.Footer><Button /></Card.Footer>
</Card>
```

### 4. 🟢 React 19 APIs (MEDIUM)

> ⚠️ **React 19+ only** — Bỏ qua nếu dùng React 18

#### `react19-no-forwardref`
```tsx
// ❌ React 18
const Input = forwardRef((props, ref) => <input ref={ref} {...props} />)

// ✅ React 19 — ref là prop thường
function Input({ ref, ...props }) {
  return <input ref={ref} {...props} />
}
```

#### `react19-use-hook`
```tsx
// ❌ React 18
const value = useContext(MyContext)

// ✅ React 19
const value = use(MyContext)
```

---

## KHI NÀO ÁP DỤNG

| Dấu hiệu | Pattern cần dùng |
|-----------|-----------------|
| Component có 5+ boolean props | Compound Components |
| Siblings cần share state | Lift State to Provider |
| Render props callbacks nhiều | Children Composition |
| `isX`, `hasY`, `showZ` props | Explicit Variants |
| `forwardRef` (React 19) | Direct ref prop |

---

## Nguồn gốc
- **Chính thức**: [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) — Vercel
- Adapt bởi: ABM Workforce v2.2 — Jarvis Orchestrator
