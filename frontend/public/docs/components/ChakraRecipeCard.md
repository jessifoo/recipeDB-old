# ChakraRecipeCard

A responsive recipe card component built with Chakra UI that displays recipe information in an elegant and accessible way.

## Usage

```tsx
import { ChakraRecipeCard } from '@/components/recipes/ChakraRecipeCard';

function RecipeList() {
  const handleLike = (id: number) => {
    // Handle like action
  };

  return (
    <ChakraRecipeCard
      recipe={{
        id: 1,
        title: "Chocolate Cake",
        description: "Rich and moist chocolate cake",
        prepTime: 20,
        cookTime: 30,
        servings: 8,
        allergens: ["dairy", "eggs", "wheat"],
        isLiked: false
      }}
      onLike={handleLike}
    />
  );
}
```

## Props

| Prop     | Type                    | Required | Description                                     |
|----------|-------------------------|----------|-------------------------------------------------|
| recipe   | Recipe                  | Yes      | Recipe data object                             |
| onLike   | (id: number) => void   | Yes      | Callback function when like button is clicked  |

### Recipe Type

```typescript
interface Recipe {
  id: number;
  title: string;
  description: string;
  prepTime: number;    // in minutes
  cookTime: number;    // in minutes
  servings: number;
  allergens: string[];
  isLiked: boolean;
}
```

## Features

- 🎨 **Responsive Design**: Adapts to different screen sizes using Chakra UI's responsive props
- 🌙 **Dark Mode Support**: Automatically adjusts colors for dark mode
- ♿ **Accessibility**: ARIA labels and semantic HTML
- 📱 **Mobile First**: Optimized for mobile devices with appropriate touch targets
- 🎯 **Type Safe**: Full TypeScript support

## Customization

The component uses Chakra UI's theme tokens and can be customized through:

1. **Theme Customization**:
```typescript
// theme/components/card.ts
export const cardTheme = defineStyleConfig({
  variants: {
    elevated: {
      container: {
        // Your custom styles
      }
    }
  }
});
```

2. **Props Override**:
```tsx
<ChakraRecipeCard
  recipe={recipe}
  onLike={handleLike}
  sx={{
    // Your custom styles
  }}
/>
```

## Implementation Details

### Responsive Behavior

- Mobile (< 480px):
  - Single column layout
  - Smaller text and spacing
  - Stacked recipe details

- Tablet (≥ 480px):
  - Multi-column layout for details
  - Larger text and spacing
  - Horizontal recipe details

- Desktop (≥ 768px):
  - Larger text and spacing
  - Optimal reading width
  - Enhanced hover effects

### Hooks Used

1. **useBreakpointValue**:
   - Manages responsive values
   - Provides fallback values
   ```tsx
   const fontSize = useBreakpointValue({ base: 'sm', md: 'md' });
   ```

2. **useThemeTokens**:
   - Access to theme values
   - Type-safe token access
   ```tsx
   const { getSpace } = useThemeTokens();
   const spacing = getSpace(4);
   ```

3. **useColorModeValue**:
   - Dark mode support
   - Consistent color switching
   ```tsx
   const textColor = useColorModeValue('gray.600', 'gray.300');
   ```

### Styling Patterns

1. **Grid Layout**:
   ```tsx
   <Grid
     templateColumns={{
       base: '1fr',
       sm: 'repeat(3, 1fr)'
     }}
     gap={{ base: 2, sm: 4 }}
   >
     {/* Content */}
   </Grid>
   ```

2. **Responsive Typography**:
   ```tsx
   <Text
     fontSize={responsive('fontSize', { base: 'sm', md: 'md' })}
     color={textColor}
   >
     {content}
   </Text>
   ```

## Best Practices

1. **Accessibility**:
   - Use semantic HTML elements
   - Provide ARIA labels
   - Maintain color contrast
   - Support keyboard navigation

2. **Performance**:
   - Memoize callbacks
   - Use CSS Grid for layout
   - Optimize re-renders
   - Lazy load images (if added)

3. **Maintainability**:
   - Use theme tokens
   - Follow component patterns
   - Document props and usage
   - Keep components focused

## Examples

### Basic Usage
```tsx
<ChakraRecipeCard recipe={recipe} onLike={handleLike} />
```

### With Custom Styles
```tsx
<ChakraRecipeCard
  recipe={recipe}
  onLike={handleLike}
  sx={{
    bg: 'gray.50',
    borderRadius: 'xl',
  }}
/>
```

### In a Grid Layout
```tsx
<RecipeGrid minCardWidth="320px" gap={6}>
  {recipes.map(recipe => (
    <ChakraRecipeCard
      key={recipe.id}
      recipe={recipe}
      onLike={handleLike}
    />
  ))}
</RecipeGrid>
```

## Related Components

- RecipeGrid
- Card
- Tag
- IconButton
