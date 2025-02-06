import { CSSReset, ChakraProvider } from '@chakra-ui/react';
import type { Preview } from '@storybook/react';
import { theme } from '../theme';

const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: '^on[A-Z].*' },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/i,
      },
    },
  },
  decorators: [
    (Story) => (
      <ChakraProvider theme={theme}>
        <CSSReset />
        <Story />
      </ChakraProvider>
    ),
  ],
};

export default preview;
