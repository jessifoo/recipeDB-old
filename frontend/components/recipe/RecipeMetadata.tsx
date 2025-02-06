import { HStack, Text } from '@chakra-ui/react';

import type { Recipe } from '../../types/recipe';

interface Props {
  recipe: Pick<Recipe, 'prep_time' | 'cook_time' | 'servings'>;
  showServings?: boolean;
}

export const RecipeMetadata: React.FC<Props> = ({
  recipe,
  showServings = true,
}) => {
  const { prep_time, cook_time, servings } = recipe;

  return (
    <HStack spacing={4}>
      {(prep_time > 0 || cook_time > 0) && (
        <HStack>
          {prep_time > 0 && <Text>Prep: {prep_time}m</Text>}
          {prep_time > 0 && cook_time > 0 && <Text>•</Text>}
          {cook_time > 0 && <Text>Cook: {cook_time}m</Text>}
        </HStack>
      )}
      {showServings && servings > 0 && (
        <HStack>
          <Text>{servings} servings</Text>
        </HStack>
      )}
    </HStack>
  );
};
