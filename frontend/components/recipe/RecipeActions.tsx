import React from 'react';

import { Button, HStack, Tooltip, Box, Text, useToast } from '@chakra-ui/react';
import { FaHeart, FaShare } from 'react-icons/fa';

import { useRecipeStore } from '../../stores/recipeStore';
import { api } from '../../utils/api';

interface Props {
  recipeId: number;
  isFavorite: boolean;
}

export const RecipeActions: React.FC<Props> = ({ recipeId, isFavorite }) => {
  const { toggleFavorite } = useRecipeStore();
  const [isSharing, setIsSharing] = React.useState(false);
  const [shareUrl, setShareUrl] = React.useState<string>();
  const toast = useToast();

  const handleFavorite = async () => {
    await toggleFavorite(recipeId);
  };

  const handleShare = async () => {
    try {
      setIsSharing(true);
      const response = await api.recipes.share(recipeId);
      setShareUrl(response.data.url);

      await navigator.clipboard.writeText(response.data.url);

      toast({
        title: 'Recipe link copied!',
        description: 'The recipe URL has been copied to your clipboard.',
        status: 'success',
        duration: 3000,
        isClosable: true,
      });
    } catch (error) {
      console.error('Failed to share recipe:', error);
      toast({
        title: 'Failed to share recipe',
        description: 'An error occurred while trying to share the recipe.',
        status: 'error',
        duration: 3000,
        isClosable: true,
      });
    } finally {
      setIsSharing(false);
    }
  };

  return (
    <>
      <HStack justify="space-between">
        <HStack>
          <Button
            leftIcon={<FaHeart />}
            variant={isFavorite ? 'solid' : 'outline'}
            colorScheme={isFavorite ? 'red' : 'gray'}
            onClick={handleFavorite}
          >
            Favorite
          </Button>
          <Tooltip
            label={shareUrl ? 'Click to copy link again' : 'Share recipe'}
          >
            <Button
              leftIcon={<FaShare />}
              onClick={handleShare}
              isLoading={isSharing}
              colorScheme={shareUrl ? 'green' : 'gray'}
            >
              {shareUrl ? 'Shared' : 'Share'}
            </Button>
          </Tooltip>
        </HStack>
      </HStack>

      {shareUrl && (
        <Box p={2} bg="gray.50" borderRadius="md">
          <Text fontSize="sm" color="gray.600">
            Shared URL: {shareUrl}
          </Text>
        </Box>
      )}
    </>
  );
};
