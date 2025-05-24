const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // Your FastAPI backend URL
        changeOrigin: true,
        // pathRewrite: { '^/api': '' }, // Uncomment if your backend API doesn't have /api prefix
      },
    },
    // Fix for Docker container port mapping if needed
    // client: {
    //   webSocketURL: 'ws://localhost:8080/ws',
    // },
    // headers: {
    //   "Access-Control-Allow-Origin": "*",
    // },
  }
})