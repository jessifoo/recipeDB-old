import type { Metadata } from 'next';

import type React from 'react';

import { Inter } from 'next/font/google';

import { theme } from '@/theme';
import { ChakraProvider } from '@chakra-ui/react';
import './globals.css';
import { Providers } from './providers';

const inter = Inter({ subsets: ['latin'] });

if (process.env.NODE_ENV === 'development') {
  require('@/mocks').initMocks();
}

export const metadata: Metadata = {
  title: 'FPIES-Friendly Recipes',
  description:
    'A recipe platform for families managing FPIES and food allergies',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <ChakraProvider theme={theme}>
          <Providers>{children}</Providers>
        </ChakraProvider>
      </body>
    </html>
  );
}
