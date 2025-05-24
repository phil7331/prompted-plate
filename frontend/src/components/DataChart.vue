<template>
  <div class="chart-container">
    <canvas ref="myChartCanvas"></canvas>
    <p v-if="error">{{ error }}</p>
    <p v-if="loading">Loading chart data...</p>
  </div>
</template>

<script>
import axios from 'axios';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default {
  name: 'DataChart',
  data() {
    return {
      chartData: null,
      error: null,
      loading: true,
      chartInstance: null,
    };
  },
  async mounted() {
    await this.fetchChartData();
    if (this.chartData) {
      this.renderChart();
    }
  },
  beforeUnmount() {
    if (this.chartInstance) {
      this.chartInstance.destroy();
    }
  },
  methods: {
    async fetchChartData() {
      this.loading = true;
      this.error = null;
      try {
        // The URL will be 'http://backend:8000/api/chart-data' when running in Docker
        // For local development (frontend served by `npm run serve`, backend by `uvicorn`):
        // use 'http://localhost:8000/api/chart-data'
        // We use a relative path here and let docker-compose/networking handle it,
        // or rely on proxy if running dev server (see vue.config.js if needed)
        const response = await axios.get('/api/chart-data'); // Proxied by vue.config.js or direct in Docker
        this.chartData = {
          labels: response.data.map(item => item.label),
          datasets: [
            {
              label: 'Dummy Data Values',
              backgroundColor: '#f87979',
              borderColor: '#f87979',
              data: response.data.map(item => item.value),
              fill: false,
              tension: 0.1
            },
          ],
        };
      } catch (e) {
        console.error("Error fetching chart data:", e);
        this.error = "Failed to load chart data. Is the backend running?";
        // Fallback to some default data or show error
        this.chartData = {
          labels: ['Error'],
          datasets: [{ label: 'Error', data: [0], backgroundColor: '#CCCCCC' }]
        };
      } finally {
        this.loading = false;
      }
    },
    renderChart() {
      if (this.chartInstance) {
        this.chartInstance.destroy(); // Destroy old chart before rendering new one
      }
      const ctx = this.$refs.myChartCanvas.getContext('2d');
      if (ctx && this.chartData) {
        this.chartInstance = new Chart(ctx, {
          type: 'bar', // You can change type to 'line', 'pie', etc.
          data: this.chartData,
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              y: {
                beginAtZero: true
              }
            }
          },
        });
      } else {
        console.error("Canvas context not found or no chart data.");
        this.error = "Could not render chart."
      }
    }
  }
};
</script>

<style scoped>
.chart-container {
  position: relative;
  margin: auto;
  height: 60vh; /* Adjust height as needed */
  width: 80vw;  /* Adjust width as needed */
  max-width: 700px; /* Optional: set a max width */
}
canvas {
  display: block; /* Prevents an extra space below the canvas */
}
p {
  color: red;
}
</style>