import type { Recipe, RecipeFilters } from '@/types/recipe';

export const filterRecipes = (recipes: Recipe[], filters: RecipeFilters): Recipe[] => {
  return recipes.filter((recipe) => {
    if (filters.searchQuery) {
      const query = filters.searchQuery.toLowerCase();
      const matchesTitle = recipe.title.toLowerCase().includes(query);
      const matchesDescription = recipe.description.toLowerCase().includes(query);
      if (!matchesTitle && !matchesDescription) {
        return false;
      }
    }

    if (filters.allergens?.length) {
      const hasAllergen = recipe.allergens.some((allergen) =>
        filters.allergens?.includes(allergen)
      );
      if (hasAllergen) {
        return false;
      }
    }

    return true;
  });
};

export const paginateRecipes = (recipes: Recipe[], page = 1, perPage = 12): Recipe[] => {
  const start = (page - 1) * perPage;
  const end = start + perPage;
  return recipes.slice(start, end);
};
