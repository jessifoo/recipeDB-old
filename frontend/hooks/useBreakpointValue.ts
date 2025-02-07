import { useBreakpointValue as useChakraBreakpointValue } from '@chakra-ui/react';

type ResponsiveValue<T> = T | Record<string, T> | Array<T | null>;

/**
 * Enhanced version of Chakra's useBreakpointValue with better TypeScript support
 * and fallback values
 */
export function useBreakpointValue<T>(values: ResponsiveValue<T>, defaultValue?: T): T | undefined {
  return useChakraBreakpointValue(values, { fallback: defaultValue });
}
