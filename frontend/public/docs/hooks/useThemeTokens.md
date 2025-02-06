# useThemeTokens

A custom hook that provides type-safe access to Chakra UI theme tokens.

## Usage

```tsx
import { useThemeTokens } from '@/hooks/useThemeTokens';

function MyComponent() {
  const { getColor, getSpace, getFontSize, getRadius } = useThemeTokens();

  return (
    <Box
      bg={getColor('accent.500')}
      p={getSpace(4)}
      fontSize={getFontSize('lg')}
      borderRadius={getRadius('md')}
    >
      Content
    </Box>
  );
}
```

## API

### getColor
Get a color token from the theme
```tsx
const accentColor = getColor('accent.500');
const primaryColor = getColor('brand.500');
```

### getSpace
Get a spacing token from the theme
```tsx
const spacing = getSpace(4); // returns '1rem'
const largeSpace = getSpace(8); // returns '2rem'
```

### getFontSize
Get a font size token from the theme
```tsx
const size = getFontSize('lg');
const smallSize = getFontSize('sm');
```

### getRadius
Get a border radius token from the theme
```tsx
const radius = getRadius('md');
const largeRadius = getRadius('lg');
```

## Benefits

1. **Type Safety**:
   - TypeScript support
   - Autocomplete for token names
   - Prevents typos and errors

2. **Theme Consistency**:
   - Access to theme values
   - Maintains design system
   - Single source of truth

3. **Developer Experience**:
   - Simple API
   - Intuitive naming
   - Reusable across components

## Examples

### Responsive Styles
```tsx
function ResponsiveComponent() {
  const { getSpace, getFontSize } = useThemeTokens();

  return (
    <Box
      p={{ base: getSpace(2), md: getSpace(4) }}
      fontSize={{ base: getFontSize('sm'), md: getFontSize('md') }}
    >
      Content
    </Box>
  );
}
```

### Custom Style Creation
```tsx
function StyledComponent() {
  const { getColor, getRadius } = useThemeTokens();

  const customStyle = {
    background: getColor('accent.50'),
    border: `1px solid ${getColor('accent.200')}`,
    borderRadius: getRadius('md'),
  };

  return <Box sx={customStyle}>Content</Box>;
}
```

## Best Practices

1. **Performance**:
   - Hook is memoized
   - Use within components
   - Avoid excessive calls

2. **Theme Consistency**:
   - Use tokens over raw values
   - Follow design system
   - Maintain scale

3. **Type Safety**:
   - Leverage TypeScript
   - Use autocomplete
   - Check token existence

## Related

- useBreakpointValue
- useTheme
- responsive utility
