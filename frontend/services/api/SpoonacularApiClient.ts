import type { ApiSource } from '../../types/api';
import type { Recipe } from '../../types/recipe';
import { BaseApiClient } from './BaseApiClient';

interface SpoonacularRecipe {
  id: number;
  title: string;
  image: string;
  imageType: string;
  servings: number;
  readyInMinutes: number;
  dairyFree: boolean;
  glutenFree: boolean;
  vegan: boolean;
  vegetarian: boolean;
  veryHealthy: boolean;
  // ... other Spoonacular specific fields
}

export class SpoonacularApiClient extends BaseApiClient {
  public static source: ApiSource = {
    name: 'Spoonacular',
    description: 'Comprehensive recipe database with detailed nutritional information',
    defaultConfig: {
      baseUrl: 'https://api.spoonacular.com',
      defaultParams: {
        apiKey: process.env.NEXT_PUBLIC_SPOONACULAR_API_KEY,
      },
    },
    parameterDocs: [
      {
        name: 'query',
        description: 'Search query for recipes',
        type: 'string',
        required: true,
      },
      {
        name: 'diet',
        description: 'Diet restrictions',
        type: 'string',
        required: false,
        options: ['vegetarian', 'vegan', 'gluten-free', 'dairy-free'],
      },
      {
        name: 'intolerances',
        description: 'Food intolerances to avoid',
        type: 'array',
        required: false,
        options: ['dairy', 'egg', 'gluten', 'peanut', 'seafood', 'shellfish', 'soy', 'wheat'],
      },
      {
        name: 'maxReadyTime',
        description: 'Maximum total cooking and prep time in minutes',
        type: 'number',
        required: false,
      },
    ],
  };

  constructor() {
    super(SpoonacularApiClient.source.defaultConfig);
  }

  private convertToRecipe(spoonacularRecipe: SpoonacularRecipe): Recipe {
    return {
      id: spoonacularRecipe.id,
      title: spoonacularRecipe.title,
      image_url: spoonacularRecipe.image,
      is_dairy_free: spoonacularRecipe.dairyFree,
      is_gluten_free: spoonacularRecipe.glutenFree,
      prep_time: spoonacularRecipe.readyInMinutes,
      servings: spoonacularRecipe.servings,
      // ... convert other fields
    } as Recipe;
  }

  public async searchRecipes(
    query: string,
    params: Record<string, string | number | boolean> = {}
  ): Promise<Recipe[]> {
    const response = await this.request<{ results: SpoonacularRecipe[] }>({
      url: '/recipes/complexSearch',
      method: 'GET',
      params: {
        query,
        addRecipeInformation: true,
        fillIngredients: true,
        ...params,
      },
    });

    return response.results.map((recipe) => this.convertToRecipe(recipe));
  }

  public async getRecipeById(id: number): Promise<Recipe> {
    const response = await this.request<SpoonacularRecipe>({
      url: `/recipes/${id}/information`,
      method: 'GET',
      params: {
        addRecipeInformation: true,
        fillIngredients: true,
      },
    });

    return this.convertToRecipe(response);
  }
}
