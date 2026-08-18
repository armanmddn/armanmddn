import { appConfig } from './config'

export type HealthState = 'checking' | 'available' | 'unavailable'

export async function checkApiHealth(signal?: AbortSignal): Promise<boolean> {
  try {
    const response = await fetch(`${appConfig.apiBaseUrl}/health/ready`, {
      headers: { Accept: 'application/json' },
      signal,
    })
    return response.ok
  } catch {
    return false
  }
}
