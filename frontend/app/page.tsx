'use client';

import { useState } from 'react';

import { RecipeCard } from '@/components/RecipeCard';
import { RecipeFilters } from '@/components/RecipeFilters';
import type { RecipeFilters as Filters, Recipe } from '@/types/recipe';

export default function Home() {
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [loading, setLoading] = useState(false);

  const handleFilterChange = async (filters: Filters) => {
    setLoading(true);
    try {
      const params = new URLSearchParams();
      if (filters.searchQuery) {
        params.append('q', filters.searchQuery);
      }
      if (filters.allergens?.length) {
        for (const allergen of filters.allergens) {
          params.append('allergens', allergen);
        }
      }

      const response = await fetch(`/api/recipes?${params.toString()}`);
      const data = await response.json();
      setRecipes(data);
    } catch (error) {
      console.error('Failed to fetch recipes:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleLike = async (recipeId: number) => {
    try {
      await fetch(`/api/recipes/${recipeId}/like`, {
        method: 'POST',
      });

      setRecipes((prev) =>
        prev.map((recipe) =>
          recipe.id === recipeId
            ? { ...recipe, isLiked: !recipe.isLiked }
            : recipe
        )
      );
    } catch (error) {
      console.error('Failed to like recipe:', error);
    }
  };

  return (
    <main className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold text-gray-900 mb-8">
        FPIES-Friendly Recipes
      </h1>

      <div className="mb-8">
        <RecipeFilters onFilterChange={handleFilterChange} />
      </div>

      {loading ? (
        <div className="text-center py-12">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900 mx-auto" />
          <p className="mt-4 text-gray-600">Loading recipes...</p>
        </div>
      ) : recipes.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {recipes.map((recipe) => (
            <RecipeCard key={recipe.id} recipe={recipe} onLike={handleLike} />
          ))}
        </div>
      ) : (
        <div className="text-center py-12">
          <p className="text-gray-600">
            No recipes found. Try adjusting your filters.
          </p>
        </div>
      )}
    </main>
  );
}
