import { Box, Text, VStack } from '@chakra-ui/react';

import { RecipeAllergenBadges } from './RecipeAllergenBadges';
import { RecipeMetadata } from './RecipeMetadata';

import type { Recipe } from '../../types/recipe';

/**
 * RecipeCard displays a single recipe in a card format
 * with image, title, cooking info, and dietary restrictions.
 */
interface RecipeCardProps {
  recipe: Recipe;
  onClick?: () => void;
}

export const RecipeCard: React.FC<RecipeCardProps> = ({ recipe, onClick }) => {
  const {
    title,
    description,
    meal_type,
    cooking_method = 'other',
    image_url,
  } = recipe;

  return (
    <Box
      onClick={onClick}
      borderWidth="1px"
      borderRadius="lg"
      p={4}
      cursor="pointer"
      _hover={{ shadow: 'md' }}
      role="article"
    >
      <VStack align="stretch" spacing={4}>
        {image_url && (
          <Box
            height="200px"
            backgroundImage={`url(${image_url})`}
            backgroundSize="cover"
            backgroundPosition="center"
            borderRadius="md"
          />
        )}
        <Text fontSize="xl" fontWeight="bold">
          {title}
        </Text>
        <Text color="gray.600">{description}</Text>
        <Text>
          {meal_type} •{' '}
          {cooking_method
            .split('_')
            .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ')}
        </Text>
        <RecipeMetadata recipe={recipe} showServings={false} />
        <RecipeAllergenBadges recipe={recipe} />
      </VStack>
    </Box>
  );
};
