import type React from 'react';
import { useCallback, useState } from 'react';

import debounce from 'lodash/debounce';

import { useFamilyProfileStore } from '../../stores/familyProfileStore';
import { useRecipeStore } from '../../stores/recipeStore';

import type { SearchFilters } from '../../types';

export const RecipeSearch: React.FC = () => {
  const [query, setQuery] = useState('');
  const { profile } = useFamilyProfileStore();
  const { searchRecipes, recipes, loading, error, filters, setFilters } =
    useRecipeStore();

  // Debounced search function
  const debouncedSearch = useCallback(
    debounce((searchQuery: string, searchFilters: SearchFilters) => {
      searchRecipes(searchQuery, searchFilters);
    }, 300),
    []
  );

  // Handle search input
  const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newQuery = e.target.value;
    setQuery(newQuery);

    // Auto-apply family allergen filters
    const searchFilters: SearchFilters = {
      ...filters,
      isDairyFree: profile?.isDairyFree || false,
      isEggFree: profile?.isEggFree || false,
      isSoyFree: profile?.isSoyFree || false,
    };

    debouncedSearch(newQuery, searchFilters);
  };

  // Handle filter changes
  const handleFilterChange = (filterKey: keyof SearchFilters) => {
    const newFilters = {
      ...filters,
      [filterKey]: !filters[filterKey],
    };
    setFilters(newFilters);
  };

  return (
    <div className="space-y-4">
      {/* Search Input */}
      <div className="relative">
        <input
          type="text"
          value={query}
          onChange={handleSearch}
          placeholder="Search for recipes..."
          className="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
          disabled={loading}
        />
        {loading && (
          <div className="absolute right-3 top-2" role="status">
            <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-500" />
          </div>
        )}
      </div>

      {/* Filters */}
      <div className="flex flex-wrap gap-2">
        <button
          type="button"
          onClick={() => handleFilterChange('isDairyFree')}
          className={`px-3 py-1 rounded-full text-sm ${
            filters.isDairyFree
              ? 'bg-blue-500 text-white'
              : 'bg-gray-200 text-gray-700'
          }`}
        >
          Dairy Free
        </button>
        <button
          type="button"
          onClick={() => handleFilterChange('isEggFree')}
          className={`px-3 py-1 rounded-full text-sm ${
            filters.isEggFree
              ? 'bg-blue-500 text-white'
              : 'bg-gray-200 text-gray-700'
          }`}
        >
          Egg Free
        </button>
        <button
          type="button"
          onClick={() => handleFilterChange('isSoyFree')}
          className={`px-3 py-1 rounded-full text-sm ${
            filters.isSoyFree
              ? 'bg-blue-500 text-white'
              : 'bg-gray-200 text-gray-700'
          }`}
        >
          Soy Free
        </button>
      </div>

      {/* Error Message */}
      {error && (
        <div className="p-4 bg-red-100 text-red-700 rounded-lg">{error}</div>
      )}

      {/* Results */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {recipes.map((recipe) => (
          <div
            key={recipe.id}
            className="p-4 border rounded-lg hover:shadow-lg transition-shadow"
          >
            {recipe.image_url && (
              <img
                src={recipe.image_url}
                alt={recipe.title}
                className="w-full h-48 object-cover rounded-lg mb-2"
              />
            )}
            <h3 className="font-semibold text-lg">{recipe.title}</h3>
            <div className="flex flex-wrap gap-1 mt-2">
              {recipe.is_dairy_free && (
                <span className="px-2 py-1 bg-green-100 text-green-800 rounded-full text-xs">
                  Dairy Free
                </span>
              )}
              {recipe.is_egg_free && (
                <span className="px-2 py-1 bg-green-100 text-green-800 rounded-full text-xs">
                  Egg Free
                </span>
              )}
              {recipe.is_soy_free && (
                <span className="px-2 py-1 bg-green-100 text-green-800 rounded-full text-xs">
                  Soy Free
                </span>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* No Results */}
      {!loading && recipes.length === 0 && query && (
        <div className="text-center text-gray-500 py-8">
          No recipes found. Try adjusting your search or filters.
        </div>
      )}
    </div>
  );
};
