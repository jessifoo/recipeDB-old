import type { Recipe, RecipeFilters } from '../types';

export const mockRecipes: Recipe[] = [
  {
    id: 1,
    title: 'Dairy-Free Mac and "Cheese"',
    description: 'A creamy, dairy-free version of mac and cheese',
    meal_type: 'dinner',
    is_collection: false,
    ingredients: [
      '1 package gluten-free macaroni',
      '1 cup cashews, soaked',
      '1/4 cup nutritional yeast',
      '2 cloves garlic',
      '1 cup plant-based milk',
      'Salt and pepper to taste',
    ],
    instructions: [
      'Cook macaroni according to package instructions',
      'Blend cashews, nutritional yeast, garlic, and milk until smooth',
      'Mix sauce with cooked pasta',
      'Season to taste',
    ],
    image_url: 'https://example.com/mac.jpg',
    is_dairy_free: true,
    is_egg_free: true,
    is_soy_free: true,
    is_gluten_free: true,
    is_nut_free: false,
    is_fpies_friendly: true,
    protein_type: 'vegetarian',
    cook_time: 25,
    servings: 4,
    date_added: new Date().toISOString(),
    fpies_triggers: [],
    fpies_safe_substitutes: {},
    allergens: ['nuts'],
    times_made: 0,
  },
  {
    id: 2,
    title: 'Allergen-Free Chicken Stir Fry',
    description: 'A simple and delicious allergen-free stir fry',
    meal_type: 'dinner',
    is_collection: false,
    ingredients: [
      '2 chicken breasts, diced',
      '2 cups mixed vegetables',
      '1 cup coconut aminos',
      '2 tbsp olive oil',
      'Ginger and garlic to taste',
    ],
    instructions: [
      'Cook chicken in olive oil until golden',
      'Add vegetables and stir-fry',
      'Season with coconut aminos, ginger, and garlic',
      'Serve hot',
    ],
    image_url: 'https://example.com/stirfry.jpg',
    is_dairy_free: true,
    is_egg_free: true,
    is_soy_free: true,
    is_gluten_free: true,
    is_nut_free: true,
    is_fpies_friendly: true,
    protein_type: 'chicken',
    cook_time: 30,
    servings: 4,
    date_added: new Date().toISOString(),
    fpies_triggers: [],
    fpies_safe_substitutes: {},
    allergens: [],
    times_made: 0,
  },
];

// Simulate API delay
const delay = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

// Mock API functions
export const mockApi = {
  recipes: mockRecipes,

  async searchRecipes(query: string, filters: RecipeFilters): Promise<Recipe[]> {
    await delay(500); // Simulate network delay

    return mockRecipes.filter((recipe) => {
      const matchesQuery = recipe.title.toLowerCase().includes(query.toLowerCase());
      const matchesFilters =
        (!filters.is_dairy_free || recipe.is_dairy_free) &&
        (!filters.is_egg_free || recipe.is_egg_free) &&
        (!filters.is_soy_free || recipe.is_soy_free) &&
        (!filters.protein_type || recipe.protein_type === filters.protein_type) &&
        (!filters.meal_type || recipe.meal_type === filters.meal_type) &&
        (!filters.cooking_method || recipe.cooking_method === filters.cooking_method) &&
        (!filters.is_fpies_friendly || recipe.is_fpies_friendly);
      return matchesQuery && matchesFilters;
    });
  },

  async getRecipe(id: string): Promise<Recipe> {
    await delay(300);
    const recipe = mockRecipes.find((r) => r.id === parseInt(id, 10));
    if (!recipe) {
      throw new Error('Recipe not found');
    }
    return recipe;
  },

  async favorite(id: number): Promise<Recipe> {
    await delay(300);
    const recipe = mockRecipes.find((r) => r.id === id);
    if (!recipe) {
      throw new Error('Recipe not found');
    }
    return recipe;
  },

  async share(id: number): Promise<{ url: string }> {
    await delay(300);
    return { url: `https://example.com/recipes/${id}` };
  },
};
