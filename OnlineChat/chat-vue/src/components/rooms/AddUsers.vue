<template>
    <div>
        <select v-model="option">
            <option v-for="user in list"
                    :value="user.id"
                    v-bind:key="user">
                {{user.attributes.username}}
            </option>
        </select>
        <mu-button class="btn-send" round color="success" @click="addUser">+</mu-button>
    </div>
</template>

<script>
/* eslint-disable */
    export default {
        name: "AddUsers",
        props: {
            room: '', // чтобы получать номер комнаты
        },
        data() {
            return {
                option: '',
                list: '',
            }
        },
        created() {
            this.loadUsers()
        },
        methods: {
            // Получать список пользователей
            loadUsers() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/users/',
                    type: 'GET',
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            addUser() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/users/',
                    type: 'POST',
                    data: {
                        room: this.room,
                        user: parseInt(this.option)
                    },
                    success: (response) => {
                        alert('Пользователь добавлен')
                    },
                    error: (response) => {
                        alert('Error add user')
                    }
                })
                // Добавить пользователя
            }
        }
    }
</script>

<style scoped>

</style>
