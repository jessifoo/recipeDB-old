import { create } from 'zustand';
import type { MealPlan, MealPlanItem } from '../types/recipe';

interface MealPlanStore {
  // State
  currentPlan: MealPlan | null;
  loading: boolean;
  error: string | null;

  // Actions
  createPlan: (startDate: string, endDate: string) => Promise<void>;
  addMeal: (meal: Omit<MealPlanItem, 'id'>) => Promise<void>;
  removeMeal: (mealId: string) => Promise<void>;
  updateMeal: (mealId: string, updates: Partial<MealPlanItem>) => Promise<void>;
  loadPlan: (planId: string) => Promise<void>;
  clearError: () => void;
}

export const useMealPlanStore = create<MealPlanStore>((set, get) => ({
  // Initial state
  currentPlan: null,
  loading: false,
  error: null,

  // Actions
  createPlan: async (startDate: string, endDate: string) => {
    try {
      set({ loading: true, error: null });

      // In development, use mock data
      if (process.env.NODE_ENV === 'development') {
        const plan: MealPlan = {
          id: Date.now().toString(),
          startDate,
          endDate,
          meals: [],
        };
        set({ currentPlan: plan, loading: false });
        return;
      }

      // TODO: Add API call for production
      throw new Error('Not implemented');
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to create meal plan',
        loading: false,
      });
    }
  },

  addMeal: async (meal: Omit<MealPlanItem, 'id'>) => {
    try {
      set({ loading: true, error: null });
      const { currentPlan } = get();

      if (!currentPlan) {
        throw new Error('No active meal plan');
      }

      const newMeal: MealPlanItem = {
        ...meal,
        id: Date.now().toString(),
      };

      // In development, update local state
      if (process.env.NODE_ENV === 'development') {
        set({
          currentPlan: {
            ...currentPlan,
            meals: [...currentPlan.meals, newMeal],
          },
          loading: false,
        });
        return;
      }

      // TODO: Add API call for production
      throw new Error('Not implemented');
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to add meal',
        loading: false,
      });
    }
  },

  removeMeal: async (mealId: string) => {
    try {
      set({ loading: true, error: null });
      const { currentPlan } = get();

      if (!currentPlan) {
        throw new Error('No active meal plan');
      }

      // In development, update local state
      if (process.env.NODE_ENV === 'development') {
        set({
          currentPlan: {
            ...currentPlan,
            meals: currentPlan.meals.filter((meal) => meal.id !== mealId),
          },
          loading: false,
        });
        return;
      }

      // TODO: Add API call for production
      throw new Error('Not implemented');
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to remove meal',
        loading: false,
      });
    }
  },

  updateMeal: async (mealId: string, updates: Partial<MealPlanItem>) => {
    try {
      set({ loading: true, error: null });
      const { currentPlan } = get();

      if (!currentPlan) {
        throw new Error('No active meal plan');
      }

      // In development, update local state
      if (process.env.NODE_ENV === 'development') {
        set({
          currentPlan: {
            ...currentPlan,
            meals: currentPlan.meals.map((meal) =>
              meal.id === mealId ? { ...meal, ...updates } : meal
            ),
          },
          loading: false,
        });
        return;
      }

      // TODO: Add API call for production
      throw new Error('Not implemented');
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to update meal',
        loading: false,
      });
    }
  },

  loadPlan: async (planId: string) => {
    try {
      set({ loading: true, error: null });

      // In development, create mock plan
      if (process.env.NODE_ENV === 'development') {
        const plan: MealPlan = {
          id: planId,
          startDate: new Date().toISOString(),
          endDate: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString(),
          meals: [],
        };
        set({ currentPlan: plan, loading: false });
        return;
      }

      // TODO: Add API call for production
      throw new Error('Not implemented');
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Failed to load meal plan',
        loading: false,
      });
    }
  },

  clearError: () => {
    set({ error: null });
  },
}));
