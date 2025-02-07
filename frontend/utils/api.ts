import type { Recipe, RecipeFilters } from '@/types/recipe';
import axios, { type AxiosResponse, isAxiosError } from 'axios';
import { mockApi } from '../mocks/recipeData';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface ApiResponse<T> {
  success: boolean;
  data: T;
  error?: string;
}

interface DeleteResponse {
  success: boolean;
  message?: string;
}

interface ApiError {
  error: string;
  message?: string;
}

async function handleResponse<T>(response: AxiosResponse<T>): Promise<ApiResponse<T>> {
  if (!response.data) {
    throw new Error('No data received from server');
  }

  return {
    success: true,
    data: response.data,
  };
}

function handleError(error: unknown): ApiError {
  if (isAxiosError(error)) {
    return {
      error: error.response?.data?.error || error.message,
      message: error.response?.data?.message || 'An error occurred while processing your request'
    };
  }
  return {
    error: error instanceof Error ? error.message : 'Unknown error occurred',
    message: 'An unexpected error occurred'
  };
}

export const api = {
  recipes: {
    async list(params?: { page?: number; limit?: number }): Promise<ApiResponse<Recipe[]>> {
      try {
        const searchParams = new URLSearchParams();
        if (params?.page) {
          searchParams.append('page', params.page.toString());
        }
        if (params?.limit) {
          searchParams.append('limit', params.limit.toString());
        }

        const response = await axios.get<Recipe[]>(`${API_BASE_URL}/api/recipes`, {
          params: searchParams,
        });

        return handleResponse<Recipe[]>(response);
      } catch (error) {
        if (process.env.NODE_ENV === 'development') {
          console.warn('Using mock data in development');
          return { success: true, data: mockApi.recipes };
        }
        throw handleError(error);
      }
    },

    async search(query: string, filters?: RecipeFilters): Promise<ApiResponse<Recipe[]>> {
      try {
        const response = await axios.get<Recipe[]>(`${API_BASE_URL}/api/recipes/search`, {
          params: {
            query,
            ...filters,
          },
        });
        return handleResponse<Recipe[]>(response);
      } catch (error) {
        if (process.env.NODE_ENV === 'development') {
          console.warn('Using mock data in development');
          const mockRecipes = await mockApi.searchRecipes(query, filters);
          return { success: true, data: mockRecipes };
        }
        throw handleError(error);
      }
    },

    async get(id: number): Promise<ApiResponse<Recipe>> {
      try {
        const response = await axios.get<Recipe>(`${API_BASE_URL}/api/recipes/${id}`);
        return handleResponse<Recipe>(response);
      } catch (error) {
        if (process.env.NODE_ENV === 'development') {
          console.warn('Using mock data in development');
          const mockRecipe = await mockApi.getRecipe(id.toString());
          return { success: true, data: mockRecipe };
        }
        throw handleError(error);
      }
    },

    async create(recipe: Omit<Recipe, 'id'>): Promise<ApiResponse<Recipe>> {
      try {
        const response = await axios.post<Recipe>(`${API_BASE_URL}/api/recipes`, recipe);
        return handleResponse<Recipe>(response);
      } catch (error) {
        throw handleError(error);
      }
    },

    async update(id: number, recipe: Partial<Recipe>): Promise<ApiResponse<Recipe>> {
      try {
        const response = await axios.put<Recipe>(`${API_BASE_URL}/api/recipes/${id}`, recipe);
        return handleResponse<Recipe>(response);
      } catch (error) {
        throw handleError(error);
      }
    },

    async delete(id: number): Promise<ApiResponse<DeleteResponse>> {
      try {
        const response = await axios.delete<DeleteResponse>(`${API_BASE_URL}/api/recipes/${id}`);
        return handleResponse<DeleteResponse>(response);
      } catch (error) {
        throw handleError(error);
      }
    },

    async favorite(id: number): Promise<ApiResponse<Recipe>> {
      try {
        const response = await axios.post<Recipe>(`${API_BASE_URL}/api/recipes/${id}/favorite`);
        return handleResponse<Recipe>(response);
      } catch (error) {
        throw handleError(error);
      }
    },

    async share(id: number): Promise<ApiResponse<{ url: string }>> {
      try {
        const response = await axios.post<{ url: string }>(`${API_BASE_URL}/api/recipes/${id}/share`);
        return handleResponse<{ url: string }>(response);
      } catch (error) {
        throw handleError(error);
      }
    },
  },
};
