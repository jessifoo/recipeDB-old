import { useFamilyProfile } from '@/stores/familyProfileStore';
import { useRecipes } from './useRecipes';

export function useFilteredRecipes(options?: {
  activeProfileId?: string;
  includeSubstitutions?: boolean;
}) {
  const { data: recipesData, ...queryInfo } = useRecipes();
  const { members } = useFamilyProfile();

  const activeProfile = options?.activeProfileId
    ? members.find((m) => m.id === options.activeProfileId)
    : null;

  const recipes = recipesData?.data || [];

  const filteredAndAnnotatedRecipes = recipes.map((recipe) => {
    const warnings: string[] = [];
    const substitutions: Record<string, string[]> = {};

    if (activeProfile) {
      // Check for allergens
      activeProfile.allergies.forEach((allergy) => {
        if (recipe.allergens?.includes(allergy)) {
          warnings.push(`Contains ${allergy}`);
        }
      });

      // Check for FPIES triggers
      activeProfile.fpiesTriggers.forEach((trigger) => {
        if (recipe.fpies_triggers?.includes(trigger)) {
          warnings.push(`FPIES Trigger: ${trigger}`);
        }

        // Add known safe substitutions
        if (options?.includeSubstitutions && activeProfile.safeSubstitutes[trigger]) {
          substitutions[trigger] = activeProfile.safeSubstitutes[trigger];
        }
      });
    }

    return {
      ...recipe,
      warnings,
      substitutions,
      isSafe: warnings.length === 0,
    };
  });

  // Sort recipes: safe ones first, then ones with substitutions, then others
  const sortedRecipes = filteredAndAnnotatedRecipes.sort((a, b) => {
    if (a.isSafe && !b.isSafe) {
      return -1;
    }
    if (!a.isSafe && b.isSafe) {
      return 1;
    }
    if (Object.keys(a.substitutions).length > Object.keys(b.substitutions).length) {
      return -1;
    }
    if (Object.keys(a.substitutions).length < Object.keys(b.substitutions).length) {
      return 1;
    }
    return 0;
  });

  return {
    ...queryInfo,
    data: sortedRecipes,
    safeRecipes: sortedRecipes.filter((r) => r.isSafe),
    recipesWithSubstitutions: sortedRecipes.filter((r) => Object.keys(r.substitutions).length > 0),
    unsafeRecipes: sortedRecipes.filter(
      (r) => !r.isSafe && Object.keys(r.substitutions).length === 0
    ),
  };
}
