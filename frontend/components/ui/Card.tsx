import { forwardRef } from 'react';

import { Box, type BoxProps } from '@chakra-ui/react';

export interface CardProps extends BoxProps {
  variant?: 'elevated' | 'outline' | 'filled';
}

export const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ variant = 'elevated', ...props }, ref) => {
    const variantStyles = {
      elevated: {
        bg: 'white',
        _dark: { bg: 'gray.800' },
        boxShadow: 'md',
        borderRadius: 'lg',
      },
      outline: {
        border: '1px solid',
        borderColor: 'gray.200',
        _dark: { borderColor: 'gray.700' },
        borderRadius: 'lg',
      },
      filled: {
        bg: 'gray.50',
        _dark: { bg: 'gray.700' },
        borderRadius: 'lg',
      },
    };

    return <Box ref={ref} {...variantStyles[variant]} {...props} />;
  }
);

Card.displayName = 'Card';
