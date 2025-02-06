import { useTheme } from '@chakra-ui/react';
import { get } from '@chakra-ui/utils';

/**
 * Custom hook to access theme tokens with TypeScript support
 * Provides easy access to colors, spacing, and other theme values
 */
export function useThemeTokens() {
  const theme = useTheme();

  return {
    /**
     * Get a color token from the theme
     * @example getColor('accent.500')
     */
    getColor: (token: string) => get(theme.colors, token),

    /**
     * Get a spacing token from the theme
     * @example getSpace(4) // returns '1rem'
     */
    getSpace: (token: string | number) => get(theme.space, token),

    /**
     * Get a font size token from the theme
     * @example getFontSize('md')
     */
    getFontSize: (token: string) => get(theme.fontSizes, token),

    /**
     * Get a radius token from the theme
     * @example getRadius('md')
     */
    getRadius: (token: string) => get(theme.radii, token),
  };
}
