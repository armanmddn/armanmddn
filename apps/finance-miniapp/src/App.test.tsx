import { render, screen } from '@testing-library/react'
import { afterEach, describe, expect, it, vi } from 'vitest'
import { App } from './App'

describe('finance mini app shell', () => {
  afterEach(() => vi.restoreAllMocks())

  it('renders in Persian and reports a healthy API', async () => {
    const fetchMock = vi
      .spyOn(globalThis, 'fetch')
      .mockResolvedValue(new Response('{}', { status: 200 }))

    render(<App />)

    const headings = screen.getAllByRole('heading')
    const h1 = headings.find((h) => h.tagName === 'H1') as HTMLHeadingElement
    expect(h1).toBeInTheDocument()
    expect(h1.textContent).toMatch(/[\u0600-\u06FF]/)
    expect(screen.getByRole('status')).toHaveTextContent('در حال بررسی')
    expect(await screen.findByText('متصل')).toBeInTheDocument()
    expect(fetchMock).toHaveBeenCalledWith(
      'http://localhost:8000/health/ready',
      expect.objectContaining({ signal: expect.any(AbortSignal) }),
    )
  })

  it('shows a non-blocking offline state when health check fails', async () => {
    vi.spyOn(globalThis, 'fetch').mockRejectedValue(new Error('offline'))

    render(<App />)

    expect(await screen.findByText('بدون اتصال')).toBeInTheDocument()
    const headings = screen.getAllByRole('heading')
    const h1 = headings.find((h) => h.tagName === 'H1') as HTMLHeadingElement
    expect(h1).toBeInTheDocument()
    expect(h1.textContent.length).toBeGreaterThan(0)
  })
})