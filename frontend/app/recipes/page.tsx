import { RecipeSearch } from '@/components/RecipeSearch';
import { RecipeGrid } from '@/components/organisms/RecipeGrid';
import type { RecipeList } from '@/types/api';
import { Container, Heading, Stack } from '@chakra-ui/react';
import { useState } from 'react';

export default function RecipesPage() {
  const [searchResults, setSearchResults] = useState<RecipeList | null>(null);

  const handleSearchResults = (results: RecipeList) => {
    setSearchResults(results);
  };

  return (
    <Container maxW="container.xl" py={8}>
      <Stack spacing={8}>
        <Heading size="xl">Recipe Search</Heading>
        <RecipeSearch onSearch={handleSearchResults} />
        <RecipeGrid recipes={searchResults} />
      </Stack>
    </Container>
  );
}
