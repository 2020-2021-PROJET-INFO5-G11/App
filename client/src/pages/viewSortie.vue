<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- Header -->
    <Header title="Groupes"/>
    <!-- NavBar -->
    <NavBar/>
    <!-- Body -->
    <div>
      <button
          type="button"
          class="btn btn-warning btn-sm"
          v-b-modal.sortie-show-modal
          @click="getSortie()">
        Détails
      </button>
    </div>
    <td> {{ sortie.nom }} </td>
    <br>
    <td> {{ sortie.type }} </td>
    <!-- Footer -->
    <Footer />
    <div :key="key"></div>
  </div>
</template>

<script>
import axios from 'axios';
import Header from './header.vue';
import NavBar from './navBar.vue';
import Footer from './footer.vue';

export default {
  name: 'sortie',
  components: { Header, NavBar, Footer },
  data() {
    return {
      sorties: [],
      sortie: {},
    };
  },
  methods: {
    forceRerender() {
      this.key += 1;
    },
    getSortie() {
      const path = 'http://localhost:5000/sorties';
      axios.get(path)
        .then((res) => {
          this.sorties = res.data.sorties;
          this.sortie = this.sorties.find(s => s.nom === this.$route.params.nom);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  created() {
    this.getSortie();
  },
  },
};
</script>

<style scoped>

i  {
  font-size: 35px;
  color: rgb(65, 192, 171);
}

i:hover {
  color: rgb(15, 138, 117);
  cursor: pointer;
}

.right {
  float: right;
  padding-right: 70px;
}

img:hover {
  opacity: 0.7;
}

.fit-picture {
  width: 291px;
  height: 191px;
}

li {
  display: inline-block;
  margin-left:4em;
}

.rect {
  border: solid;
  border-width: 5px;
  border-color: rgb(65, 192, 171);
  width: 300px;
  height: 200px;
}

.rect:hover {
  border-color: rgb(15, 138, 117);
  cursor: pointer;
}

.scrollmenu {
  overflow: auto;
  white-space: nowrap;
}

h1{
  margin-left:1em;
}

.title {
  width: 300px;
  text-align: center;
}

</style>
