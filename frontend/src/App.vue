<template>
  <div id="app-container">
    <h1>Data Visualization</h1>
    <DataChart />
  </div>
</template>

<script>
import DataChart from './components/DataChart.vue'

export default {
  name: 'App',
  components: {
    DataChart
  }
}
</script>

<style>
#app-container {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>