<template>
    <mu-col span="4" sm="4" xl="2" class="room-list">
        <mu-button @click="addRoom">Добавить комнату</mu-button>
        <div v-for="room in rooms" v-bind:key="room">
            <h3 @click="openDialog(room.id)">{{room.creator.username}}</h3>
            <small>{{room.date}}</small>
        </div>
    </mu-col>
</template>

<script>
/* eslint-disable */
    import $ from 'jquery'

    export default {
        name: "Room",
        data() {
            return {
                rooms: '',

            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
            });
            this.loadRoom()
        },
        methods: {
            loadRoom() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/room/',
                    type: 'GET',
                    success: (response) => {
                        this.rooms = response.data.data
                    }
                })
            },
            openDialog(id) {
                this.$emit('openDialog', id)
            },
            addRoom() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/chat/room/',
                    type: 'POST',
                    success: (response) => {
                        this.loadRoom()
                    },
                    error: (response) => {
                        alert("Комната не создана")
                    }
                })

            }
        }
    }
</script>

<style scoped>
    h3 {
        cursor: pointer;
    }
    .room-list {
        margin: 0 10px 0 0;
        box-shadow: 1px 4px 5px #848181;
    }
</style>
