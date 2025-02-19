<template>
  <div class="home">
    <div class="hero is-info is-small mb-6">
      <div class="hero-body has-text-centered">
        <h1 class="title">ElektroMechanix</h1>
        <h1 class="subtitle">- Parczew -</h1>
        <P></P>
        <P></P>

        <h2 class="subtitle">Profesjonalna regeneracja oraz naprawa alternatorów i rozruszników.</h2>
      </div> 
    </div>

    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4 mt-6">
            <div class="box has-text-centered" style="background-color:antiquewhite">

              <h2 class="is-size-4 mt-4 mb-4"><strong>Diagnostyka</strong></h2>
              
              <dl>
              <dt>Test urządzenia na specjalnym stole probierczym</dt> 
              <dt>Rozebranie oraz dogłębna analiza podzespołów</dt>
              </dl>
            
            </div>
          </div>


          <div class="column is-4 mt-6">
            <div class="box has-text-centered" style="background-color:antiquewhite">

              <h2 class="is-size-4 mt-4 mb-4"><strong>Naprawa</strong></h2>

              <dl>
              <dt>Rozebranie</dt>
              <dt>Specjalistyczne czyszczenie (szkiełkowanie)</dt>
              <dt><strong>Diagnostyka</strong></dt>
              <dt>Wymiana uszkodzonej części</dt>
              </dl>
            
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered" style="background-color:antiquewhite">

              <h2 class="is-size-4 mt-4 mb-4"><strong>Pełna regeneracja</strong></h2>
              
              <dl>
              <dt>Rozebranie</dt>
              <dt>Specjalistyczne czyszczenie (szkiełkowanie)</dt>
              <dt><strong>Diagnostyka</strong></dt>
              <dt>Wymiana wszystkich niezbędnych elementów potrzebnych do dalszej długotrwałej pracy</dt>
              </dl>

            </div>
          </div>

          <div class="column is-12 has-text-centered">
             <router-link to="/dashboard/orders" class="button is-info is-size-4 mt-6 mb-6">Rezerwacja naprawy</router-link>
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  beforeCreate() {
    this.$store.commit('removeToken')
  }
}
</script>


