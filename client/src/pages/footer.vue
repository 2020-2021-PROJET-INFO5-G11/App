<template>
  <div class="footBand">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <ul>
      <li>
        <div> Legal </div>
         <div>
          <i class="fa fa-pencil fa-3x"> Politique </i>
        </div>
        <div>
          <i class="fa fa-newspaper-o fa-3x"> Conditions d'utilisations </i>
        </div>
      </li>

      <li>
        <div> Contactez nous </div>
        <div>
          <i class="fa fa-facebook fa-3x"> Facebook </i>
        </div>
        <div>
          <i class="fa fa-instagram fa-3x"> Instagram </i>
        </div>
      </li>

      <li>
        <div> Redirection </div>
        <div>
          <i class="fa fa-home fa-3x" @click="$router.push('/accueil')"> Acceuil </i>
        </div>
        <div>
          <i class="fa fa-user fa-3x" @click="$router.push({path: `/profil/${current_user.id}`})"> Profil </i>
        </div>
      </li>

    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      current_user: {},
    };
  },
  methods: {
  getCurrentUser() {
      const path = 'http://localhost:5000/api/user/current';
      axios.get(path)
        .then((res) => {
          this.current_user = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getCurrentUser();
  }
  
};
</script>

<style scoped>
.footBand {
  background-color: black;
  color: whitesmoke;
  opacity: 0.7;
}
li {
    display: inline-block;
    padding-left: 100px;
}

i  {
  font-size: 15px;
}

i:hover  {
    cursor: pointer;
    color: rgb(65, 192, 171);
}

div {
  font-size: 18px;
  text-decoration: underline;

}
</style>
