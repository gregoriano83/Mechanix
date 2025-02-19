<template>
    <div class="page-signup">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Zarejestruj</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Nazwa firmy</label>
                        <div class="control">
                            <input type="text" name="company" class="input" v-model="company">
                        </div>
                    </div>
                    <div class="field">
                        <label>E-mail</label>
                        <div class="control">
                            <input type="email" name="username" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Hasło</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="field">
                        <label>Powtórz hasło</label>
                        <div class="control">
                            <input type="password" name="password2" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    
                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Wyślij</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>

    </div>
    
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

    export default {
        name: 'SignUp',
        data() {
            return {
                username: '',
                password: '',
                password2: '',
                company: '',
                errors: []
            }
        },
        methods: {
            async submitForm(e) {
                this.errors = []

                if (this.username === '') {
                    this.errors.push('Podaj nazwę użytkownika')
                }

                if (this.password === '') {
                    this.errors.push('Hasło jest za krótkie')
                }

                if (this.password !== this.password2) {
                    this.errors.push('Powtórzone hasło nie jest identyczne')
                }

                if (!this.errors.length) {
                    this.$store.commit('setIsLoading', true)
                    
                    const formData = {
                        username: this.username,
                        password: this.password,
                        password2: this.password2,
                        email: this.username,
                        first_name: this.company

                    }

                    axios
                        .post('/api/v1/register/', formData)
                        .then(response => {
                            console.log(response)

                            toast({
                                message: 'Konto zostało utworzone. Proszę się zalogować',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 4000,
                                position: 'bottom-right'
                            })

                            this.$router.push('/log-in')
                        })
                        .catch(error => {
                            if (error.response) {
                                for (const property in error.response.data) {
                                    this.errors.push(`${property}: ${error.response.data[property]}`)
                                }

                                console.log(JSON.stringify(error.response.data))
                            } else if (error.message) {
                                console.log(JSON.stringify(error.message))
                            } else {
                                console.log(JSON.stringify(error))
                            }
                        })
                    } 
                }
                
        },
    }
</script>