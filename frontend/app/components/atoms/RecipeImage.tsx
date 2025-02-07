import { Box, Image, ImageProps } from '@chakra-ui/react';

interface RecipeImageProps extends Omit<ImageProps, 'src'> {
  imageUrl?: string;
  title: string;
}

export function RecipeImage({ imageUrl, title, ...props }: RecipeImageProps) {
  if (!imageUrl) return null;

  return (
    <Box position="relative" height="200px" overflow="hidden" borderRadius="lg">
      <Image
        src={imageUrl}
        alt={title}
        objectFit="cover"
        width="100%"
        height="100%"
        fallbackSrc="/images/recipe-placeholder.jpg"
        transition="transform 0.3s ease-in-out"
        _hover={{ transform: 'scale(1.05)' }}
        {...props}
      />
    </Box>
  );
}
