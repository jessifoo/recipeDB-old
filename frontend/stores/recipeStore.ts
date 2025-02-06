import { create } from 'zustand';
import type { Recipe, RecipeFilters } from '../types';
import { api } from '../utils/api';

interface RecipeStore {
  // State
  recipes: Recipe[];
  loading: boolean;
  error: string | null;
  selectedRecipe: Recipe | null;
  searchQuery: string;
  filters: RecipeFilters;

  // Actions
  searchRecipes: (query: string, filters: RecipeFilters) => Promise<void>;
  saveRecipe: (recipe: Recipe) => Promise<void>;
  deleteRecipe: (id: number) => Promise<void>;
  setSelectedRecipe: (recipe: Recipe | null) => void;
  setFilters: (filters: RecipeFilters) => void;
  toggleFavorite: (id: number) => Promise<void>;
  shareRecipe: (id: number) => Promise<void>;
  clearError: () => void;
}

export const useRecipeStore = create<RecipeStore>((set, get) => ({
  // Initial state
  recipes: [],
  loading: false,
  error: null,
  selectedRecipe: null,
  searchQuery: '',
  filters: {
    is_dairy_free: false,
    is_egg_free: false,
    is_soy_free: false,
    protein_type: undefined,
  },

  // Actions
  searchRecipes: async (query: string, filters: RecipeFilters) => {
    try {
      set({ loading: true, error: null });
      const response = await api.recipes.search(query, filters);
      set({
        recipes: response.data,
        searchQuery: query,
        filters,
        loading: false,
      });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to search recipes',
        loading: false,
      });
    }
  },

  saveRecipe: async (recipe: Recipe) => {
    try {
      set({ loading: true, error: null });
      const response = await api.recipes.create(recipe);

      // Update recipes list if it exists in current search
      const { recipes, searchQuery, filters } = get();
      if (searchQuery) {
        const updatedResponse = await api.recipes.search(searchQuery, filters);
        set({ recipes: updatedResponse.data });
      } else {
        set({ recipes: [...recipes, response.data] });
      }

      set({ loading: false });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to save recipe',
        loading: false,
      });
    }
  },

  deleteRecipe: async (id: number) => {
    try {
      set({ loading: true, error: null });
      await api.recipes.delete(id);

      // Remove from current list
      const { recipes } = get();
      set({
        recipes: recipes.filter((r) => r.id !== id),
        loading: false,
      });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to delete recipe',
        loading: false,
      });
    }
  },

  setSelectedRecipe: (recipe: Recipe | null) => {
    set({ selectedRecipe: recipe });
  },

  setFilters: (filters: RecipeFilters) => {
    set({ filters });

    // Re-run search with new filters if we have a query
    const { searchQuery } = get();
    if (searchQuery) {
      get().searchRecipes(searchQuery, filters);
    }
  },

  toggleFavorite: async (id: number) => {
    try {
      const response = await api.recipes.favorite(id);

      // Update recipe in state
      const { recipes, selectedRecipe } = get();
      const updatedRecipes = recipes.map((recipe) => (recipe.id === id ? response.data : recipe));

      set({
        recipes: updatedRecipes,
        selectedRecipe: selectedRecipe?.id === id ? response.data : selectedRecipe,
      });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to update favorite',
      });
    }
  },

  shareRecipe: async (id: number) => {
    try {
      await api.recipes.share(id);
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to share recipe',
      });
    }
  },

  clearError: () => {
    set({ error: null });
  },
}));
