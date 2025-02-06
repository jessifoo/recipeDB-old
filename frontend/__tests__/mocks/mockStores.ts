import type { FamilyProfileState } from '../../stores/familyProfileStore';
import type { Recipe, SearchFilters } from '../../types';

export const mockRecipeWithAllergens: Recipe = {
  id: 1,
  title: 'Recipe with Hidden Allergens',
  description: 'A test recipe with allergens',
  ingredients: ['natural flavors', 'casein'],
  instructions: ['step 1'],
  meal_type: 'dinner',
  cooking_method: 'stovetop',
  allergenWarnings: ['Contains dairy derivatives'],
  is_collection: false,
  date_added: new Date().toISOString(),
  is_dairy_free: false,
  is_gluten_free: true,
  is_soy_free: true,
  is_nut_free: true,
  is_egg_free: true,
  is_fpies_friendly: true,
  fpies_triggers: [],
  fpies_safe_substitutes: {},
  allergens: ['dairy'],
  times_made: 0,
  protein_type: 'other',
  prep_time: 15,
  cook_time: 30,
  servings: 4,
  image_url: 'test.jpg',
  image_preview_url: 'test.jpg'
};

export const mockFamilyProfile: FamilyProfileState = {
  members: [
    {
      id: '1',
      name: 'Test User',
      allergies: ['dairy', 'eggs'],
      fpiesTriggers: [],
      safeSubstitutes: {},
      reactionHistory: []
    }
  ],
  activeProfile: '1',
  addMember: jest.fn(),
  updateMember: jest.fn(),
  setActiveProfile: jest.fn(),
  addReaction: jest.fn(),
  addSafeSubstitute: jest.fn()
};

export type RecipeStore = {
  recipes: Recipe[];
  loading: boolean;
  error: string | null;
  filters: SearchFilters;
  searchRecipes: () => Promise<void>;
  toggleFavorite: () => void;
  setFilters: () => void;
};

export const createMockRecipeStore = (overrides: Partial<RecipeStore> = {}): RecipeStore => ({
  recipes: [],
  loading: false,
  error: null,
  filters: {
    isDairyFree: false,
    isEggFree: false,
    isSoyFree: false,
    isGlutenFree: false,
    isNutFree: false,
    isFpiesFriendly: false
  },
  searchRecipes: jest.fn().mockResolvedValue(undefined),
  toggleFavorite: jest.fn(),
  setFilters: jest.fn(),
  ...overrides
});
