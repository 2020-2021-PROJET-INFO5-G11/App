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
        <span class="nom"> {{sortie.nom}} &ensp;-&ensp; </span>
        <span class="id">ID: {{id}} </span>

        <!-- Buttons : show memberd and subscribe/unsuscribe-->
        <div style="float: right; margin-right: 1%;">
          <button @click="$bvModal.show('show-members')" class="showMembers">
            Voir les participants
          </button>
          <button @click="$bvModal.show('subscribe')" v-if="!is_subscribed && (sortie.capaciteMax - sortie.nbInscrits != 0)"
            :disabled="sortie.capaciteMax - sortie.nbInscrits == 0" class="subscribe">
            Inscription
          </button>
          <button @click="$bvModal.show('edit-subscribe')" v-if="is_subscribed"
            class="subscribe">
            Modifier l'inscription
          </button>
          <br>
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
              {{ current_user.prenom }} {{ current_user.nom }} ( vous )
              <br>
            </div>
            <!-- Other members -->
            <div v-for="m in sortie.participants" v-bind:key="m"
                 class="member">
              <div v-if="m.userName !== current_user.userName">
                {{ m.prenom }} {{ m.nom }}
              </div>
              <br>
            </div>
            <br><br>

            <!-- Suscribe/Unsuscribe-->
            <button v-if="!is_subscribed && (sortie.capaciteMax - sortie.nbInscrits != 0)" 
                    @click="$bvModal.hide('show-members'); $bvModal.show('subscribe');"
                    :disabled="sortie.capaciteMax - sortie.nbInscrits == 0" class="subscribe2">
              S'inscrire
            </button>
            <button v-if="is_subscribed" @click="$bvModal.hide('show-members'); $bvModal.show('edit-subscribe');"
                    class="subscribe2">
              Modifier l'inscription
            </button>
            <br><br>
          </div>
        </div>
      </b-modal>

      <!-- inscription pannel-->
      <b-modal ref="subscribe" id="subscribe" hide-footer
        title="Inscription à la sortie">
        <div style="font-size: 20px;">
          <br>
          <div>
            <div>
              <span> {{sortie.nbInscrits}} personnes participent déjà à l'activité.</span>
            </div>
            <div>
              <span> Il y a {{sortie.capaciteMax - sortie.nbInscrits}} places restantes.</span>
            </div>
          </div>
          <br>
          <!-- nb -->
          <span style="font-weight: bold;"> J'aimerais réserver </span> 
          <!-- <input type="number" style="width: 55px;" min="1" :max="sortie.capaciteMax - sortie.nbInscrits" value="1"/> -->
          <input type="number" style="width: 55px;" min="1" :max="1" value="1"/> 
          <span style="font-weight: bold;"> places. </span>
          <br><br><br><br><br>
          <!-- Suscribe/Unsuscribe-->
          <div style="text-align: center;">
            <button v-on:click="subscribe()" @click="$bvModal.hide('subscribe');"
                    :disabled="sortie.capaciteMax - sortie.nbInscrits == 0" class="subscribe2">
              Enregistrer
            </button>
          </div>
          <br><br>
        </div>
      </b-modal>

      <!-- edit inscription pannel-->
      <b-modal ref="edit-subscribe" id="edit-subscribe" hide-footer
        title="Inscription à la sortie">
        <div style="font-size: 20px;">
          <br>
          <div>
            <div>
              <span> {{sortie.nbInscrits}} personnes participent déjà à l'activité.</span>
            </div>
            <div>
              <span> Il y a {{sortie.capaciteMax - sortie.nbInscrits}} places restantes.</span>
            </div>
          </div>
          <br>
          <!-- nb -->
          <span style="font-weight: bold;"> J'aimerais réserver </span> 
          <!-- <input type="number" style="width: 55px;" min="0" :max="sortie.capaciteMax - sortie.nbInscrits value="0"/> -->
          <input type="number" style="width: 55px;" min="0" :max="0" value="0"/>
          <span style="font-weight: bold;"> places. </span>
          <br><br><br><br><br>
          <!-- Suscribe/Unsuscribe-->
          <div style="text-align: center;">
            <button v-on:click="unsuscribe()" @click="$bvModal.hide('edit-subscribe');"
                    class="subscribe2">
              Enregistrer la modification
            </button>
          </div>
          <br><br>
        </div>
      </b-modal>

      <br><br>

      <!-- Photo + type + description -->
      <ul>
        <!-- Activity's photo-->
        <li style="height: 250px;">
          <div class="rect img-container" @click="$router.push({path: `/sortie/${sortie.id_sortie}`})">
            <img class="fit-picture" :src="getImgUrl(sortie.photo)"  >
            <img v-if="sortie.capaciteMax - sortie.nbInscrits == 0" class="overlay-img fit-picture" src="../assets/complet.png"  >
          </div> <br>
        </li>

        <!-- Type + Description -->
        <li style="height: 250px;" class="resume">
          <span class="resumeTitle">
            Type : 
          </span>
          <span class="resumeContent">
            {{sortie.typeSortie}}
          </span><br><br>
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
            <br>  
            <span> {{ sortie.capaciteMax - sortie.nbInscrits }} places restantes </span>
          </span>


          <br><br><br>
        </li>
      </ul>
      
      <!-- Edit button -->
      <div @click="$router.push({path: `/modification-sortie/${id}`})" class="edit">
        <img src="../assets/edit.png" width="60">
        <br> <span> Modifier </span>

      </div>

      <br><br>
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
          {{c.timestamp}} - {{ c.contenu }}
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
      current_user: {},
      id: '0',
      comments: ["Trop bien", "C'est sur le parking du haut le rdv ?", "Elle est difficile cette rando pour un débutant ?"],
      is_subscribed: false,
      sortie: {},
    };
  },
  methods: {

    getSortie() {
      const path = `http://localhost:5000/api/sortie/${this.$route.params.id}`;
      axios.get(path)
        .then((res) => {
          this.id = this.$route.params.id;
          this.sortie = res.data;
          this.comments= res.data.commentaires;
          this.getCurrentUser();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getImgUrl(image) {
      return require('../assets/'+image+'.jpg');
    },
    subscribe() {
      const path = `http://localhost:5000/api/sortie/${this.$route.params.id}/register`;
      axios.post(path)
        .then((res) => {
          this.is_subscribed = true;
          this.getSortie();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    unsuscribe() {
      const path = `http://localhost:5000/api/sortie/${this.$route.params.id}/register`;
      axios.delete(path)
        .then((res) => {
          this.is_subscribed = false;
          this.getSortie();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getCurrentUser() {
      const path = 'http://localhost:5000/api/user/current';
      axios.get(path)
        .then((res) => {
          this.current_user = res.data;
          // Is suscribe
          for(const p in this.sortie.participants){
            if(p.userName === this.current_user.userName)
              this.is_subscribed = true;
              break;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    }
    },
    async created() {
      this.getSortie();
    },
};
</script>

<style scoped>

.nom {
  margin-left: 20px;
  font-size: 40px;
}

.id {
  font-size: 45px;
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

.id:hover {
  font-size: 50px;
  cursor: copy;
}

.edit {
  float: right; 
  padding-right: 8%;
  cursor: pointer;
  font-size: 13px;
}

.showMembers {
  width: 350px;
  height: 60px;
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

.membersCount {
  padding-left: 50px;
  text-align: center;
  width: 350px;
  height: 60px;
  font-size: 20px;
}

.remainingPlaces {
  padding-left: 50px;
  text-align: center;
  width: 250px;
  height: 60px;
  font-size: 20px;
}

.subscribe {
  width: 300px;
  height: 60px;
  font-size: 30px;
  margin-left: 10px;
  margin-right: 20px;
  background-color: rgb(61, 150, 135);
  border-color: white;
  color: whitesmoke;
}

.subscribe2 {
  padding: 10px;
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
  width: 600px;
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

.img-container {
     position: relative;
}

.overlay-img {
     position: absolute;
     top: 0;
     left: 0;
}

</style>
