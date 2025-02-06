import { defineStyle, defineStyleConfig } from '@chakra-ui/styled-system';

const baseStyle = defineStyle({
  card: {
    container: {
      bg: 'white',
      _dark: {
        bg: 'gray.800',
      },
      borderRadius: 'lg',
      boxShadow: 'md',
      overflow: 'hidden',
      transition: 'all 0.2s',
    },
    image: {
      height: '200px',
      objectFit: 'cover',
      width: '100%',
    },
    content: {
      p: 6,
    },
    title: {
      fontSize: 'xl',
      fontWeight: 'semibold',
      mb: 2,
    },
    description: {
      color: 'gray.600',
      _dark: {
        color: 'gray.300',
      },
    },
  },
  grid: {
    container: {
      width: '100%',
      gap: { base: 4, md: 6 },
      columns: { base: 1, md: 2, lg: 3 },
    },
  },
  filters: {
    container: {
      p: 4,
      bg: 'gray.50',
      _dark: {
        bg: 'gray.700',
      },
      borderRadius: 'md',
      mb: 6,
    },
  },
});

const variants = {
  featured: defineStyle({
    card: {
      container: {
        boxShadow: 'xl',
      },
      image: {
        height: '300px',
      },
    },
  }),
  compact: defineStyle({
    card: {
      container: {
        boxShadow: 'sm',
      },
      image: {
        height: '150px',
      },
      content: {
        p: 4,
      },
    },
  }),
};

export const recipeTheme = defineStyleConfig({
  baseStyle,
  variants,
  defaultProps: {
    variant: 'default',
  },
});
