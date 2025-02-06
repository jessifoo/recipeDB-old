import { render, screen, waitFor } from '@testing-library/react';
import { RecipeSearch } from '../components/recipe/RecipeSearch';
import { useRecipeStore } from '../stores/recipeStore';
import { useFamilyProfileStore } from '../stores/familyProfileStore';
import * as mockStores from './mocks/mockStores';
import userEvent from '@testing-library/user-event';

// Mock the stores
jest.mock('../stores/recipeStore');
jest.mock('../stores/familyProfileStore');

const mockUseRecipeStore = useRecipeStore as jest.MockedFunction<typeof useRecipeStore>;
const mockUseFamilyProfileStore = useFamilyProfileStore as jest.MockedFunction<typeof useFamilyProfileStore>;

describe('RecipeSearch Component', () => {
  const mockSearchRecipes = jest.fn().mockResolvedValue(undefined);
  const mockToggleFavorite = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
    jest.useFakeTimers();

    // Mock store implementations
    mockUseRecipeStore.mockReturnValue(
      mockStores.createMockRecipeStore({
        searchRecipes: mockSearchRecipes,
        toggleFavorite: mockToggleFavorite,
      })
    );

    mockUseFamilyProfileStore.mockReturnValue(mockStores.mockFamilyProfile);
  });

  afterEach(() => {
    jest.useRealTimers();
  });

  describe('Search Functionality', () => {
    it('should debounce search requests by 300ms', async () => {
      render(<RecipeSearch />);
      const searchInput = screen.getByPlaceholderText(/search for recipes/i);

      // Type search query
      await userEvent.type(searchInput, 'test recipe');

      // Fast-forward timers
      jest.advanceTimersByTime(200);
      expect(mockSearchRecipes).not.toHaveBeenCalled();

      jest.advanceTimersByTime(100);
      await waitFor(() => {
        expect(mockSearchRecipes).toHaveBeenCalledWith(
          'test recipe',
          expect.any(Object)
        );
      });
    });
  });

  describe('Filter Functionality', () => {
    it('should apply family profile allergen filters automatically', async () => {
      mockUseRecipeStore.mockReturnValue(
        mockStores.createMockRecipeStore({
          searchRecipes: mockSearchRecipes,
          filters: {
            isDairyFree: false,
            isEggFree: false,
            isSoyFree: false
          }
        })
      );

      mockUseFamilyProfileStore.mockReturnValue({
        profile: {
          isDairyFree: true,
          isEggFree: false,
          isSoyFree: true
        }
      });

      render(<RecipeSearch />);
      const searchInput = screen.getByPlaceholderText(/search for recipes/i);

      await userEvent.type(searchInput, 'test');
      jest.advanceTimersByTime(300);

      expect(mockSearchRecipes).toHaveBeenCalledWith('test', {
        isDairyFree: true,
        isEggFree: false,
        isSoyFree: true
      });
    });

    it('should toggle filters when filter buttons are clicked', async () => {
      const setFilters = jest.fn();
      mockUseRecipeStore.mockReturnValue(
        mockStores.createMockRecipeStore({
          searchRecipes: mockSearchRecipes,
          setFilters,
          filters: {
            isDairyFree: false,
            isEggFree: false,
            isSoyFree: false
          }
        })
      );

      render(<RecipeSearch />);

      const dairyFreeButton = screen.getByRole('button', { name: /dairy free/i });
      await userEvent.click(dairyFreeButton);

      expect(setFilters).toHaveBeenCalledWith({
        isDairyFree: true,
        isEggFree: false,
        isSoyFree: false
      });
    });
  });

  describe('Loading and Error States', () => {
    it('should display loading spinner when searching', () => {
      mockUseRecipeStore.mockReturnValue(
        mockStores.createMockRecipeStore({
          searchRecipes: mockSearchRecipes,
          loading: true,
          recipes: []
        })
      );

      render(<RecipeSearch />);

      expect(screen.getByRole('status')).toBeInTheDocument();
      expect(screen.getByPlaceholderText(/search for recipes/i)).toBeDisabled();
    });

    it('should display error message when search fails', () => {
      const testErrorMessage = 'Failed to fetch recipes';

      mockUseRecipeStore.mockReturnValue(
        mockStores.createMockRecipeStore({
          searchRecipes: mockSearchRecipes,
          error: testErrorMessage
        })
      );

      render(<RecipeSearch />);
      expect(screen.getByText(testErrorMessage)).toBeInTheDocument();
    });
  });
});
