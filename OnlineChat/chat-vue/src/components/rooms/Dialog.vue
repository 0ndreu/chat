<template>
    <mu-col span="8" xl='10' class="dialog">
        <mu-container>
            <mu-raw direction="column" justify-content="start" align-items="end"
                    v-for="dialog in dialogs" v-bind:key="dialog">
                <p><strong>{{dialog.user.username}}</strong></p>
                <p>{{dialog.text}}</p>
                <span>{{dialog.date}}</span>
            </mu-raw>
        </mu-container>
    </mu-col>
</template>

<script>
/* eslint-disable */
    import $ from 'jquery'

    export default {
        name: "Dialog",
        props: {
            id: ''
        },
        data() {
            return {
                dialogs: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')} // так как нужен токен для диалогов
            });
            this.loadDialog()
        },
        methods: {
            loadDialog() {
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
        border: 1px solid #000;
    }
</style>
