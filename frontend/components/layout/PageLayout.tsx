import type { ReactNode } from 'react';

import { Container } from '@chakra-ui/react';

interface PageLayoutProps {
  children: ReactNode;
}

export function PageLayout({ children }: PageLayoutProps) {
  return <Container maxW="container.xl">{children}</Container>;
}
