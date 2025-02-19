<template>
    <div class="page-client">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ client.company }}</h1>   
                
                <router-link :to="{name: 'EditClient', params: { id: client.id }}" class="button is-success mt-4">Edytuj</router-link>
            </div>

            <div class="column is-12">
                <h2 class="subtitle">Dane kontaktowe</h2>

                <p><strong>{{ client.name }}</strong></p>
                <p v-if="client.email">{{ client.email }}</p>
                <p v-if="client.address1">{{ client.address1 }}</p>
                <p v-if="client.address2">{{ client.address2 }}</p>
                <p v-if="client.zipcode || client.city">{{ client.zipcode }} {{ client.city }}</p>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

    export default {
        name: 'ShowClient',
        data () {
            return {
                client: {}
            } 
        },
        mounted() {
            this.getClient()
        },
        methods: {
            getClient() {
                const clientID = this.$route.params.id

                axios
                    .get(`/api/v1/clients/${clientID}`)
                    .then(response => {
                        this.client = response.data
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
            }
        }

    }
</script>