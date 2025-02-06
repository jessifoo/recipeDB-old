import { Box, Image, type ImageProps } from '@chakra-ui/react';

interface RecipeImageProps extends Omit<ImageProps, 'fallback'> {
  title: string;
  imageUrl?: string;
}

/**
 * RecipeImage component with consistent styling and fallback
 */
export const RecipeImage = ({
  title,
  imageUrl,
  ...props
}: RecipeImageProps) => {
  if (!imageUrl) {
    return (
      <Box
        w="100%"
        h="200px"
        bg="gray.100"
        borderRadius="lg"
        _dark={{ bg: 'gray.700' }}
      />
    );
  }

  return (
    <Image
      src={imageUrl}
      alt={title}
      borderRadius="lg"
      objectFit="cover"
      w="100%"
      h="200px"
      fallback={
        <Box
          w="100%"
          h="200px"
          bg="gray.100"
          borderRadius="lg"
          _dark={{ bg: 'gray.700' }}
        />
      }
      {...props}
    />
  );
};

export default RecipeImage;
