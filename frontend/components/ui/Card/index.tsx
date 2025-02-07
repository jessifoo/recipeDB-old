import { forwardRef } from 'react';

import { Box, type BoxProps } from '@chakra-ui/react';

export interface CardProps extends BoxProps {
  variant?: 'elevated' | 'outline' | 'filled';
}

export const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ variant = 'elevated', children, ...props }, ref) => {
    const variantStyles = {
      elevated: {
        bg: 'white',
        shadow: 'sm',
        _hover: { shadow: 'md' },
      },
      outline: {
        borderWidth: '1px',
      },
      filled: {
        bg: 'gray.50',
      },
    };

    return (
      <Box
        ref={ref}
        p={4}
        borderRadius="lg"
        transition="all 0.2s"
        {...variantStyles[variant]}
        {...props}
      >
        {children}
      </Box>
    );
  }
);

Card.displayName = 'Card';
