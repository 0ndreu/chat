<template>
    <div>
        <input v-model="login" placeholder="Login" type="text"/>
        <input v-model="password" placeholder="Password" type="password"/>
        <button @click="setLogin">Войти</button>
    </div>
</template>

<script>
/* eslint-disable */
    import $ from 'jquery'

    export default {
        name: 'Login',
        data() {
            return {
                login: '',
                password: ''
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/auth/token/create/',     //куда передаем
                    type: 'POST',
                    data: {                                    // Данные, которые передаем на бэкенд
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("correct!")
                        sessionStorage.setItem('auth_token', response.data.attributes.auth_token)   // .data.attributes - путь до auth_token
                        this.$router.push({name:'home'})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("login or password are incorrect")
                        }
                        console.log(response)
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
