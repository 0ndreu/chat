<template>
    <mu-col span="8" xl='9'>
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
                <mu-button round color="success">send</mu-button>
            </mu-row>
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
