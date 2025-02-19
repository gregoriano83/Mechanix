<template>
    <div class="page-edit-client">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edytuj - {{ order.car_name }} {{ order.car_model }} {{ order.car_engine }}</h1>
          </div>

          <div class="column is-6">
            <div class="field">
                <label>Przedmiot zlecenia</label>
                    <div class="control">
                        <div class="select">
                            <select v-model="order.item">
                                <option value="Rozrusznik">Rozrusznik</option>
                                <option value="Alternator">Alternator</option>
                            </select>
                        </div>
                    </div>     
                </div>

            <div class="field">
                <label>Marka</label>

                <div class="control">
                    <input type="text" name="car_name" class="input" v-model="order.car_name">
                </div>
            </div>

            <div class="field">
                <label>Model</label>

                <div class="control">
                    <input type="text" name="car_model" class="input" v-model="order.car_model">
                </div>
            </div>

            <div class="field">
                <label>Silnik</label>

                <div class="control">
                    <input type="text" name="car_engine" class="input" v-model="order.car_engine">
                </div>
            </div>

            <div class="field">
                <label>VIN pojazdu</label>

                <div class="control">
                    <input type="text" name="car_vin" class="input" v-model="order.car_vin">
                </div>
            </div>

            <div class="field">
                <label>Numer części</label>

                <div class="control">
                    <input type="text" name="item_number" class="input" v-model="order.item_number">
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
        name: 'EditOrder',
        data() {
            return {
                order: {} 
            }
        },
        mounted() {
            this.getOrder()
        },
        methods: {
            getOrder() {
                const orderID = this.$route.params.id

                axios
                    .get(`/api/v1/orders/${orderID}`)
                    .then(response => {
                        this.order = response.data
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
            },
            submitForm() {
                const orderID = this.$route.params.id
                axios
                    .patch(`/api/v1/orders/${orderID}/`, this.order)
                    .then(response => {
                        this.$router.push(`/dashboard/orders/${orderID}`)
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })

           }

        }
    }

</script>