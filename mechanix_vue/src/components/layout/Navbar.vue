<template>
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item"><strong>Mechanix</strong></router-link>
    </div>

    
        <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                    <template v-if="!$store.state.isAuthenticated">
                    <router-link to="" class="button is-info"><strong>Współpraca</strong></router-link>
                    <router-link to="/sign-up" class="button is-success"><strong>Rejestracja</strong></router-link>
                    <router-link to="/log-in" class="button is-light">Zaloguj się</router-link>
                    </template>
                    
                </div>
            </div>
        </div>
    
</nav>
</template>

<script>
export default {

    name: 'Navbar'
    
}
</script>

