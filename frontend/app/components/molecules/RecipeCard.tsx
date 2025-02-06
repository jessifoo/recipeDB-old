import type { RecipeSearchResult } from '@/types/api';
import {
  Card,
  CardBody,
  Heading,
  LinkBox,
  LinkOverlay,
} from '@chakra-ui/react';
import NextLink from 'next/link';
import { RecipeImage } from '../atoms/RecipeImage';
import { RecipeMetadata } from '../atoms/RecipeMetadata';

interface RecipeCardProps {
  recipe: RecipeSearchResult;
}

export function RecipeCard({ recipe }: RecipeCardProps) {
  return (
    <LinkBox
      as={Card}
      variant="outline"
      _hover={{ shadow: 'lg' }}
      transition="all 0.2s"
    >
      <RecipeImage imageUrl={recipe.image_url} title={recipe.title} />
      <CardBody>
        <LinkOverlay as={NextLink} href={`/recipes/${recipe.id}`}>
          <Heading size="md" mb={2} noOfLines={2}>
            {recipe.title}
          </Heading>
        </LinkOverlay>

        <RecipeMetadata
          cookingTime={recipe.total_time}
          servings={recipe.servings}
          cuisine={recipe.cuisine}
        />
      </CardBody>
    </LinkBox>
  );
}
