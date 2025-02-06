import type { RecipeList } from '@/types/api';
import { Box, Grid, Text } from '@chakra-ui/react';
import { RecipeCard } from '../molecules/RecipeCard';

interface RecipeGridProps {
  recipes: RecipeList | null;
}

export function RecipeGrid({ recipes }: RecipeGridProps) {
  if (!recipes?.results?.length) {
    return (
      <Box textAlign="center" py={8}>
        <Text color="gray.600" fontSize="lg">
          No recipes found. Try adjusting your search criteria.
        </Text>
      </Box>
    );
  }

  return (
    <Grid
      templateColumns={{
        base: '1fr',
        md: 'repeat(2, 1fr)',
        lg: 'repeat(3, 1fr)',
      }}
      gap={6}
      width="100%"
    >
      {recipes.results.map((recipe) => (
        <RecipeCard key={recipe.id} recipe={recipe} />
      ))}
    </Grid>
  );
}
