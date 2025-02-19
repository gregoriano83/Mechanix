<template>
    <div class="page-client">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title"></h1>
                
            </div>
            
            <div 
                class="column is-3"
                style="margin:0 auto;"
                v-for="client in clients"
                v-bind:key="client.id"
            >
            
                <div class="box" >
                    <h3 class="is-size-4 mb-4">{{ client.company }}</h3>

                    <router-link :to="{ name: 'ShowClient', params: { id: client.id}}" class="button is-info is-small">Szczegóły</router-link>


                </div>
            </div>
            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Wyloguj mnie</button>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

    export default {
        name: 'Client',
        data() {
            return {
                clients: [] 
            }
        },
        mounted() {
            this.getClient()
        },
        methods: {
            logout(){
                axios
                .post('/api/v1/token/logout/')
                .then(response => {
                    axios.defaults.headers.common['Authorization'] = ''

                    localStorage.removeItem('token')

                    this.$store.commit('removeToken')

                    this.$router.push('/')
                })
                .catch(error => {
                    if (error.response) {                 
                        console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            console.log(JSON.stringify(error.message))
                        } else {
                            console.log(JSON.stringify(error))
                        }
                })
            },
            getClient(){
                axios
                    .get('/api/v1/clients/')
                    .then(response => {
                            this.clients.push(response.data[0])
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
            }
        }
    }

</script>