import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { ApiConfig } from '../types/api';

interface ApiConfigState {
  configs: Record<string, ApiConfig>;
  setConfig: (apiName: string, config: Partial<ApiConfig>) => void;
  getConfig: (apiName: string) => ApiConfig | undefined;
  resetConfig: (apiName: string) => void;
}

export const useApiConfigStore = create<ApiConfigState>()(
  persist(
    (set, get) => ({
      configs: {},

      setConfig: (apiName: string, config: Partial<ApiConfig>) => {
        set((state) => ({
          configs: {
            ...state.configs,
            [apiName]: {
              ...state.configs[apiName],
              ...config,
              defaultParams: {
                ...state.configs[apiName]?.defaultParams,
                ...config.defaultParams,
              },
              headers: {
                ...state.configs[apiName]?.headers,
                ...config.headers,
              },
            },
          },
        }));
      },

      getConfig: (apiName: string) => {
        return get().configs[apiName];
      },

      resetConfig: (apiName: string) => {
        set((state) => {
          const { [apiName]: _, ...rest } = state.configs;
          return { configs: rest };
        });
      },
    }),
    {
      name: 'api-config-storage',
    }
  )
);
