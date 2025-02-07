import { forwardRef } from 'react';

import {
  Container as ChakraContainer,
  type ContainerProps,
} from '@chakra-ui/react';

export const Container = forwardRef<HTMLDivElement, ContainerProps>(
  ({ children, ...props }, ref) => {
    return (
      <ChakraContainer
        ref={ref}
        px={{ base: 4, md: 6, lg: 8 }}
        maxW={{
          base: '100%',
          sm: '540px',
          md: '720px',
          lg: '960px',
          xl: '1140px',
          '2xl': '1320px',
        }}
        {...props}
      >
        {children}
      </ChakraContainer>
    );
  }
);

Container.displayName = 'Container';
