import { Button as ChakraButton, type ButtonProps } from '@chakra-ui/react';

interface BaseButtonProps extends ButtonProps {
  label: string;
}

/**
 * Base Button component that follows the design system
 * Uses theme-based styling with no inline styles
 */
export const Button = ({ label, children, ...props }: BaseButtonProps) => (
  <ChakraButton {...props}>{label || children}</ChakraButton>
);

export default Button;
