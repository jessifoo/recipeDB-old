# RecipeGrid

A responsive grid layout component optimized for displaying recipe cards. Uses CSS Grid with auto-fit and minmax for optimal responsive behavior.

## Usage

```tsx
import { RecipeGrid } from '@/components/recipes/RecipeGrid';
import { ChakraRecipeCard } from '@/components/recipes/ChakraRecipeCard';

function RecipeList() {
  return (
    <RecipeGrid
      minCardWidth={{ base: '280px', md: '320px' }}
      gap={{ base: 4, md: 6 }}
    >
      {recipes.map(recipe => (
        <ChakraRecipeCard
          key={recipe.id}
          recipe={recipe}
          onLike={handleLike}
        />
      ))}
    </RecipeGrid>
  );
}
```

## Props

| Prop         | Type                              | Required | Default                                | Description                          |
|--------------|-----------------------------------|----------|----------------------------------------|--------------------------------------|
| minCardWidth | string \| Record<string, string>  | No       | { base: '280px', md: '320px' }        | Minimum width for grid items         |
| children     | ReactNode                         | Yes      | -                                      | Grid items to display                |
| ...rest      | GridProps                        | No       | -                                      | Additional Chakra UI Grid props      |

## Features

- 📱 **Responsive Layout**: Automatically adjusts columns based on container width
- 🎯 **Dense Packing**: Efficiently uses available space
- 🔄 **Fluid Grid**: Adapts to different screen sizes
- 🎨 **Customizable**: Extends Chakra UI's Grid component

## Implementation Details

### Grid Layout

Uses CSS Grid's `auto-fit` and `minmax` for responsive behavior:

```tsx
<Grid
  templateColumns={{
    base: '1fr',
    sm: `repeat(auto-fit, minmax(${minCardWidth}, 1fr))`
  }}
  gap={gap}
  autoFlow="row dense"
>
  {children}
</Grid>
```

### Responsive Behavior

- Mobile:
  - Single column layout
  - Smaller gaps
  - Full width cards

- Tablet/Desktop:
  - Multi-column layout
  - Larger gaps
  - Optimal card width

## Examples

### Basic Usage
```tsx
<RecipeGrid>
  {recipes.map(recipe => (
    <ChakraRecipeCard key={recipe.id} recipe={recipe} />
  ))}
</RecipeGrid>
```

### Custom Card Width
```tsx
<RecipeGrid
  minCardWidth={{
    base: '250px',
    sm: '300px',
    md: '350px'
  }}
>
  {children}
</RecipeGrid>
```

### Custom Gap
```tsx
<RecipeGrid gap={{ base: 4, md: 6, lg: 8 }}>
  {children}
</RecipeGrid>
```

## Best Practices

1. **Responsive Design**:
   - Use relative units for minCardWidth
   - Consider different screen sizes
   - Test with various content amounts

2. **Performance**:
   - Virtualize large lists
   - Optimize child components
   - Use appropriate key props

3. **Accessibility**:
   - Maintain logical tab order
   - Consider grid navigation
   - Test with screen readers

## Related Components

- ChakraRecipeCard
- Grid
- Container
