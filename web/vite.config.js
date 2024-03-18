import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'url';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port : 8082,
    host: '0.0.0.0',
    proxy: {
      '/api/v1': {
           target: 'http://localhost:8083',
           changeOrigin: true,
           secure: false,      
           ws: true,
       }
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      '@stores': fileURLToPath(new URL('./src/stores', import.meta.url)),
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
