import { SimpleGrid } from '@chakra-ui/react';

import { RecipeCard } from './RecipeCard';

import type { Recipe } from '../../types/recipe';

interface RecipeGridProps {
  recipes: Recipe[];
  onRecipeClick?: (recipe: Recipe) => void;
}

/**
 * RecipeGrid displays a responsive grid of RecipeCards
 */
export const RecipeGrid = ({ recipes, onRecipeClick }: RecipeGridProps) => (
  <SimpleGrid columns={{ base: 1, md: 2, lg: 3 }}>
    {recipes.map((recipe) => (
      <RecipeCard
        key={recipe.id}
        recipe={recipe}
        onClick={() => onRecipeClick?.(recipe)}
      />
    ))}
  </SimpleGrid>
);
