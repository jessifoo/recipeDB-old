import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export interface FamilyMember {
  id: string;
  name: string;
  allergies: string[];
  fpiesTriggers: string[];
  safeSubstitutes: Record<string, string[]>;
  reactionHistory: Array<{
    date: string;
    food: string;
    symptoms: string[];
    notes: string;
  }>;
}

interface FamilyProfileState {
  members: FamilyMember[];
  activeProfile: string | null;
  // Actions
  addMember: (member: Omit<FamilyMember, 'id' | 'reactionHistory'>) => void;
  updateMember: (id: string, updates: Partial<FamilyMember>) => void;
  setActiveProfile: (id: string | null) => void;
  addReaction: (
    memberId: string,
    reaction: Omit<FamilyMember['reactionHistory'][0], 'date'>
  ) => void;
  addSafeSubstitute: (memberId: string, ingredient: string, substitute: string) => void;
}

export const useFamilyProfileStore = create<FamilyProfileState>()(
  persist(
    (set, _get) => ({
      members: [],
      activeProfile: null,

      addMember: (member) =>
        set((state) => ({
          members: [
            ...state.members,
            {
              ...member,
              id: crypto.randomUUID(),
              reactionHistory: [],
            },
          ],
        })),

      updateMember: (id, updates) =>
        set((state) => ({
          members: state.members.map((member) =>
            member.id === id ? { ...member, ...updates } : member
          ),
        })),

      setActiveProfile: (id) => set({ activeProfile: id }),

      addReaction: (memberId, reaction) =>
        set((state) => ({
          members: state.members.map((member) =>
            member.id === memberId
              ? {
                  ...member,
                  reactionHistory: [
                    {
                      ...reaction,
                      date: new Date().toISOString(),
                    },
                    ...member.reactionHistory,
                  ],
                }
              : member
          ),
        })),

      addSafeSubstitute: (memberId, ingredient, substitute) =>
        set((state) => ({
          members: state.members.map((member) =>
            member.id === memberId
              ? {
                  ...member,
                  safeSubstitutes: {
                    ...member.safeSubstitutes,
                    [ingredient]: [...(member.safeSubstitutes[ingredient] || []), substitute],
                  },
                }
              : member
          ),
        })),
    }),
    {
      name: 'family-profiles',
    }
  )
);
