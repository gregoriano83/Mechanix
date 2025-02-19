<template>
    <div class="page-edit-client">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edytuj - {{ client.company }}</h1>
          </div>

          <div class="column is-6">
            <div class="field">
                <label>Nazwa firmy</label>

                <div class="control">
                    <input type="text" name="name" class="input" v-model="client.company">
                </div>
            </div>

            <div class="field">
                <label>Email</label>

                <div class="control">
                    <input type="email" name="email" class="input" v-model="client.email">
                </div>
            </div>

            <div class="field">
                <label>Adres</label>

                <div class="control">
                    <input type="text" name="address1" class="input" v-model="client.address1">
                </div>
            </div>

            <div class="field">
                <label>Address c.d.</label>

                <div class="control">
                    <input type="text" name="address2" class="input" v-model="client.address2">
                </div>
            </div>

          </div>

          <div class="column is-6">
            <div class="field">
                <label>Kod pocztowy</label>

                <div class="control">
                    <input type="text" name="zipcode" class="input" v-model="client.zipcode ">
                </div>
            </div>

            <div class="field">
                <label>Miasto</label>

                <div class="control">
                    <input type="text" name="city" class="input" v-model="client.city">
                </div>
            </div>
            
        </div>

        <div class="column is-12">
            <div class="field">
                <div class="control">
                    <button class="button is-success" @click="submitForm">Zapisz zmiany</button>
                </div>
            </div>
            
        </div>
        </div>
    </div>
</template>
 
<script>
import axios from 'axios'

    export default {
        name: 'EditClient',
        data() {
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
            },
            submitForm() {
                const clientID = this.$route.params.id
                axios
                    .patch(`/api/v1/clients/${clientID}/`, this.client)
                    .then(response => {
                        this.$router.push('/dashboard/client')
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })

           }

        }
    }

</script>