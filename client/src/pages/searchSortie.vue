<template>
  <div>
    <!-- Header -->
    <Header title="Page temporaire"/>
    <!-- NavBar -->
    <NavBar> </NavBar>
    <!-- Sorties -->
    <div class="row">
      <div class="col-sm-10">
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Nom</th>
              <th scope="col">Type</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(sortie, index) in sorties" :key="index">
              <td>{{ sortie.nom }}</td>
              <td>{{ sortie.typeSortie }}</td>
              <td>
              </td>
            </tr>
          </tbody>
        </table>
    </div>
    </div>
    <!-- Footer -->
    <Footer />
    <div :key="key"></div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import Header from './header.vue';
import NavBar from './navBar.vue';
import Footer from './footer.vue';

export default {
  data() {
    return {
      sorties: [],
    };
  },
  components: {
    alert: Alert, Header, NavBar, Footer,
  },
  methods: {
    forceRerender() {
      this.key += 1;
    },
    getSearch() {
      const path = `http://localhost:5000/api/search/${this.$route.params.search}`;
      axios.get(path)
        .then((res) => {
          this.sorties = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getSearch();
  },
};
</script>

<style>
  .bouton {
    background-color: rgb(65, 192, 171);
  }
</style>
