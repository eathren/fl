import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import { TanStackRouterVite } from '@tanstack/router-plugin/vite'
import tailwindcss from '@tailwindcss/vite'
import path from "path"
// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss(), TanStackRouterVite({ autoCodeSplitting: true }), ],
   resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})
