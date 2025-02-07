import type { Recipe } from '@/types/recipe';
import { http, HttpResponse } from 'msw';

const mockRecipes: Recipe[] = [
  {
    id: 1,
    title: 'Spaghetti Carbonara',
    description: 'Classic Italian pasta dish',
    ingredients: ['pasta', 'eggs', 'pecorino cheese', 'guanciale', 'black pepper'],
    instructions: ['Cook pasta', 'Mix eggs and cheese', 'Combine with hot pasta'],
    cookingTime: 30,
    servings: 4,
  },
  // Add more mock recipes as needed
];

export const handlers = [
  // List recipes
  http.get('*/api/recipes', () => {
    return HttpResponse.json({ data: mockRecipes });
  }),

  // Get single recipe
  http.get('*/api/recipes/:id', ({ params }) => {
    const { id } = params;
    const recipe = mockRecipes.find((r) => r.id === Number(id));

    if (!recipe) {
      return new HttpResponse(null, { status: 404 });
    }

    return HttpResponse.json({ data: recipe });
  }),

  // Create recipe
  http.post('*/api/recipes', async ({ request }) => {
    const newRecipe = await request.json();
    return HttpResponse.json({
      data: { ...newRecipe, id: (Math.random() * 1000) | 0 },
    });
  }),

  // Update recipe
  http.put('*/api/recipes/:id', async ({ params, request }) => {
    const { id } = params;
    const updates = await request.json();
    const recipe = mockRecipes.find((r) => r.id === Number(id));

    if (!recipe) {
      return new HttpResponse(null, { status: 404 });
    }

    return HttpResponse.json({
      data: { ...recipe, ...updates },
    });
  }),

  // Delete recipe
  http.delete('*/api/recipes/:id', ({ params }) => {
    const { id } = params;
    const recipe = mockRecipes.find((r) => r.id === Number(id));

    if (!recipe) {
      return new HttpResponse(null, { status: 404 });
    }

    return new HttpResponse(null, { status: 204 });
  }),
];
