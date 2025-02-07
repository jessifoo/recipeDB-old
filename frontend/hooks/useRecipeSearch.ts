import { api } from '@/utils/api';
import { useQuery } from '@tanstack/react-query';

export function useRecipeSearch(
  query: string,
  options?: {
    protein?: string;
    isDairyFree?: boolean;
    isSoyFree?: boolean;
    isEggFree?: boolean;
    page?: number;
    limit?: number;
  }
) {
  return useQuery({
    queryKey: ['recipes', 'search', query, options],
    queryFn: () => api.recipes.search(query, options),
    enabled: query.length > 0,
    staleTime: 1000 * 60 * 5, // Cache for 5 minutes
  });
}
