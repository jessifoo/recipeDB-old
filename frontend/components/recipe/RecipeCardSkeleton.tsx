import type { FC } from 'react';

import {
  Box,
  Card,
  CardBody,
  Skeleton,
  SkeletonText,
  VStack,
} from '@chakra-ui/react';

/**
 * RecipeCardSkeleton displays a loading state for recipe cards
 * matching the layout of the actual RecipeCard component
 */
export const RecipeCardSkeleton: FC = () => {
  return (
    <Card variant="elevated" shadow="md">
      <CardBody>
        <VStack spacing={4} align="stretch">
          <Skeleton height="200px" borderRadius="lg" />
          <SkeletonText noOfLines={2} spacing={2} skeletonHeight={6} />
          <Box pt={2}>
            <Skeleton height="24px" width="120px" />
          </Box>
          <SkeletonText noOfLines={2} spacing={2} />
        </VStack>
      </CardBody>
    </Card>
  );
};
