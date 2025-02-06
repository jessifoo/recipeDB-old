import axios, { AxiosInstance } from 'axios';
import type {
  Allergen,
  AllergenCreate,
  CookMethod,
  CookMethodCreate,
  CuisineType,
  CuisineTypeCreate,
  DietaryRestriction,
  DietaryRestrictionCreate,
  FamilyMember,
  FamilyMemberCreate,
  Ingredient,
  IngredientCategory,
  IngredientCreate,
  MealPlan,
  MealPlanCreate,
  MealType,
  MealTypeCreate,
  ProteinType,
  ProteinTypeCreate,
  Recipe,
  RecipeCreate,
  RecipeList,
  RecipeRating,
  RecipeRatingCreate,
  RecipeSearchFilters,
  RecipeUpdate,
} from '../types/api';

class ApiClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api',
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  // Recipes
  async getRecipes(page = 1, limit = 20) {
    const { data } = await this.client.get<Recipe[]>('/recipes', {
      params: { skip: (page - 1) * limit, limit },
    });
    return data;
  }

  async getRecipe(id: number) {
    const { data } = await this.client.get<Recipe>(`/recipes/${id}`);
    return data;
  }

  async createRecipe(recipe: RecipeCreate) {
    const { data } = await this.client.post<Recipe>('/recipes', recipe);
    return data;
  }

  async updateRecipe(id: number, recipe: RecipeUpdate) {
    const { data } = await this.client.put<Recipe>(`/recipes/${id}`, recipe);
    return data;
  }

  async deleteRecipe(id: number) {
    await this.client.delete(`/recipes/${id}`);
  }

  // Recipe Search
  async searchRecipes(
    query: string,
    filters?: RecipeSearchFilters,
    page = 1,
    limit = 20
  ) {
    const { data } = await this.client.get<RecipeList>('/recipe-search', {
      params: {
        query,
        ...filters,
        page,
        page_size: limit,
      },
    });
    return data;
  }

  // Ingredients
  async getIngredients(page = 1, limit = 100) {
    const { data } = await this.client.get<Ingredient[]>('/ingredients', {
      params: { skip: (page - 1) * limit, limit },
    });
    return data;
  }

  async createIngredient(ingredient: IngredientCreate) {
    const { data } = await this.client.post<Ingredient>(
      '/ingredients',
      ingredient
    );
    return data;
  }

  // Ingredient Categories
  async getIngredientCategories() {
    const { data } = await this.client.get<IngredientCategory[]>(
      '/ingredient-categories'
    );
    return data;
  }

  // Allergens
  async getAllergens() {
    const { data } = await this.client.get<Allergen[]>('/allergens');
    return data;
  }

  async createAllergen(allergen: AllergenCreate) {
    const { data } = await this.client.post<Allergen>('/allergens', allergen);
    return data;
  }

  // Cook Methods
  async getCookMethods() {
    const { data } = await this.client.get<CookMethod[]>('/cook-methods');
    return data;
  }

  async createCookMethod(method: CookMethodCreate) {
    const { data } = await this.client.post<CookMethod>(
      '/cook-methods',
      method
    );
    return data;
  }

  // Protein Types
  async getProteinTypes() {
    const { data } = await this.client.get<ProteinType[]>('/protein-types');
    return data;
  }

  async createProteinType(type: ProteinTypeCreate) {
    const { data } = await this.client.post<ProteinType>(
      '/protein-types',
      type
    );
    return data;
  }

  // Meal Types
  async getMealTypes() {
    const { data } = await this.client.get<MealType[]>('/meal-types');
    return data;
  }

  async createMealType(type: MealTypeCreate) {
    const { data } = await this.client.post<MealType>('/meal-types', type);
    return data;
  }

  // Cuisine Types
  async getCuisineTypes() {
    const { data } = await this.client.get<CuisineType[]>('/cuisine-types');
    return data;
  }

  async createCuisineType(type: CuisineTypeCreate) {
    const { data } = await this.client.post<CuisineType>(
      '/cuisine-types',
      type
    );
    return data;
  }

  // Dietary Restrictions
  async getDietaryRestrictions() {
    const { data } = await this.client.get<DietaryRestriction[]>(
      '/dietary-restrictions'
    );
    return data;
  }

  async createDietaryRestriction(restriction: DietaryRestrictionCreate) {
    const { data } = await this.client.post<DietaryRestriction>(
      '/dietary-restrictions',
      restriction
    );
    return data;
  }

  // Family Members
  async getFamilyMembers() {
    const { data } = await this.client.get<FamilyMember[]>('/family-members');
    return data;
  }

  async createFamilyMember(member: FamilyMemberCreate) {
    const { data } = await this.client.post<FamilyMember>(
      '/family-members',
      member
    );
    return data;
  }

  // Meal Plans
  async getMealPlans(page = 1, limit = 20) {
    const { data } = await this.client.get<MealPlan[]>('/meal-plans', {
      params: { skip: (page - 1) * limit, limit },
    });
    return data;
  }

  async createMealPlan(plan: MealPlanCreate) {
    const { data } = await this.client.post<MealPlan>('/meal-plans', plan);
    return data;
  }

  // Recipe Ratings
  async getRecipeRatings(recipeId: number) {
    const { data } = await this.client.get<RecipeRating[]>(
      `/recipes/${recipeId}/ratings`
    );
    return data;
  }

  async createRecipeRating(rating: RecipeRatingCreate) {
    const { data } = await this.client.post<RecipeRating>(
      '/recipe-ratings',
      rating
    );
    return data;
  }
}

export const apiClient = new ApiClient();
