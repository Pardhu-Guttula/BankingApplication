import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: './',

  server: {
    host: '0.0.0.0',
    port: 5173,
    strictPort: true,
    allowedHosts: 'all',

    hmr: {
      clientPort: 443,
      host: 'code-generation-server.eastus2.cloudapp.azure.com'
    }
  }
})
