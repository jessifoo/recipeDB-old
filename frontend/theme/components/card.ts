import { defineStyle, defineStyleConfig } from '@chakra-ui/styled-system';

const baseStyle = defineStyle({
  container: {
    bg: 'white',
    _dark: {
      bg: 'gray.800',
    },
    borderRadius: 'lg',
    boxShadow: 'sm',
    transition: 'all 0.2s',
  },
});

const variants = {
  elevated: defineStyle({
    container: {
      boxShadow: 'md',
      _hover: {
        boxShadow: 'lg',
      },
    },
  }),
  outline: defineStyle({
    container: {
      border: '1px solid',
      borderColor: 'gray.200',
      _dark: {
        borderColor: 'gray.700',
      },
    },
  }),
};

export const cardTheme = defineStyleConfig({
  baseStyle,
  variants,
  defaultProps: {
    variant: 'elevated',
  },
});
