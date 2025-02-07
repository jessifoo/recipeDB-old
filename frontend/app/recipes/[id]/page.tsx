import { useRecipe } from '@/hooks/api/useRecipes';
import {
  Badge,
  Box,
  Container,
  Divider,
  Grid,
  Heading,
  Image,
  List,
  ListIcon,
  ListItem,
  Stack,
  Text,
  useColorModeValue,
} from '@chakra-ui/react';
import { MdCheckCircle, MdTimer } from 'react-icons/md';

export default function RecipeDetailPage({
  params,
}: {
  params: { id: string };
}) {
  const { data: recipe, isLoading, error } = useRecipe(parseInt(params.id));
  const borderColor = useColorModeValue('gray.200', 'gray.700');

  if (isLoading) {
    return (
      <Container maxW="container.xl" py={8}>
        <Text>Loading recipe...</Text>
      </Container>
    );
  }

  if (error) {
    return (
      <Container maxW="container.xl" py={8}>
        <Text color="red.500">Error loading recipe: {error.message}</Text>
      </Container>
    );
  }

  if (!recipe) {
    return (
      <Container maxW="container.xl" py={8}>
        <Text>Recipe not found</Text>
      </Container>
    );
  }

  return (
    <Container maxW="container.xl" py={8}>
      <Stack spacing={8}>
        <Box>
          <Heading size="2xl" mb={4}>
            {recipe.title}
          </Heading>
          {recipe.image_url && (
            <Image
              src={recipe.image_url}
              alt={recipe.title}
              borderRadius="lg"
              width="100%"
              maxH="400px"
              objectFit="cover"
            />
          )}
        </Box>

        <Grid templateColumns={{ base: '1fr', md: '2fr 1fr' }} gap={8}>
          <Stack spacing={6}>
            {recipe.description && (
              <Text fontSize="lg">{recipe.description}</Text>
            )}

            <Box>
              <Heading size="md" mb={4}>
                Instructions
              </Heading>
              <List spacing={4}>
                {recipe.instructions?.map((instruction, index) => (
                  <ListItem key={index} display="flex">
                    <ListIcon as={MdCheckCircle} color="green.500" mt={1} />
                    <Text>{instruction}</Text>
                  </ListItem>
                ))}
              </List>
            </Box>
          </Stack>

          <Stack
            spacing={6}
            borderWidth="1px"
            borderRadius="lg"
            p={6}
            borderColor={borderColor}
          >
            <Box>
              <Heading size="md" mb={4}>
                Details
              </Heading>
              <Stack spacing={3}>
                {recipe.prep_time_minutes && (
                  <Box display="flex" alignItems="center">
                    <ListIcon as={MdTimer} color="blue.500" />
                    <Text>Prep time: {recipe.prep_time_minutes} minutes</Text>
                  </Box>
                )}
                {recipe.cook_time_minutes && (
                  <Box display="flex" alignItems="center">
                    <ListIcon as={MdTimer} color="blue.500" />
                    <Text>Cook time: {recipe.cook_time_minutes} minutes</Text>
                  </Box>
                )}
                {recipe.servings && <Text>Servings: {recipe.servings}</Text>}
              </Stack>
            </Box>

            <Divider />

            <Box>
              <Heading size="md" mb={4}>
                Ingredients
              </Heading>
              <List spacing={2}>
                {recipe.ingredients?.map((ingredient, index) => (
                  <ListItem key={index}>
                    <ListIcon as={MdCheckCircle} color="green.500" />
                    {ingredient}
                  </ListItem>
                ))}
              </List>
            </Box>

            {recipe.cuisine_types?.length > 0 && (
              <>
                <Divider />
                <Box>
                  <Heading size="md" mb={4}>
                    Cuisine
                  </Heading>
                  <Stack direction="row" wrap="wrap" spacing={2}>
                    {recipe.cuisine_types.map((cuisine) => (
                      <Badge
                        key={cuisine.cuisine_id}
                        colorScheme="purple"
                        px={2}
                        py={1}
                        borderRadius="full"
                      >
                        {cuisine.name}
                      </Badge>
                    ))}
                  </Stack>
                </Box>
              </>
            )}
          </Stack>
        </Grid>
      </Stack>
    </Container>
  );
}
