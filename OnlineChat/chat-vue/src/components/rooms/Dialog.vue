<template>
    <div class="dialog">
        <div v-for="dialog in dialogs" v-bind:key="dialog">
            <h2>{{dialog.user.username}}</h2>
            <p>{{dialog.text}}</p>
            <span>{{dialog.date}}</span>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
    import $ from 'jquery'

    export default {
        name: "Dialog",
        props: {
            id: ''
        },
        data () {
            return {
                dialogs: '',
            }
        },
        created () {
            $.ajaxSetup({
                    headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')} // так как нужен токен для диалогов
                });
             this.loadDialog()
        },
        methods: {
            loadDialog () {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/dialog/',
                    type: 'GET',
                    data: {
                        room: this.id,
                    },
                    success: (response) => {
                        this.dialogs = response.data.data
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .dialog {
        width: 70%;
        height: 100px;
        border: 1px solid #000;
    }
</style>
