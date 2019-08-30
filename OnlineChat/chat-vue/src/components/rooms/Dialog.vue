<template>
    <mu-col span="8" xl='9'>
        <AddUsers :room="id"></AddUsers>
        <mu-container class="dialog">
            <mu-row direction="column"
                    justify-content="start"
                    align-items="end"
                    v-for="dialog in dialogs"
                    v-bind:key="dialog">
                <p><strong>{{dialog.user.username}}</strong></p>
                <p>{{dialog.text}}</p>
                <span><small>{{dialog.date}}</small></span>
            </mu-row>
        </mu-container>
        <mu-container>
            <mu-row>
                <mu-text-field v-model="form.textarea"
                               multi-line :rows="4"
                               full-width
                               placeholder="Input your message">
                </mu-text-field>
                <mu-button round color="success" @click="sendMes">send</mu-button>
            </mu-row>
        </mu-container>
    </mu-col>
</template>

<script>
/* eslint-disable */

import AddUsers from './AddUsers'
    export default {
        name: "Dialog",
        props: {
            id: '' // присылается сюда ИД комнаты, а потом его кладем в <AddUsers>
        },
        components: {
            AddUsers
        },
        data() {
            return {
                dialogs: '',
                form: {
                    textarea: '',
                }
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')} // так как нужен токен для диалогов
            });
            this.loadDialog()
            setInterval(() => {
                this.loadDialog()
            }, 5000)
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
            },
            sendMes() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/dialog/',
                    type: 'POST',
                    data: {
                        room: this.id,
                        text: this.form.textarea
                    },
                    success: (response) => {
                        this.loadDialog()
                        form.textarea.text = ''
                    },
                    error: (response) => {
                        alert(response.statusText)
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
