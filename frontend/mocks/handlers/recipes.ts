import { http, HttpResponse } from 'msw';
import { mockRecipes } from '../data/recipes';

export const recipeHandlers = [
  // Search recipes
  http.get('/api/recipe-search', ({ request }) => {
    const url = new URL(request.url);
    const query = url.searchParams.get('query')?.toLowerCase() || '';
    const cuisine = url.searchParams.get('cuisine_type')?.toLowerCase();
    const diet = url.searchParams.get('diet')?.toLowerCase();
    const maxTime = url.searchParams.get('max_cooking_time');

    let filteredRecipes = mockRecipes;

    // Apply filters
    if (query) {
      filteredRecipes = filteredRecipes.filter(
        (recipe) =>
          recipe.title.toLowerCase().includes(query) ||
          recipe.description?.toLowerCase().includes(query)
      );
    }

    if (cuisine) {
      filteredRecipes = filteredRecipes.filter(
        (recipe) => recipe.cuisine?.toLowerCase() === cuisine
      );
    }

    if (diet) {
      filteredRecipes = filteredRecipes.filter((recipe) =>
        recipe.diet?.includes(diet)
      );
    }

    if (maxTime) {
      const maxMinutes = parseInt(maxTime);
      filteredRecipes = filteredRecipes.filter(
        (recipe) => recipe.total_time && recipe.total_time <= maxMinutes
      );
    }

    return HttpResponse.json({
      total: filteredRecipes.length,
      results: filteredRecipes,
      source: 'mock',
    });
  }),

  // Get recipe by ID
  http.get('/api/recipes/:id', ({ params }) => {
    const recipe = mockRecipes.find((r) => r.id === params.id);

    if (!recipe) {
      return new HttpResponse(null, { status: 404 });
    }

    return HttpResponse.json(recipe);
  }),
];
