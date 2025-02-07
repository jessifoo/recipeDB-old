import type { SystemStyleObject } from '@chakra-ui/react';

type ResponsiveStyle<T> = T | Partial<Record<string, T>>;

/**
 * Creates responsive styles using a mobile-first approach
 * @example
 * createResponsiveStyle({
 *   base: { fontSize: 'sm' },
 *   md: { fontSize: 'md' },
 *   lg: { fontSize: 'lg' },
 * })
 */
export function createResponsiveStyle<T extends SystemStyleObject>(
  styles: ResponsiveStyle<T>
): SystemStyleObject {
  if (typeof styles !== 'object' || styles === null) {
    return styles as SystemStyleObject;
  }

  return Object.entries(styles).reduce((acc: SystemStyleObject, [breakpoint, style]) => {
    if (breakpoint === 'base') {
      Object.assign(acc, style);
      return acc;
    }
    acc[`@media screen and (min-width: ${breakpoint})`] = style;
    return acc;
  }, {});
}

/**
 * Creates a responsive value for Chakra UI props
 * @example
 * responsive('fontSize', ['sm', 'md', 'lg'])
 * // or
 * responsive('spacing', { base: 2, md: 4, lg: 6 })
 */
export function responsive<T>(
  property: string,
  value: ResponsiveStyle<T>
): { [key: string]: ResponsiveStyle<T> } {
  return { [property]: value };
}

export const getResponsiveValue = <T>(
  styles: ResponsiveStyle<T>,
  breakpoint: string
): T | undefined => {
  if (typeof styles === 'object' && !Array.isArray(styles)) {
    return (styles as Record<string, T>)[breakpoint];
  }
  return styles as T;
};
