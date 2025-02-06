import type { ComponentStyleConfig } from '@chakra-ui/react';

export const Card: ComponentStyleConfig = {
  variants: {
    elevated: {
      backgroundColor: 'white',
      boxShadow: 'base',
      borderRadius: 'md',
      cursor: 'pointer',
      transition: 'all 0.2s',
      _hover: {
        transform: 'translateY(-2px)',
        boxShadow: 'md',
      },
    },
  },
  defaultProps: {
    variant: 'elevated',
  },
};
