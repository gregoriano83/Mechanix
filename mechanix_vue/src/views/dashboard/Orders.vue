<template>
    <div class="page-orders">
        <div class="columns is-multiline ">
            <div class="column is-12 has-text-centered">
                <h1 class="title">Twoje zlecenia</h1>
                

            </div>
            
            <div class="column is-12">
            <router-link :to="{ name:'' }" class="button is-info is-focused my-3 ml-5">Dodaj zlecenie</router-link>
            </div>
            
            <div
                class="column is-2 mx-1"
                v-for="order in orders"
                v-bind:key="order.id"
            >

                <div class="box">
                    <h3 class="is-size-6 mb-2">{{ order.car_name }} {{ order.car_model }}</h3>
                    <h3 class="is-size-5 mb-2">{{ order.item }}</h3>
                    <h3 class="is-size-7 mb-2">{{ order.status }}</h3>



                    <router-link :to="{ name: 'Order', params: { id: order.id}}" class="button is-link is-rounded is-small">Szczegóły</router-link>


                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

    export default {
        name: 'Orders',
        data() {
            return {
                orders: [] 
            }
        },
        mounted() {
            this.getOrders()
        },
        methods: {
            getOrders(){
                axios
                    .get('/api/v1/orders/')
                    .then(response => {
                        for (let i = 0; i < response.data.length; i++ ) {
                            this.orders.push(response.data[i])
                        }
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
            }
        }
    }

</script>