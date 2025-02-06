import type { ApiRequestConfig } from '../../../types/api';

export class ApiError extends Error {
  constructor(
    message: string,
    public readonly config?: ApiRequestConfig,
    public readonly statusCode?: number,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'ApiError';
  }

  public static fromError(error: unknown, config?: ApiRequestConfig): ApiError {
    if (error instanceof ApiError) {
      return error;
    }

    if (error instanceof Error) {
      return new ApiError(error.message, config, undefined, error);
    }

    return new ApiError(
      typeof error === 'string' ? error : 'An unexpected error occurred',
      config
    );
  }
}
