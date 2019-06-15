<template> <!-- весь html который будет -->
  <div id="app">
    <router-view/>      <!-- обрабатывает ВСЕ рауты, они будут содержаться в этом диве -->
  </div>
</template>

<!-- дается название компоненту для экспорта и логика -->

<script>
export default {
  name: 'App'
}
</script>
<!-- все стили цсс к етому компоненту -->
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
