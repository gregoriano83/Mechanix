<template>
    <div class="page-client">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="subtitle">{{ order.car_name }} {{ order.car_model }}<br>{{ order.car_engine }}</h1>   
             
            </div>

            <div class="column is-12">
                <p><strong>{{ order.item }}</strong></p>
                <br>
                <p><strong>VIN: </strong>{{ order.car_vin }}</p>
                <p v-if="order.item_number"><strong>Numer części: </strong>{{ order.item_number }}</p>
                <p v-if="order.status"><strong>Status zlecenia: </strong>{{ order.status}}</p>
                <div v-if="order.status == 'Nowy' || order.status == 'Zlecenie przyjęte'">
                    <router-link :to="{name: 'EditOrder', params: { id: order.id }}" class="button is-info mt-4">Edytuj</router-link>
                </div>

                <div v-else-if="order.status == 'Ukończone zlecenie'" class="column is-12 mt-5">
                    <!-- <button class="button button-noedit is-info mt-4" disabled>Edytuj</button> -->
                    <div class=" notification is-info has-text-centered">
                       <!-- <button class="delete"></button> -->
                        <p>Zlecenie zostało ukończone. Gotowe do odbioru lub dostawy.</p>
                    </div>
                </div>

                <div v-else-if="order.status == 'W realizacji'" class="column is-12 mt-5">
                    <!-- <button class="button button-noedit is-info mt-4" disabled>Edytuj</button> -->
                    <div class=" notification is-warning has-text-centered">
                       <!-- <button class="delete"></button> -->
                        <p>Funkcja edycji wyłączona z powodu rozpoczęcia realizacji zlecenia. Prosimy o ewentualny kontakt telefoniczny.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

    export default {
        name: 'Order',
        data () {
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
                console.log(orderID)
                axios
                    .get(`/api/v1/orders/${orderID}/`)
                    .then(response => {
                        this.order = response.data
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
            }
        }

    }
</script>