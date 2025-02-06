import { setupWorker } from 'msw/browser';
import { recipeHandlers } from './handlers/recipes';

export const worker = setupWorker(...recipeHandlers);

// Expose worker globally
declare global {
  interface Window {
    msw: {
      worker: typeof worker;
    };
  }
}

window.msw = { worker };
