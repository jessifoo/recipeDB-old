import type { AxiosError, RawAxiosRequestHeaders } from 'axios';

export interface ApiConfig {
  baseUrl: string;
  defaultParams: Record<string, string | number | boolean>;
  headers: RawAxiosRequestHeaders;
  timeout: number;
}

export interface RequestInterceptor<TRequest = unknown> {
  id?: string;
  onRequest: (config: ApiRequestConfig<TRequest>) => ApiRequestConfig<TRequest>;
}

export interface ResponseInterceptor<TResponse = unknown> {
  id?: string;
  onResponse: (response: TResponse) => Promise<TResponse> | TResponse;
  onError: (error: ApiError) => Promise<never>;
}

export interface ApiRequestConfig<TRequest = unknown> {
  url: string;
  method: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';
  params?: Record<string, string | number | boolean>;
  data?: TRequest;
  headers?: RawAxiosRequestHeaders;
  timeout?: number;
  validateStatus?: (status: number) => boolean;
  retry?: {
    maxRetries: number;
    delayMs: number;
    retryCondition?: (error: ApiError) => boolean;
  };
}

export interface ApiError extends AxiosError {
  details: ApiErrorDetails;
  isRetryable?: boolean;
}

export interface ApiErrorDetails {
  message: string;
  statusCode?: number;
  config?: ApiRequestConfig;
  originalError?: Error;
  context?: Record<string, unknown>;
  retryAttempt?: number;
}

export interface ApiSource {
  name: string;
  description: string;
  defaultConfig: Partial<ApiConfig>;
  parameterDocs: ApiParameterDocs[];
}

export interface ApiParameterDocs {
  name: string;
  description: string;
  type: 'string' | 'number' | 'boolean' | 'array';
  required: boolean;
  default?: string | number | boolean | string[];
  options?: string[];
}

// Recipe Types
export interface Recipe {
  recipe_id: number;
  title: string;
  image_url?: string;
  source_url?: string;
  prep_time_minutes?: number;
  cook_time_minutes?: number;
  servings?: number;
  is_favorite: boolean;
  variations?: string;
  last_made_date?: string;
  created_at: string;
  updated_at: string;
  instructions: RecipeInstruction[];
  allergens: Allergen[];
  ingredients: Ingredient[];
  meal_types: MealType[];
  cook_methods: CookMethod[];
  protein_types: ProteinType[];
  cuisine_types: CuisineType[];
}

export interface RecipeCreate {
  title: string;
  image_url?: string;
  source_url?: string;
  prep_time_minutes?: number;
  cook_time_minutes?: number;
  servings?: number;
  is_favorite?: boolean;
  variations?: string;
  instructions: RecipeInstructionCreate[];
}

export interface RecipeUpdate {
  title?: string;
  image_url?: string;
  source_url?: string;
  prep_time_minutes?: number;
  cook_time_minutes?: number;
  servings?: number;
  is_favorite?: boolean;
  variations?: string;
  instructions?: RecipeInstructionCreate[];
}

// Recipe Instructions
export interface RecipeInstruction {
  instruction_id: number;
  recipe_id: number;
  step_number: number;
  instruction: string;
}

export interface RecipeInstructionCreate {
  step_number: number;
  instruction: string;
}

// Ingredients
export interface Ingredient {
  ingredient_id: number;
  name: string;
  category_id: number;
}

export interface IngredientCreate {
  name: string;
  category_id: number;
}

export interface IngredientCategory {
  category_id: number;
  name: string;
}

// Allergens
export interface Allergen {
  allergen_id: number;
  name: string;
  severity?: string;
}

export interface AllergenCreate {
  name: string;
  severity?: string;
}

// Cook Methods
export interface CookMethod {
  method_id: number;
  name: string;
}

export interface CookMethodCreate {
  name: string;
}

// Protein Types
export interface ProteinType {
  protein_id: number;
  name: string;
}

export interface ProteinTypeCreate {
  name: string;
}

// Meal Types
export interface MealType {
  meal_type_id: number;
  name: string;
}

export interface MealTypeCreate {
  name: string;
}

// Cuisine Types
export interface CuisineType {
  cuisine_id: number;
  name: string;
  last_used_date?: string;
}

export interface CuisineTypeCreate {
  name: string;
  last_used_date?: string;
}

// Dietary Restrictions
export interface DietaryRestriction {
  restriction_id: number;
  name: string;
}

export interface DietaryRestrictionCreate {
  name: string;
}

// Family Members
export interface FamilyMember {
  member_id: number;
  name: string;
  birth_date?: string;
  notes?: string;
}

export interface FamilyMemberCreate {
  name: string;
  birth_date?: string;
  notes?: string;
}

// Meal Plans
export interface MealPlan {
  plan_id: number;
  recipe_id: number;
  planned_date: string;
  meal_type_id: number;
  notes?: string;
  member_id: number;
}

export interface MealPlanCreate {
  recipe_id: number;
  planned_date: string;
  meal_type_id: number;
  notes?: string;
  member_id: number;
}

// Recipe Search
export interface RecipeSearchFilters {
  cuisine_type?: string;
  difficulty?: string;
  max_cooking_time?: number;
  tags?: string[];
  ingredients?: string[];
  allergens_exclude?: string[];
  dietary_restrictions?: string[];
}

export interface RecipeSearchResult {
  id: string;
  title: string;
  description?: string;
  image_url?: string;
  source_url?: string;
  prep_time?: number;
  cook_time?: number;
  total_time?: number;
  servings?: number;
  cuisine?: string;
  diet?: string[];
  ingredients?: string[];
  instructions?: string[];
  source: string;
}

export interface RecipeList {
  total: number;
  results: RecipeSearchResult[];
  source: string;
}

// Recipe Ratings
export interface RecipeRating {
  rating_id: number;
  recipe_id: number;
  member_id: number;
  rating: number;
  review?: string;
  created_at: string;
}

export interface RecipeRatingCreate {
  recipe_id: number;
  member_id: number;
  rating: number;
  review?: string;
}
