# Design System Documentation

## Overview
This design system is built on top of Chakra UI to provide a consistent, accessible, and maintainable component library for our application.

## Core Principles
1. **Consistency**: Use predefined tokens for colors, spacing, typography, and other design elements
2. **Accessibility**: Follow WCAG 2.1 guidelines for all components
3. **Flexibility**: Components should be composable and customizable
4. **Performance**: Optimize for bundle size and runtime performance

## Directory Structure
```
frontend/
├── components/
│   ├── ui/            # Base UI components
│   └── features/      # Feature-specific components
├── theme/
│   ├── foundations/   # Design tokens
│   ├── components/    # Component-specific theme
│   └── styles/        # Global styles
└── docs/             # Documentation
```

## Design Tokens

### Colors
- Brand Colors: Primary colors that represent our brand
- Accent Colors: Secondary colors for highlighting and emphasis
- Semantic Colors: Colors that convey meaning (success, error, warning, info)
- Neutral Colors: Grays and whites for backgrounds and text

### Typography
- Font Family: Inter for headings and body text
- Font Sizes: From xs (0.75rem) to 9xl (8rem)
- Font Weights: From hairline (100) to black (900)
- Line Heights: Predefined scales for different contexts

### Spacing
We use an 8-point grid system:
- 0: 0
- 1: 0.25rem (4px)
- 2: 0.5rem (8px)
- 3: 0.75rem (12px)
- 4: 1rem (16px)
...etc.

### Components

#### Base Components
1. **Card**
   - Variants: elevated, outline, filled
   - Props: variant, ...BoxProps
   - Usage: Container for related content

2. **Button**
   - Variants: solid, outline, ghost, link
   - Sizes: xs, sm, md, lg
   - States: hover, active, disabled, loading

3. **Input**
   - Variants: outline, filled, flushed
   - States: focus, error, disabled
   - Validation support

## Best Practices

### Component Development
1. **Composition Over Inheritance**
   ```tsx
   // Good
   <Card>
     <CardHeader />
     <CardBody />
   </Card>

   // Avoid
   <Card header={...} body={...} />
   ```

2. **Props API**
   - Use consistent prop names across components
   - Provide sensible defaults
   - Use TypeScript for type safety

3. **Accessibility**
   - Include ARIA attributes
   - Support keyboard navigation
   - Maintain proper contrast ratios

### State Management
1. Use local state for UI-specific state
2. Use global state (React Context, Redux, etc.) for shared state
3. Keep components pure when possible

### Performance
1. Use React.memo() for expensive components
2. Lazy load components when appropriate
3. Optimize re-renders by proper prop management

## Usage Examples

### Basic Card
```tsx
import { Card } from '@/components/ui';

function Example() {
  return (
    <Card variant="elevated">
      <h2>Card Title</h2>
      <p>Card content goes here</p>
    </Card>
  );
}
```

### Responsive Design
```tsx
<Box
  padding={{ base: 4, md: 6, lg: 8 }}
  width={{ base: "100%", md: "50%" }}
>
  Content
</Box>
```

## Contributing
1. Follow the component structure in `/components/ui`
2. Add tests for new components
3. Update documentation
4. Follow TypeScript best practices
5. Ensure accessibility compliance
