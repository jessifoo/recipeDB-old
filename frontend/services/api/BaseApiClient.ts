import axios, {
  type AxiosInstance,
  type InternalAxiosRequestConfig,
  type AxiosResponse,
  type AxiosError,
  type RawAxiosRequestHeaders,
  type AxiosRequestConfig,
} from 'axios';
import type {
  ApiConfig,
  ApiRequestConfig,
  RequestInterceptor,
  ResponseInterceptor,
} from '../../types/api';

export class BaseApiClient {
  protected config: ApiConfig;
  protected axios: AxiosInstance;
  protected requestInterceptors: RequestInterceptor[] = [];
  protected responseInterceptors: ResponseInterceptor[] = [];

  constructor(config: Partial<ApiConfig>) {
    this.config = {
      baseUrl: '',
      defaultParams: {},
      headers: {},
      timeout: 10000,
      ...config,
    };

    this.axios = axios.create({
      baseURL: this.config.baseUrl,
      timeout: this.config.timeout,
      headers: this.config.headers,
    });

    // Setup default interceptors
    this.setupInterceptors();
  }

  protected setupInterceptors() {
    // Request interceptor
    this.axios.interceptors.request.use((config: InternalAxiosRequestConfig) => {
      const apiRequestConfig: ApiRequestConfig = {
        url: config.url || '',
        method: (config.method?.toUpperCase() as ApiRequestConfig['method']) || 'GET',
        params: { ...this.config.defaultParams, ...(config.params || {}) },
        data: config.data,
        headers: { ...this.config.headers, ...(config.headers || {}) } as RawAxiosRequestHeaders,
      };

      // Run through all request interceptors
      const modifiedConfig = this.requestInterceptors.reduce(
        (conf, interceptor) => interceptor.onRequest(conf),
        apiRequestConfig
      );

      return {
        ...config,
        ...modifiedConfig,
        headers: { ...config.headers, ...modifiedConfig.headers },
      } as InternalAxiosRequestConfig;
    });

    // Response interceptor
    this.axios.interceptors.response.use(
      async (response: AxiosResponse) => {
        let data = response.data;
        for (const interceptor of this.responseInterceptors) {
          data = await interceptor.onResponse(data);
        }
        return data;
      },
      async (error: AxiosError) => {
        let currentError = error;
        for (const interceptor of this.responseInterceptors) {
          currentError = await interceptor.onError(currentError);
        }
        throw currentError;
      }
    );
  }

  public addRequestInterceptor(interceptor: RequestInterceptor): void {
    this.requestInterceptors.push(interceptor);
  }

  public addResponseInterceptor(interceptor: ResponseInterceptor): void {
    this.responseInterceptors.push(interceptor);
  }

  public updateConfig(newConfig: Partial<ApiConfig>): void {
    this.config = {
      ...this.config,
      ...newConfig,
      defaultParams: {
        ...this.config.defaultParams,
        ...newConfig.defaultParams,
      },
      headers: {
        ...this.config.headers,
        ...newConfig.headers,
      },
    };

    Object.assign(this.axios.defaults, {
      baseURL: this.config.baseUrl,
      timeout: this.config.timeout,
      headers: { ...this.config.headers },
    });
  }

  protected async request<T>(config: ApiRequestConfig): Promise<T> {
    const response = await this.axios.request({
      ...config,
    });
    return response as T;
  }
}
