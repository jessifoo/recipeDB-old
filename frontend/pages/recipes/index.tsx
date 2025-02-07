import { PageLayout } from '@/components/layout/PageLayout';
import { RecipeGrid } from '@/components/recipe/RecipeGrid';
import type { Recipe } from '@/types/recipe';

export default function RecipesPage() {
  // Example recipes for testing
  const recipes: Recipe[] = [
    {
      id: 1,
      title: 'Spaghetti Carbonara',
      description: 'Classic Italian pasta dish with eggs and pancetta',
      image_url: 'https://example.com/carbonara.jpg',
      meal_type: 'dinner',
      cooking_method: 'stovetop_cooking',
      prep_time: 15,
      cook_time: 20,
      is_dairy_free: false,
      is_gluten_free: false,
      is_nut_free: true,
      is_egg_free: false,
      is_soy_free: true,
    },
    {
      id: 2,
      title: 'Quinoa Buddha Bowl',
      description:
        'Healthy bowl with quinoa, roasted vegetables, and tahini dressing',
      image_url: 'https://example.com/buddha-bowl.jpg',
      meal_type: 'lunch',
      cooking_method: 'meal_prep',
      prep_time: 20,
      cook_time: 30,
      is_dairy_free: true,
      is_gluten_free: true,
      is_nut_free: false,
      is_egg_free: true,
      is_soy_free: true,
    },
  ];

  return (
    <PageLayout>
      <RecipeGrid
        recipes={recipes}
        onRecipeClick={(recipe) => console.log('Clicked recipe:', recipe.title)}
      />
    </PageLayout>
  );
}
