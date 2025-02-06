import { proxy, subscribe } from 'valtio';
import { create } from 'zustand';
import { devtools, subscribeWithSelector } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';
import { router } from '../router';
import type { SearchParams } from '../router';

// Valtio state for reactive UI elements
export const uiState = proxy({
  theme: 'light' as 'light' | 'dark',
  sidebarOpen: true,
  modals: new Set<string>(),
  toast: null as { message: string; type: 'success' | 'error' } | null,
});

// Subscribe to theme changes
subscribe(uiState, () => {
  document.documentElement.classList.toggle('dark', uiState.theme === 'dark');
});

// Types for our main store
interface GlobalState {
  // URL-synced state
  search: {
    query: string;
    filters: {
      category: string[];
      dietary: string[];
      cookingTime: [number, number];
    };
    page: number;
  };
  // App state
  recipes: {
    favorites: number[];
    recentlyViewed: number[];
    userNotes: Record<number, string>;
  };
  // Action creators
  actions: {
    updateSearch: (params: Partial<SearchParams>) => void;
    toggleFavorite: (recipeId: number) => void;
    addRecentlyViewed: (recipeId: number) => void;
    updateNote: (recipeId: number, note: string) => void;
    clearHistory: () => void;
  };
}

// Create store with all middleware
export const useGlobalStore = create<GlobalState>()(
  subscribeWithSelector(
    devtools(
      immer((set, _get) => ({
        // Initial state
        search: {
          query: '',
          filters: {
            category: [],
            dietary: [],
            cookingTime: [0, 180],
          },
          page: 1,
        },
        recipes: {
          favorites: [],
          recentlyViewed: [],
          userNotes: {},
        },
        // Actions
        actions: {
          updateSearch: (params) => {
            set((state) => {
              // Update internal state
              if (params.q) {
                state.search.query = params.q;
              }
              if (params.page) {
                state.search.page = params.page;
              }
              if (params.filters) {
                const filters = JSON.parse(params.filters);
                state.search.filters = { ...state.search.filters, ...filters };
              }
            });
            // Sync with URL
            router.navigate({
              search: (old) => ({ ...old, ...params }),
            });
          },

          toggleFavorite: (recipeId) => {
            set((state) => {
              const favorites = state.recipes.favorites;
              const index = favorites.indexOf(recipeId);
              if (index === -1) {
                favorites.push(recipeId);
              } else {
                favorites.splice(index, 1);
              }
            });
          },

          addRecentlyViewed: (recipeId) => {
            set((state) => {
              const recent = state.recipes.recentlyViewed;
              const index = recent.indexOf(recipeId);
              if (index !== -1) {
                recent.splice(index, 1);
              }
              recent.unshift(recipeId);
              if (recent.length > 10) {
                recent.pop();
              }
            });
          },

          updateNote: (recipeId, note) => {
            set((state) => {
              state.recipes.userNotes[recipeId] = note;
            });
          },

          clearHistory: () => {
            set((state) => {
              state.recipes.recentlyViewed = [];
            });
          },
        },
      }))
    )
  )
);

// Subscribe to relevant state changes
useGlobalStore.subscribe(
  (state) => state.recipes.favorites,
  (favorites) => {
    localStorage.setItem('favorites', JSON.stringify(favorites));
  }
);

// Create a middleware for analytics
export const withAnalytics = (_config: Record<string, unknown>) => (next: (args: unknown[]) => unknown) => (args: unknown[]) => {
  const result = next(args);
  if (args[0]?.type?.includes('action')) {
    // Send to analytics service
  }
  return result;
};
