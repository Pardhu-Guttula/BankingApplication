import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],

  base: '/c0b9164a-76ec-4978-adcc-71df6e601857/preview',
  server: {
    host: '0.0.0.0',
    port: 5173,
    allowedHosts: true,
    hmr: {
      path: '/c0b9164a-76ec-4978-adcc-71df6e601857/preview',
    }
  }
})
