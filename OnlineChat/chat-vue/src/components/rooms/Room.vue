<template>
    <div span="4" sm="4" xl="2">
        <div v-for="room in rooms" v-bind:key="room">
            <h3 @click="openDialog(room.id)">{{room.creator.username}}</h3>
            <small>{{room.date}}</small>
        </div>
    </div>
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
            }
        }
    }
</script>

<style scoped>
    h3 {
        cursor: pointer;
    }
</style>
