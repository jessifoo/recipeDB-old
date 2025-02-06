import type { ChangeEvent, FC } from 'react';

import { Search2Icon } from '@chakra-ui/icons';
import {
  Box,
  Card,
  CardBody,
  Checkbox,
  CheckboxGroup,
  FormControl,
  FormLabel,
  Heading,
  HStack,
  Input,
  InputGroup,
  InputLeftElement,
  Select,
  Stack,
  Text,
  useStyleConfig,
  VStack,
} from '@chakra-ui/react';

import type {
  CookingMethod,
  MealType,
  RecipeFilters,
} from '../../types/recipe';

interface Props {
  filters: RecipeFilters;
  onFilterChange: (key: keyof RecipeFilters, value: string | boolean) => void;
}

const mealTypes: MealType[] = [
  'breakfast',
  'lunch',
  'dinner',
  'dessert',
  'snack',
  'other',
];
const cookingMethods: CookingMethod[] = [
  'bake',
  'stovetop',
  'grill',
  'slow_cooker',
  'instant_pot',
  'air_fryer',
  'refrigerate',
  'freeze',
];

/**
 * RecipeFilterComponent component handles all filtering options for recipes
 * including search, meal type, cooking method, and dietary restrictions.
 */
export const RecipeFilterComponent: FC<Props> = ({
  filters,
  onFilterChange,
}) => {
  const styles = useStyleConfig('Recipe');

  return (
    <Card variant="elevated" shadow="md">
      <CardBody>
        <VStack spacing={6} align="stretch">
          <Box>
            <Heading size="md" mb={4}>
              Filters
            </Heading>
            <HStack spacing={4}>
              <InputGroup>
                <InputLeftElement pointerEvents="none">
                  <Search2Icon color="gray.400" />
                </InputLeftElement>
                <Input
                  value={filters.search_query ?? ''}
                  onChange={(e: ChangeEvent<HTMLInputElement>) =>
                    onFilterChange('search_query', e.target.value)
                  }
                  placeholder="Search recipes..."
                  variant="filled"
                  aria-label="Search recipes"
                />
              </InputGroup>
              <FormControl>
                <FormLabel htmlFor="meal-type" fontWeight="medium">
                  Meal Type
                </FormLabel>
                <Select
                  id="meal-type"
                  value={filters.meal_type ?? ''}
                  onChange={(e: ChangeEvent<HTMLSelectElement>) =>
                    onFilterChange('meal_type', e.target.value)
                  }
                  placeholder="Select meal type"
                  variant="filled"
                >
                  <option value="">All</option>
                  {mealTypes.map((type) => (
                    <option key={type} value={type}>
                      {type.charAt(0).toUpperCase() + type.slice(1)}
                    </option>
                  ))}
                </Select>
              </FormControl>
              <FormControl>
                <FormLabel htmlFor="cooking-method" fontWeight="medium">
                  Cooking Method
                </FormLabel>
                <Select
                  id="cooking-method"
                  value={filters.cooking_method ?? ''}
                  onChange={(e: ChangeEvent<HTMLSelectElement>) =>
                    onFilterChange('cooking_method', e.target.value)
                  }
                  placeholder="Select cooking method"
                  variant="filled"
                >
                  <option value="">All</option>
                  {cookingMethods.map((method) => (
                    <option key={method} value={method}>
                      {method
                        .split('_')
                        .map(
                          (word) => word.charAt(0).toUpperCase() + word.slice(1)
                        )
                        .join(' ')}
                    </option>
                  ))}
                </Select>
              </FormControl>
            </HStack>
          </Box>

          <Box>
            <Text fontWeight="medium" mb={3}>
              Dietary Restrictions
            </Text>
            <Stack spacing={3}>
              <CheckboxGroup>
                <VStack align="start" spacing={2}>
                  {[
                    { key: 'is_dairy_free', label: 'Dairy Free' },
                    { key: 'is_soy_free', label: 'Soy Free' },
                    { key: 'is_gluten_free', label: 'Gluten Free' },
                    { key: 'is_nut_free', label: 'Nut Free' },
                    { key: 'is_egg_free', label: 'Egg Free' },
                    { key: 'is_fpies_friendly', label: 'FPIES Friendly' },
                  ].map(({ key, label }) => (
                    <Checkbox
                      key={key}
                      isChecked={filters[key as keyof RecipeFilters] ?? false}
                      onChange={(e: ChangeEvent<HTMLInputElement>) =>
                        onFilterChange(
                          key as keyof RecipeFilters,
                          e.target.checked
                        )
                      }
                      colorScheme="green"
                    >
                      {label}
                    </Checkbox>
                  ))}
                  <Checkbox
                    isChecked={filters.is_collection ?? false}
                    onChange={(e: ChangeEvent<HTMLInputElement>) =>
                      onFilterChange('is_collection', e.target.checked)
                    }
                    colorScheme="purple"
                  >
                    Collections Only
                  </Checkbox>
                </VStack>
              </CheckboxGroup>
            </Stack>
          </Box>
        </VStack>
      </CardBody>
    </Card>
  );
};
