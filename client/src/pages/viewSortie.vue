<template>
  <div>

    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />

    <!-- Header -->
    <Header :title='sortie.nom' />
    <!-- NavBar -->
    <NavBar />

    <!-- Body -->
    <body>
      <br />

      <!-- Title + buttons -->
      <div>
        <!-- Title : current activity's name and current activty's ID -->
        <span class="title"> {{sortie.nom}} - {{sortie.id}} </span>
        <!-- Buttons : show memberd and subscribe/unsuscribe-->
        <div style="float: right">
          <button @click="$bvModal.show('show-members')" class="showMembers">
            Voir les participants
          </button>
          <button v-if="!is_subscribed" v-on:click="is_subscribed = true"
            class="subscribe">
            S'inscrire
          </button>
          <button v-if="is_subscribed" v-on:click="is_subscribed = false"
            class="subscribe">
            Se désinscrire
          </button>
        </div>
      </div>

      <!-- view members pannel-->
      <b-modal ref="showMembers" id="show-members" hide-footer
        title="Liste des participants">
        <div>
          <div style="text-align: center; font-size: 30px;">
            <br>
            <!-- User -->
            <div v-if="is_subscribed"
                 class="user">
              {{ userName }} ( vous )
              <br>
            </div>
            <!-- Other members -->
            <div v-for="m in members" v-bind:key="m"
                 class="member">
              {{ m }}
              <br>
            </div>
            <br><br>

            <!-- Suscribe/Unsuscribe-->
            <button v-if="!is_subscribed" v-on:click="is_subscribed = true"
                    class="subscribe2">
              S'inscrire
            </button>
            <button v-if="is_subscribed" v-on:click="is_subscribed = false"
                    class="subscribe2">
              Se désinscrire
            </button>
            <br><br>
          </div>
        </div>
      </b-modal>

      <br><br>

      <!-- Photo + description -->
      <ul>
        <!-- Activity's photo-->
        <li style="height: 250px;">
          <img class="fit-picture" :src="getImgUrl(sortie.photo)">
        </li>

        <!-- Description -->
        <li style="height: 250px;" class="resume">
          <span class="resumeTitle">
            Description :
          </span>
          <br><br>
          <span class="resumeContent">
            {{ sortie.description }}
          </span>
        </li>
      </ul>

      <!-- Location, Date etc.. --> 
      <ul>
        <li>
          <span class="location">
            {{ sortie.lieu }}
          </span>

          <br>
          
          <span class="date">
            {{ sortie.date }} - {{ sortie.heure }}
          </span>

          <br>
          
          <span class="duree">
            Durée : {{ sortie.duree }}
          </span>

          <br><br><br>
        </li>

        <!-- Separateur -->
        <li style="padding: 10px;">
          <div class="separator">
            <br><br><br><br><br>
          </div>
        </li>

        <li>
          <span class="rdv">
            Lieu de rendez-vous : {{ sortie.point_rdv}}
          </span>

          <br>  
          
          <span class="capacity">
            Capacité min : {{ sortie.capaciteMin }} 
            <span style="padding: 15px;">-</span>
            Capacité max : {{ sortie.capaciteMax }}
          </span>

          <br><br><br>
        </li>
      </ul>

      <!-- Separator -->
      <br><br><br>
      <div class="horizontalSeparator">
        <br>
      </div>

      <!-- Comments -->
      <br>
      <div class="comments">
        <h2> Espace commentaires </h2>
        <br><br>
      </div>

      <div v-for="c in comments" v-bind:key="c"
             class="comment">
        <div style="padding: 5px;">
          {{ c }}
        </div>
      </div>

      <br><br><br>
    </body>

    <!-- Footer -->
    <Footer />

  </div>
</template>

<script>
import axios from "axios";
import Header from "./header.vue";
import NavBar from "./navBar.vue";
import Footer from "./footer.vue";

export default {
  name: "sortie",
  components: { Header, NavBar, Footer },
  data() {
    return {
      name: 'Randonnée entre copains',
      location: 'Mont Jalla',
      date: '26/02/2021',
      hour: '15h30',
      min: 3,
      max: 12,
      rdv: 'Hubert Dubedout, Musée de l\'Eveché',
      id: '112',
      image: 'randonnée',
      resume: "Etiam placerat non dui et tristique. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam placerat non dui et tristique. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam placerat non dui et tristique.",
      userName: "Vernet Maxime",
      members: ["ElJraidi Rim", "Sajide Idriss", "Manissadjian Gabriel"],
      comments: ["Trop bien", "C'est sur le parking du haut le rdv ?", "Elle est difficile cette rando pour un débutant ?"],
      is_subscribed: false,
      sortie: {},
    };
  },
  methods: {

    getSortie() {
      const path = `http://localhost:5000/api/sorties/get_one/${this.$route.params.id}`;
      axios.get(path)
        .then((res) => {
          this.sortie = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getImgUrl(image) {
      return require('../'+image+'.jpg');
    },
    },
    created() {
      this.getSortie();
    },
};
</script>

<style scoped>

.title {
  margin-left: 20px;
  font-size: 40px;
}

.showMembers {
  font-size: 30px;
  text-decoration: bold;
  background-color: rgb(61, 150, 135);
  border-color: white;
  color: whitesmoke;
}

.user:hover {
  font-size: 32px;
}

.member:hover {
  font-size: 32px;
  text-decoration: underline;
}

.subscribe {
  font-size: 30px;
  margin-left: 10px;
  margin-right: 20px;
  background-color: rgb(61, 150, 135);
  border-color: white;
  color: whitesmoke;
}

.subscribe2 {
  font-size: 25px;
  background-color: rgb(61, 150, 135);
  border-color: white;
  color: whitesmoke;
}

.showMembers:hover {
  font-size: 32px;
  background-color: rgb(15, 138, 117);
  cursor: pointer;
  opacity: 0.7;
}

.subscribe:hover {
  font-size: 32px;
  background-color: rgb(15, 138, 117);
  cursor: pointer;
  opacity: 0.7;
}

.subscribe2:hover {
  font-size: 27px;
  background-color: rgb(15, 138, 117);
  cursor: pointer;
  opacity: 0.7;
}

.fit-picture {
  width: 320px;
  height: 210px;
}

li {
  display: inline-block;
  vertical-align: top;
  margin-left: 30px;
}

.resume {
  max-height: 210px;
  width: 1200px;
  overflow-x: scroll;
}

.resumeTitle {
  font-size: 25px;
}

.resumeContent {
  font-size: 20px;
}

.location {
  padding-left: 70px;
  font-size: 25px;
}

.date {
  padding-left: 70px;
  font-size: 20px;
}

.duree {
  padding-left: 70px;
  font-size: 18px;
}

.capacity, .rdv {
  font-size: 20px;
}

.separator {
  border: solid; 
  width: 2px;
  border-width:1px; 
  border-color: grey;
}

.horizontalSeparator {
  border: solid; 
  height: 2px;
  width: 90%;
  margin-left: 5%;
  border-width:1px; 
  border-color: grey;
}

.comments {
  margin-left: 40%;
}

.comment {
  margin-left: 10%;
  margin-top : 10px;
  border: solid;
  border-color:  rgb(15, 138, 117);
  width: 80%;
}

.comment:hover {
  cursor: pointer;
  opacity: 0.7;
}

.modal-backdrop
{
    opacity:0.5 !important;
}

</style>
