import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import RecipeList from '../components/RecipeList';

// Mock fetch
global.fetch = jest.fn();

const mockRecipes = [
  {
    id: 1,
    title: 'Dairy-Free Chicken Curry',
    meal_type: 'dinner',
    is_collection: false,
    source_url: 'https://example.com',
    image_url: 'https://example.com/image.jpg',
    image_preview_url: 'https://example.com/preview.jpg',
    ingredients: [],
    instructions: [],
    prep_time: 10,
    cook_time: 30,
    cooking_method: 'stovetop',
    date_added: '2025-01-28T14:30:41-07:00',
    is_dairy_free: true,
    is_soy_free: false,
    is_gluten_free: false,
    is_nut_free: false,
    is_egg_free: false,
  },
  {
    id: 2,
    title: 'Gluten-Free Collection',
    meal_type: 'collection',
    is_collection: true,
    source_url: 'https://example.com',
    ingredients: [],
    instructions: [],
    date_added: '2025-01-28T14:30:41-07:00',
    is_dairy_free: false,
    is_soy_free: false,
    is_gluten_free: true,
    is_nut_free: false,
    is_egg_free: false,
  },
];

describe('RecipeList', () => {
  beforeEach(() => {
    (global.fetch as jest.Mock).mockReset();
  });

  it('renders recipe cards with correct information', async () => {
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockRecipes,
    });

    render(<RecipeList />);

    // Wait for recipes to load
    await waitFor(() => {
      expect(screen.getByText('Dairy-Free Chicken Curry')).toBeInTheDocument();
    });

    // Check if recipe details are displayed
    expect(screen.getAllByText('Dinner')).toHaveLength(2);
    expect(screen.getByText('Stovetop')).toBeInTheDocument();
    expect(screen.getAllByText('Dairy Free')).toHaveLength(2);
    expect(screen.getByText('Prep: 10m | Cook: 30m')).toBeInTheDocument();

    // Check if collection is displayed
    expect(screen.getByText('Gluten-Free Collection')).toBeInTheDocument();
    expect(screen.getAllByText('Gluten Free')).toHaveLength(2);
  });

  it('applies filters correctly', async () => {
    const mockFetch = global.fetch as jest.Mock;
    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockRecipes,
    });

    render(<RecipeList />);

    // Wait for initial load
    await waitFor(() => {
      expect(screen.getByText('Dairy-Free Chicken Curry')).toBeInTheDocument();
    });

    // Apply meal type filter
    const mealTypeSelect = screen.getByLabelText('Meal Type');
    await userEvent.selectOptions(mealTypeSelect, 'dinner');

    // Check if fetch was called with correct params
    await waitFor(() => {
      expect(mockFetch).toHaveBeenCalledWith(expect.stringContaining('meal_type=dinner'));
    });

    // Apply allergen filter
    const dairyFreeCheckbox = screen.getByLabelText('Dairy Free');
    fireEvent.click(dairyFreeCheckbox);

    await waitFor(() => {
      expect(mockFetch).toHaveBeenCalledWith(expect.stringContaining('allergens=dairy'));
    });

    // Apply search query
    const searchInput = screen.getByLabelText('Search Recipes');
    await userEvent.type(searchInput, 'curry');

    await waitFor(() => {
      expect(mockFetch).toHaveBeenCalledWith(expect.stringContaining('q=curry'));
    });
  });

  it('handles empty state', async () => {
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => [],
    });

    render(<RecipeList />);

    // Wait for loading to finish
    await waitFor(() => {
      expect(screen.queryByRole('progressbar')).not.toBeInTheDocument();
    });

    // Verify no recipe cards are shown
    expect(screen.queryByRole('img')).not.toBeInTheDocument();
  });

  it('handles fetch errors gracefully', async () => {
    const consoleError = jest.spyOn(console, 'error').mockImplementation(() => {});
    (global.fetch as jest.Mock).mockRejectedValueOnce(new Error('Failed to fetch'));

    render(<RecipeList />);

    await waitFor(() => {
      expect(consoleError).toHaveBeenCalledWith('Error fetching recipes:', expect.any(Error));
    });

    consoleError.mockRestore();
  });
});
