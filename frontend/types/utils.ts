/**
 * Type guard to ensure a value is not undefined
 */
export function isDefined<T>(value: T | undefined): value is T {
  return value !== undefined;
}

/**
 * Type guard to ensure a value is not null
 */
export function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}

/**
 * Ensures all properties in an object are required
 */
export type Required<T> = {
  [P in keyof T]-?: T[P];
};

/**
 * Makes specific properties in a type required
 */
export type RequiredProps<T, K extends keyof T> = T & Required<Pick<T, K>>;

/**
 * Type guard for checking if a value is a Promise
 */
export function isPromise<T = unknown>(value: unknown): value is Promise<T> {
  return value instanceof Promise;
}

/**
 * Ensures a function returns a non-Promise type
 */
export type NonPromise<T> = T extends Promise<infer U> ? U : T;

/**
 * Type guard for checking if an object has a specific property
 */
export function hasProperty<T extends object, K extends PropertyKey>(
  obj: T,
  prop: K
): obj is T & Record<K, unknown> {
  return Object.prototype.hasOwnProperty.call(obj, prop);
}

/**
 * Type guard for checking if a value matches a specific type
 */
export function isType<T>(value: unknown, check: (value: unknown) => value is T): value is T {
  return check(value);
}

/**
 * Utility type for API responses that ensures proper typing
 */
export type ApiResponseType<T> = {
  data: T;
  error?: string;
};
