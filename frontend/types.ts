export interface Recipe {
  id: number;
  title: string;
  description: string;
  ingredients: string[];
  instructions: string[];
  meal_type: string;
  cooking_method: string;
  allergenWarnings: string[];
  is_collection: boolean;
  date_added: string;
  is_dairy_free: boolean;
  is_gluten_free: boolean;
  is_soy_free: boolean;
  is_nut_free: boolean;
  is_egg_free: boolean;
  is_fpies_friendly: boolean;
  fpies_triggers: string[];
  fpies_safe_substitutes: Record<string, string>;
  allergens: string[];
  times_made: number;
  protein_type: string;
  prep_time: number;
  cook_time: number;
  servings: number;
  image_url: string;
  image_preview_url: string;
}

export interface SearchFilters {
  isDairyFree?: boolean;
  isEggFree?: boolean;
  isSoyFree?: boolean;
  isGlutenFree?: boolean;
  isNutFree?: boolean;
  isFpiesFriendly?: boolean;
}

export interface RecipeStore {
  recipes: Recipe[];
  loading: boolean;
  error: string | null;
  filters: SearchFilters;
  searchRecipes: (query: string, filters?: SearchFilters) => Promise<void>;
  toggleFavorite: (recipeId: number) => void;
  setFilters: (filters: SearchFilters) => void;
}
