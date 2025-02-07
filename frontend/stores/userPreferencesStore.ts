import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';

type UserPreferences = {
  theme: 'light' | 'dark';
  fontSize: 'small' | 'medium' | 'large';
  allergies: string[];
  // Actions
  setTheme: (theme: UserPreferences['theme']) => void;
  setFontSize: (size: UserPreferences['fontSize']) => void;
  updateAllergies: (allergies: string[]) => void;
};

export const useUserPreferences = create<UserPreferences>()(
  devtools(
    persist(
      (set) => ({
        // Initial state
        theme: 'light',
        fontSize: 'medium',
        allergies: [],

        // Actions
        setTheme: (theme) => set({ theme }),
        setFontSize: (fontSize) => set({ fontSize }),
        updateAllergies: (allergies) => set({ allergies }),
      }),
      {
        name: 'user-preferences', // name in localStorage
      }
    ),
    { name: 'User Preferences Store' }
  )
);
