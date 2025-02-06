import { useQuery } from '@tanstack/react-query';
import { apiClient } from '../../services/api';
import type { RecipeSearchFilters } from '../../types/api';

// Query keys
export const recipeSearchKeys = {
  all: ['recipe-search'] as const,
  search: (
    query: string,
    filters?: RecipeSearchFilters,
    page?: number,
    limit?: number
  ) => [...recipeSearchKeys.all, { query, filters, page, limit }] as const,
};

export function useRecipeSearch(
  query: string,
  filters?: RecipeSearchFilters,
  page = 1,
  limit = 20,
  enabled = true
) {
  return useQuery({
    queryKey: recipeSearchKeys.search(query, filters, page, limit),
    queryFn: () => apiClient.searchRecipes(query, filters, page, limit),
    enabled: enabled && !!query,
  });
}
