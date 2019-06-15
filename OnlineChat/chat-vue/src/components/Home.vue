<template>
    <div>
        <h1>Чат на Vue-js</h1>
        <button @click="goLogin">Вход</button>
    </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    goLogin () {
      this.$router.push({name: 'login'})// в функции гоЛогин перенаправляемся в компонент с именем 'login' (то, что указали в index.js)
    }
  }
}
</script>

<style scoped>

</style>
