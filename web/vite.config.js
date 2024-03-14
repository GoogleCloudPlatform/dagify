import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port : 8082,
    host: '0.0.0.0',
    proxy: {
      '/api/v1': {
           target: 'http://localhost:8081',
           changeOrigin: true,
           secure: false,      
           ws: true,
       }
  }
  },
  build: {
    rollupOptions: {
      output: {
        entryFileNames: `static/[name].js`,
        chunkFileNames: `static/[name].js`,
        assetFileNames: `static/[name].[ext]`
      }
    }
  }
})
