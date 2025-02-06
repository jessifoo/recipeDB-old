import React, { useState } from 'react';

import { addDays, format, startOfWeek } from 'date-fns';

import { useMealPlanStore } from '../../stores/mealPlanStore';
import { useRecipeStore } from '../../stores/recipeStore';

import type { MealType, Recipe } from '../../types/recipe';

const MEAL_TYPES: MealType[] = ['breakfast', 'lunch', 'dinner', 'snack'];

export const MealPlanner: React.FC = () => {
  const { currentPlan, addMeal, removeMeal, createPlan, loading, error } =
    useMealPlanStore();
  const { recipes } = useRecipeStore();
  const [selectedRecipe, setSelectedRecipe] = useState<Recipe | null>(null);
  const [selectedDate, setSelectedDate] = useState<Date | null>(null);
  const [selectedMealType, setSelectedMealType] = useState<MealType>('dinner');

  // Initialize a week-long meal plan if none exists
  React.useEffect(() => {
    if (!currentPlan) {
      const start = startOfWeek(new Date());
      const end = addDays(start, 6);
      createPlan(start.toISOString(), end.toISOString());
    }
  }, [currentPlan, createPlan]);

  const handleAddMeal = () => {
    if (selectedRecipe && selectedDate) {
      addMeal({
        recipeId: selectedRecipe.id.toString(),
        date: selectedDate.toISOString(),
        mealType: selectedMealType,
        servings: 4,
      });
      setSelectedRecipe(null);
      setSelectedDate(null);
    }
  };

  const getDayMeals = (date: Date) => {
    if (!currentPlan) {
      return [];
    }
    return currentPlan.meals.filter(
      (meal) =>
        format(new Date(meal.date), 'yyyy-MM-dd') === format(date, 'yyyy-MM-dd')
    );
  };

  const renderWeek = () => {
    if (!currentPlan) {
      return null;
    }

    const start = new Date(currentPlan.startDate);
    const days = Array.from({ length: 7 }, (_, i) => addDays(start, i));

    return (
      <div className="grid grid-cols-7 gap-4">
        {days.map((day) => (
          <div
            key={day.toISOString()}
            className="border rounded-lg p-4 min-h-[200px]"
          >
            <div className="font-semibold mb-2">
              {format(day, 'EEEE')}
              <br />
              {format(day, 'MMM d')}
            </div>

            {MEAL_TYPES.map((mealType) => {
              const meals = getDayMeals(day).filter(
                (m) => m.mealType === mealType
              );
              if (meals.length === 0) {
                return null;
              }

              return (
                <div key={mealType} className="mb-2">
                  <div className="text-sm text-gray-600 capitalize">
                    {mealType}
                  </div>
                  {meals.map((meal) => {
                    const recipe = recipes.find(
                      (r) => r.id.toString() === meal.recipeId
                    );
                    if (!recipe) {
                      return null;
                    }

                    return (
                      <div
                        key={meal.id}
                        className="text-sm p-2 bg-blue-50 rounded mt-1 flex justify-between items-center"
                      >
                        <span>{recipe.title}</span>
                        <button
                          type="button"
                          onClick={() => removeMeal(meal.id)}
                          className="text-red-500 hover:text-red-700"
                        >
                          ×
                        </button>
                      </div>
                    );
                  })}
                </div>
              );
            })}

            <button
              type="button"
              onClick={() => {
                setSelectedDate(day);
                setSelectedMealType('dinner');
              }}
              className="mt-2 text-sm text-blue-500 hover:text-blue-700"
            >
              + Add Meal
            </button>
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold">Meal Planner</h2>

      {/* Add Meal Form */}
      {selectedDate && (
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="font-semibold mb-4">
            Add Meal for {format(selectedDate, 'EEEE, MMMM d')}
          </h3>

          <div className="space-y-4">
            <div>
              <label
                htmlFor="mealType"
                className="block text-sm font-medium mb-1"
              >
                Meal Type
              </label>
              <select
                id="mealType"
                value={selectedMealType}
                onChange={(e) =>
                  setSelectedMealType(e.target.value as MealType)
                }
                className="w-full p-2 border rounded"
              >
                {MEAL_TYPES.map((type) => (
                  <option key={type} value={type}>
                    {type.charAt(0).toUpperCase() + type.slice(1)}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label
                htmlFor="recipe"
                className="block text-sm font-medium mb-1"
              >
                Recipe
              </label>
              <select
                id="recipe"
                value={selectedRecipe?.id || ''}
                onChange={(e) => {
                  const recipe = recipes.find(
                    (r) => r.id.toString() === e.target.value
                  );
                  setSelectedRecipe(recipe || null);
                }}
                className="w-full p-2 border rounded"
              >
                <option value="">Select a recipe...</option>
                {recipes.map((recipe) => (
                  <option key={recipe.id} value={recipe.id}>
                    {recipe.title}
                  </option>
                ))}
              </select>
            </div>

            <div className="flex justify-end gap-2">
              <button
                type="button"
                onClick={() => setSelectedDate(null)}
                className="px-4 py-2 text-gray-600 hover:text-gray-800"
              >
                Cancel
              </button>
              <button
                type="button"
                onClick={handleAddMeal}
                disabled={!selectedRecipe}
                className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:opacity-50"
              >
                Add to Plan
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Error Message */}
      {error && (
        <div className="p-4 bg-red-100 text-red-700 rounded-lg">{error}</div>
      )}

      {/* Weekly Plan */}
      {loading ? (
        <div className="flex justify-center py-8">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500" />
        </div>
      ) : (
        renderWeek()
      )}
    </div>
  );
};
