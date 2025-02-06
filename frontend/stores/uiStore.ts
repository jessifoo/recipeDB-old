import { create } from 'zustand';
import { devtools } from 'zustand/middleware';

type UIState = {
  isSidebarOpen: boolean;
  activeModal: string | null;
  filters: {
    searchTerm: string;
    dietaryRestrictions: string[];
  };
  // Actions
  toggleSidebar: () => void;
  setActiveModal: (modal: string | null) => void;
  updateFilters: (filters: Partial<UIState['filters']>) => void;
};

export const useUIStore = create<UIState>()(
  devtools(
    (set) => ({
      // Initial state
      isSidebarOpen: true,
      activeModal: null,
      filters: {
        searchTerm: '',
        dietaryRestrictions: [],
      },

      // Actions
      toggleSidebar: () => set((state) => ({ isSidebarOpen: !state.isSidebarOpen })),

      setActiveModal: (modal) => set({ activeModal: modal }),

      updateFilters: (newFilters) =>
        set((state) => ({
          filters: { ...state.filters, ...newFilters },
        })),
    }),
    { name: 'UI Store' }
  )
);
