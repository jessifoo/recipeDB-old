import { Badge, HStack } from '@chakra-ui/react';

import type { Recipe } from '../../types/recipe';

interface Props {
  recipe: Pick<
    Recipe,
    | 'is_dairy_free'
    | 'is_soy_free'
    | 'is_gluten_free'
    | 'is_nut_free'
    | 'is_egg_free'
  >;
}

export const RecipeAllergenBadges: React.FC<Props> = ({ recipe }) => {
  const {
    is_dairy_free,
    is_soy_free,
    is_gluten_free,
    is_nut_free,
    is_egg_free,
  } = recipe;

  return (
    <HStack spacing={2} wrap="wrap">
      {is_dairy_free && <Badge colorScheme="green">Dairy Free</Badge>}
      {is_soy_free && <Badge colorScheme="green">Soy Free</Badge>}
      {is_gluten_free && <Badge colorScheme="green">Gluten Free</Badge>}
      {is_nut_free && <Badge colorScheme="green">Nut Free</Badge>}
      {is_egg_free && <Badge colorScheme="green">Egg Free</Badge>}
    </HStack>
  );
};
