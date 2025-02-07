import type React from 'react';

import { Container, Typography } from '@mui/material';

import RecipeList from '../components/RecipeList';

const RecipesPage: React.FC = () => {
  return (
    <Container maxWidth="lg">
      <Typography
        variant="h4"
        component="h1"
        gutterBottom
        sx={{ mt: 4, mb: 2 }}
      >
        FPIES-Safe Recipes
      </Typography>
      <RecipeList />
    </Container>
  );
};

export default RecipesPage;
