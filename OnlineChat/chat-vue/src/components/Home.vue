<template>
    <div>
        <h1>Чат на Vue-js</h1>
        <button @click="goLogin" v-if="!auth">Вход</button>
        <button @click="Logout" v-else>Выход</button>
        <Room v-if="auth"></Room>
    </div>
</template>

<script>
/* eslint-disable */
    import Room from '@/components/Room'
    export default {
        name: 'Home',
        components: {
            Room
        },
        computed: { //вычисляемое свойство. отслежиает, залогинен ли пользователь
            auth() {
                if (sessionStorage.getItem('auth_token')) {
                    return true
                }
            }

        },
        methods: {
            goLogin() {
                this.$router.push({name: 'login'})// в функции гоЛогин перенаправляемся в компонент с именем 'login' (то, что указали в index.js)
            },
            Logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            }
        }
    }
</script>

<style scoped>

</style>
