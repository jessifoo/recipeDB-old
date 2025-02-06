import { RecipeCard } from '../../components/recipe/RecipeCard';
import { render, screen } from '@testing-library/react';
import type { Recipe } from '../../types/recipe';

const mockRecipe: Recipe = {
  id: 1,
  title: 'Test Recipe',
  description: 'A delicious test recipe',
  ingredients: ['ingredient 1', 'ingredient 2'],
  instructions: ['step 1', 'step 2'],
  meal_type: 'dinner',
  is_collection: false,
  date_added: new Date().toISOString(),
  is_dairy_free: false,
  is_gluten_free: false,
  is_soy_free: false,
  is_nut_free: false,
  is_egg_free: false,
  is_fpies_friendly: false,
  fpies_triggers: [],
  fpies_safe_substitutes: {},
  allergens: [],
  times_made: 0,
  cooking_method: 'stovetop',
  protein_type: 'other',
  prep_time: 15,
  cook_time: 30,
  servings: 4,
  image_url: 'test.jpg',
  image_preview_url: 'test.jpg'
};

describe('RecipeCard', () => {
  it('renders recipe details correctly', () => {
    render(<RecipeCard recipe={mockRecipe} />);

    // Check basic recipe info
    expect(screen.getByText(mockRecipe.title)).toBeInTheDocument();
    expect(screen.getByText(mockRecipe.description)).toBeInTheDocument();
    expect(screen.getByText((content) => content.includes(mockRecipe.meal_type))).toBeInTheDocument();
    expect(screen.getByText((content) => content.includes('Stovetop'))).toBeInTheDocument();

    // Check cooking times
    expect(screen.getByText(/Prep: 15/)).toBeInTheDocument();
    expect(screen.getByText(/Cook: 30/)).toBeInTheDocument();
  });

  it('handles click events', () => {
    const handleClick = jest.fn();
    render(<RecipeCard recipe={mockRecipe} onClick={handleClick} />);

    const card = screen.getByRole('article');
    card.click();

    expect(handleClick).toHaveBeenCalled();
  });
});
