import { useRecipeSearch } from '@/hooks/api/useRecipeSearch';
import {
  Box,
  Button,
  Collapse,
  FormControl,
  FormLabel,
  Grid,
  HStack,
  IconButton,
  Input,
  NumberInput,
  NumberInputField,
  Select,
  Stack,
  useDisclosure,
} from '@chakra-ui/react';
import { useEffect, useState } from 'react';
import { FaFilter } from 'react-icons/fa';

const cuisineOptions = [
  'Italian',
  'Mexican',
  'Chinese',
  'Indian',
  'Japanese',
  'Thai',
  'Mediterranean',
  'American',
  'French',
  'Greek',
];

const dietOptions = [
  'Vegetarian',
  'Vegan',
  'Gluten-Free',
  'Dairy-Free',
  'Keto',
  'Paleo',
  'Low-Carb',
];

interface RecipeSearchProps {
  onSearch: (results: any) => void;
}

export default function RecipeSearch({ onSearch }: RecipeSearchProps) {
  const [query, setQuery] = useState('');
  const [cuisine, setCuisine] = useState<string>('');
  const [diet, setDiet] = useState<string>('');
  const [maxTime, setMaxTime] = useState<number | ''>('');
  const { isOpen, onToggle } = useDisclosure();

  const { data, isLoading, refetch } = useRecipeSearch(
    query,
    {
      cuisine_type: cuisine || undefined,
      diet: diet || undefined,
      max_cooking_time: maxTime || undefined,
    },
    1,
    20,
    false
  );

  useEffect(() => {
    if (data) {
      onSearch(data);
    }
  }, [data, onSearch]);

  const handleSearch = () => {
    if (query.trim()) {
      refetch();
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  const handleClear = () => {
    setQuery('');
    setCuisine('');
    setDiet('');
    setMaxTime('');
  };

  return (
    <Stack spacing={4} width="100%">
      <HStack>
        <FormControl>
          <Input
            placeholder="Search recipes..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyPress={handleKeyPress}
            variant="filled"
            size="lg"
          />
        </FormControl>
        <IconButton
          aria-label="Toggle filters"
          icon={<FaFilter />}
          variant="filter"
          size="lg"
          onClick={onToggle}
        />
        <Button
          onClick={handleSearch}
          isLoading={isLoading}
          size="lg"
          colorScheme="blue"
          variant="solid"
        >
          Search
        </Button>
      </HStack>

      <Collapse in={isOpen}>
        <Box layerStyle="form">
          <Grid variant="filters">
            <FormControl>
              <FormLabel>Cuisine Type</FormLabel>
              <Select
                placeholder="Select cuisine"
                value={cuisine}
                onChange={(e) => setCuisine(e.target.value)}
                variant="filled"
              >
                {cuisineOptions.map((option) => (
                  <option key={option} value={option.toLowerCase()}>
                    {option}
                  </option>
                ))}
              </Select>
            </FormControl>

            <FormControl>
              <FormLabel>Dietary Restriction</FormLabel>
              <Select
                placeholder="Select diet"
                value={diet}
                onChange={(e) => setDiet(e.target.value)}
                variant="filled"
              >
                {dietOptions.map((option) => (
                  <option key={option} value={option.toLowerCase()}>
                    {option}
                  </option>
                ))}
              </Select>
            </FormControl>

            <FormControl>
              <FormLabel>Max Cooking Time (minutes)</FormLabel>
              <NumberInput
                value={maxTime}
                onChange={(_, value) => setMaxTime(value)}
                min={0}
                variant="filled"
              >
                <NumberInputField placeholder="Enter time" />
              </NumberInput>
            </FormControl>
          </Grid>

          <Button
            onClick={handleClear}
            mt={4}
            variant="filter"
            size="md"
            width="auto"
          >
            Clear Filters
          </Button>
        </Box>
      </Collapse>
    </Stack>
  );
}
