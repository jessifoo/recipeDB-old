export type ProteinType =
  | 'chicken'
  | 'beef'
  | 'pork'
  | 'fish'
  | 'shellfish'
  | 'turkey'
  | 'lamb'
  | 'vegetarian'
  | 'other';

export type MealType = 'breakfast' | 'lunch' | 'dinner' | 'dessert' | 'snack' | 'other';

export type CookingMethod =
  | 'bake'
  | 'stovetop'
  | 'grill'
  | 'slow_cooker'
  | 'instant_pot'
  | 'air_fryer'
  | 'refrigerate'
  | 'freeze';

export interface User {
  id: number;
  name: string;
  allergies: string[];
  preferences: Record<string, unknown>;
  healthConditions: string[];
}

export interface MethodDifference {
  type: string;
  description: string;
  base: string;
  variation: string;
}

export interface TimingDifference {
  type: string;
  base: string;
  variation: string;
}

export interface KeyDifferences {
  ingredients: {
    added: string[];
    removed: string[];
  };
  methods: MethodDifference[];
  timing: TimingDifference[];
}

export interface VariationGroup {
  base_title: string;
  recipe_count: number;
  description: string;
}

export interface Recipe {
  id: number;
  title: string;
  description: string;
  meal_type: MealType;
  is_collection: boolean;
  source_url?: string;
  image_url?: string;
  image_preview_url?: string;
  ingredients: string[];
  instructions: string[];
  prep_time?: number;
  cook_time?: number;
  cooking_method?: CookingMethod;
  protein_type?: ProteinType;
  servings?: number;
  date_added: string;
  is_dairy_free: boolean;
  is_soy_free: boolean;
  is_gluten_free: boolean;
  is_nut_free: boolean;
  is_egg_free: boolean;
  is_fpies_friendly: boolean;
  fpies_triggers: string[];
  fpies_safe_substitutes: Record<string, string>;
  allergens: string[];
  last_made?: string;
  times_made: number;
  rating?: number;
  variation_group?: {
    base_title: string;
    recipe_count: number;
    description: string;
  };
  variation_notes?: string;
  favorite?: boolean;
  key_differences?: {
    ingredients: {
      added: string[];
      removed: string[];
    };
    methods: Array<{
      type: string;
      description: string;
      base: string;
      variation: string;
    }>;
    timing: Array<{
      type: string;
      base: string;
      variation: string;
    }>;
  };
}

export interface CookingHistory {
  id: number;
  recipeId: number;
  dateCooked: string;
  notes?: string;
  recipe?: Recipe;
}

export interface RecipeFilters {
  meal_type?: MealType;
  cooking_method?: CookingMethod;
  protein_type?: ProteinType;
  is_collection?: boolean;
  allergens?: string[];
  is_fpies_friendly?: boolean;
  is_dairy_free?: boolean;
  search_query?: string;
}

// Export RecipeFilters as SearchFilters for API compatibility
export type SearchFilters = RecipeFilters;

export interface MealPlan {
  id: string;
  startDate: string;
  endDate: string;
  meals: MealPlanItem[];
}

export interface MealPlanItem {
  id: string;
  recipeId: string;
  date: string;
  mealType: MealType;
  servings: number;
  notes?: string;
}

export interface RecipeCategory {
  id: string;
  name: string;
  description?: string;
  recipes: string[]; // Recipe IDs
}
