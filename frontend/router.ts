import { RootRoute, Route, Router, createHashHistory } from '@tanstack/router';
import { z } from 'zod';

// Define type-safe search params
const searchParamsSchema = z.object({
  q: z.string().optional(),
  category: z.string().optional(),
  page: z.coerce.number().optional(),
  filters: z.string().optional(), // JSON stringified filters
});

export type SearchParams = z.infer<typeof searchParamsSchema>;

// Root route
const rootRoute = new RootRoute();

// Routes with type-safe params and search params
const indexRoute = new Route({
  getParentRoute: () => rootRoute,
  path: '/',
  validateSearch: searchParamsSchema,
});

const recipeRoute = new Route({
  getParentRoute: () => rootRoute,
  path: 'recipe/$recipeId',
  parseParams: (params) => ({
    recipeId: Number(params.recipeId),
  }),
  validateSearch: searchParamsSchema,
});

// Create and export the router
const routeTree = rootRoute.addChildren([indexRoute, recipeRoute]);

export const router = new Router({
  routeTree,
  history: createHashHistory(),
  defaultPreload: 'intent',
});

declare module '@tanstack/router' {
  interface Register {
    router: typeof router;
  }
}
