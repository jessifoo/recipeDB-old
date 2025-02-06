import type React from 'react';
import { useEffect, useState } from 'react';

import { Box, Container, Grid, Stack, Spinner } from '@chakra-ui/react';

import { RecipeCard } from './recipe/RecipeCard';
import { RecipeFilterComponent } from './recipe/RecipeFilters';

import type { Recipe, RecipeFilters } from '../types/recipe';

const RecipeList: React.FC = () => {
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [filters, setFilters] = useState<RecipeFilters>({
    search_query: '',
    meal_type: '',
    cooking_method: '',
    is_dairy_free: false,
    is_soy_free: false,
    is_gluten_free: false,
    is_nut_free: false,
    is_egg_free: false,
    is_collection: false,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRecipes = async () => {
      setLoading(true);
      try {
        const queryParams = new URLSearchParams();

        if (filters.meal_type) {
          queryParams.append('meal_type', filters.meal_type);
        }
        if (filters.cooking_method) {
          queryParams.append('cooking_method', filters.cooking_method);
        }
        if (filters.search_query) {
          queryParams.append('q', filters.search_query);
        }
        if (filters.is_collection !== undefined) {
          queryParams.append('is_collection', filters.is_collection.toString());
        }

        const response = await fetch(`/api/recipes?${queryParams.toString()}`);
        const data = await response.json();
        setRecipes(data);
      } catch (error) {
        console.error('Failed to fetch recipes:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchRecipes();
  }, [filters]);

  const handleFilterChange = (
    key: keyof RecipeFilters,
    value: string | boolean
  ) => {
    setFilters((prev) => ({ ...prev, [key]: value }));
  };

  const filterRecipes = (recipes: Recipe[]): Recipe[] => {
    return recipes.filter((recipe) => {
      // Add allergen filters
      const allergens: string[] = [];
      if (filters.is_dairy_free) {
        allergens.push('dairy');
      }
      if (filters.is_soy_free) {
        allergens.push('soy');
      }
      if (filters.is_gluten_free) {
        allergens.push('gluten');
      }
      if (filters.is_nut_free) {
        allergens.push('nuts');
      }
      if (filters.is_egg_free) {
        allergens.push('eggs');
      }

      return allergens.every(
        (allergen) => !recipe.allergens.includes(allergen)
      );
    });
  };

  const filteredRecipes = filterRecipes(recipes);

  return (
    <Container maxW="container.xl" p={4}>
      <Stack spacing={4}>
        <RecipeFilterComponent
          filters={filters}
          onFilterChange={handleFilterChange}
        />

        {loading ? (
          <Box textAlign="center" py={8}>
            <Spinner size="xl" />
          </Box>
        ) : (
          <Grid
            templateColumns={{
              base: '1fr',
              sm: 'repeat(2, 1fr)',
              lg: 'repeat(3, 1fr)',
            }}
            gap={4}
          >
            {filteredRecipes.map((recipe) => (
              <RecipeCard key={recipe.id} recipe={recipe} />
            ))}
          </Grid>
        )}
      </Stack>
    </Container>
  );
};

export default RecipeList;
