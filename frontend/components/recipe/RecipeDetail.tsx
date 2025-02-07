import React, { type JSX } from 'react';

import {
  Heading,
  Image,
  ListItem,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalHeader,
  ModalOverlay,
  OrderedList,
  UnorderedList,
  VStack,
} from '@chakra-ui/react';

import { RecipeActions } from './RecipeActions';
import { RecipeAllergenBadges } from './RecipeAllergenBadges';
import { RecipeMetadata } from './RecipeMetadata';

import type { Recipe } from '../../types/recipe';

interface Props {
  /**
   * The recipe object containing details about the recipe.
   */
  recipe: Recipe;

  /**
   * Callback function that is invoked to close the recipe detail view.
   * @returns {void}
   */
  onClose: () => void;
}

/**
 * A React component that displays a recipe's details in a modal.
 *
 * @param {Props} props - The component props.
 * @param {Recipe} props.recipe - The recipe object containing details about the recipe.
 * @param {() => void} props.onClose - The callback function that is invoked to close the recipe detail view.
 * @returns {JSX.Element} - The rendered component.
 */
export const RecipeDetail: React.FC<Props> = ({
  recipe,
  onClose,
}: Props): JSX.Element => {
  return (
    <Modal isOpen onClose={onClose} size="xl">
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>
          {recipe.title}
          <ModalCloseButton />
        </ModalHeader>
        <ModalBody>
          <VStack align="stretch" spacing={4}>
            {recipe.image_url && (
              <Image
                src={recipe.image_url}
                alt={recipe.title}
                borderRadius="lg"
                objectFit="cover"
                height={256}
              />
            )}

            <RecipeActions
              recipeId={recipe.id}
              isFavorite={Boolean(recipe.favorite)}
            />
            <RecipeMetadata recipe={recipe} />
            <RecipeAllergenBadges recipe={recipe} />

            {/* Ingredients */}
            <VStack align="stretch">
              <Heading as="h3" size="lg" mb={2}>
                Ingredients
              </Heading>
              <UnorderedList listStyleType="disc">
                {recipe.ingredients.map((ingredient: string) => (
                  <ListItem key={ingredient}>{ingredient}</ListItem>
                ))}
              </UnorderedList>
            </VStack>

            {/* Instructions */}
            <VStack align="stretch">
              <Heading as="h3" size="lg" mb={2}>
                Instructions
              </Heading>
              <OrderedList listStyleType="decimal">
                {recipe.instructions.map((instruction: string) => (
                  <ListItem key={instruction}>{instruction}</ListItem>
                ))}
              </OrderedList>
            </VStack>
          </VStack>
        </ModalBody>
      </ModalContent>
    </Modal>
  );
};
