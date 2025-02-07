import { breakpoints } from './breakpoints';
import { colors } from './colors';
import { radii } from './radii';
import { spacing } from './spacing';
import { typography } from './typography';

export const foundations = {
  colors,
  ...typography,
  space: spacing,
  sizes: spacing,
  breakpoints,
  radii,
};
