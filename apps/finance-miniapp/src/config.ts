/// <reference types="vite/client" />

export const appConfig = {
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000',
  environment: import.meta.env.MODE,
} as const