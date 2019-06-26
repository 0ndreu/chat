<template>
    <div>
        <h1>Чат на Vue-js</h1>
        <button @click="goLogin" v-if="!auth">Вход</button>
        <button @click="Logout" v-else>Выход</button>
        <Room v-if="auth" @openDialog="openDialog"></Room>
       <Dialog v-if="dialog.show" :id="dialog.id"></Dialog>
    </div>
</template>

<script>
/* eslint-disable */
    import Room from '@/components/rooms/Room.vue'
    import Dialog from '@/components/rooms/Dialog.vue'

    export default {
        name: 'Home',
        components: {
            Room,
            Dialog
        },
        data() {
            return {
                dialog: {
                    id: '',
                    show: false,
                }
            }
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
                this.$router.push({name: 'login'}) // в функции гоЛогин перенаправляемся в компонент с именем 'login' (то, что указали в index.js)
            },
            Logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
            openDialog(id) {
                this.dialog.id = id
                this.dialog.show = true
            }
        }
    }
</script>

<style scoped>

</style>
