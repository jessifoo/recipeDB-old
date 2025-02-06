import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { apiClient } from '../../services/api';
import type { IngredientCreate } from '../../types/api';

// Query keys
export const ingredientKeys = {
  all: ['ingredients'] as const,
  lists: () => [...ingredientKeys.all, 'list'] as const,
  list: (page: number, limit: number) =>
    [...ingredientKeys.lists(), { page, limit }] as const,
  categories: () => [...ingredientKeys.all, 'categories'] as const,
};

export function useIngredients(page = 1, limit = 100) {
  return useQuery({
    queryKey: ingredientKeys.list(page, limit),
    queryFn: () => apiClient.getIngredients(page, limit),
  });
}

export function useIngredientCategories() {
  return useQuery({
    queryKey: ingredientKeys.categories(),
    queryFn: () => apiClient.getIngredientCategories(),
  });
}

export function useCreateIngredient() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (ingredient: IngredientCreate) =>
      apiClient.createIngredient(ingredient),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ingredientKeys.lists() });
    },
  });
}
