import { useEffect, useState } from 'react'
import { appConfig } from './config'
import { checkApiHealth, type HealthState } from './health'
import './styles.css'

const statusLabels: Record<HealthState, string> = {
  checking: 'در حال بررسی',
  available: 'متصل',
  unavailable: 'بدون اتصال',
}

export function App() {
  const [health, setHealth] = useState<HealthState>('checking')

  useEffect(() => {
    const controller = new AbortController()
    void checkApiHealth(controller.signal).then((isAvailable) => {
      if (!controller.signal.aborted) setHealth(isAvailable ? 'available' : 'unavailable')
    })
    return () => controller.abort()
  }, [])

  return (
    <main className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">نسخه آزمایشی</p>
          <h1>مربی مالی</h1>
        </div>
        <div className={`status status--${health}`} role="status" aria-live="polite">
          <span className="status__dot" aria-hidden="true" />
          {statusLabels[health]}
        </div>
      </header>

      <section className="hero" aria-labelledby="welcome-title">
        <p className="hero__icon" aria-hidden="true">هدف</p>
        <h2 id="welcome-title">برای پس‌انداز این ماه آماده‌ای؟</h2>
        <p>درآمد و هدفت را مشخص کن تا سقف خرج روزانه‌ات را با هم بسازیم.</p>
        <button type="button" disabled>شروع تنظیم برنامه</button>
        <small>راه‌اندازی حساب در فاز بعد فعال می‌شود.</small>
      </section>

      <footer className="runtime-info">
        <span>محیط: {appConfig.environment}</span>
        <span className="runtime-info__url" title={appConfig.apiBaseUrl}>API: {appConfig.apiBaseUrl}</span>
      </footer>
    </main>
  )
}
