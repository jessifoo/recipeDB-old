import { router } from '@/router';
import { uiState, useGlobalStore } from '@/stores/globalStore';
import { useCallback } from 'react';
import { useSnapshot } from 'valtio';

export function useAppState() {
  // Get reactive UI state from Valtio
  const ui = useSnapshot(uiState);

  // Get global state and actions from Zustand
  const { search, recipes, actions } = useGlobalStore();

  // Get URL state from TanStack Router
  const searchParams = router.state.search;

  // Computed values
  const isFiltered =
    search.filters.category.length > 0 || search.filters.dietary.length > 0 || search.query !== '';

  // Combined actions
  const viewRecipe = useCallback(
    (recipeId: number) => {
      actions.addRecentlyViewed(recipeId);
      router.navigate({
        to: '/recipe/$recipeId',
        params: { recipeId: recipeId.toString() },
      });
    },
    [actions]
  );

  const toggleTheme = useCallback(() => {
    uiState.theme = uiState.theme === 'light' ? 'dark' : 'light';
  }, []);

  const showToast = useCallback((message: string, type: 'success' | 'error' = 'success') => {
    uiState.toast = { message, type };
    setTimeout(() => {
      uiState.toast = null;
    }, 3000);
  }, []);

  return {
    // State
    ui,
    search,
    recipes,
    searchParams,
    isFiltered,

    // Actions
    ...actions,
    viewRecipe,
    toggleTheme,
    showToast,

    // URL navigation
    navigate: router.navigate,
  };
}
