<template>
  <q-page>
    <div class="row q-col-gutter-sm q-ma-xs">
      <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
        <q-card class="my-card" flat bordered>
          <q-card-section horizontal>
            <q-card-section class="q-pt-xs">
      <!-- info sur le compte -->
            </q-card-section>

            <q-card-section class="col-5 flex flex-center">
              
              <q-img
                class="rounded-borders"
                src="https://cdn.quasar.dev/img/boy-avatar.png"
              />
            </q-card-section>
          </q-card-section>

          <q-separator />


        </q-card>
      </div>
      <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
        <q-card>
          <q-card-section>
            <q-form class="q-gutter-md">
              <q-input filled v-model="user.first_name" label="First Name" lazy-rules />

              <q-input filled v-model="user.last_name" label="Last Name" lazy-rules />

              <q-input filled v-model="user.age" label="Age" lazy-rules />

              <q-input filled v-model="user.email" label="Email" lazy-rules />

              <q-input filled v-model="user.phone" label="Phone" lazy-rules />

              <div>
                <q-btn label="Update" type="submit" color="primary" /> <!-- rajouter la fonction de mise a jour -->
                <q-btn label="Changer le mot de passe" type="submit" color="primary" @click="$router.push('/changement_de_mot_de_passe')"/>
              </div>
            </q-form>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
export default { //rajouter ici les fonctions de récupération des données via la BD
  data() {
    return {
      user: {
        first_name: "Mayur",
        last_name: "Patel",
        age: 30,
        email: "m******@****.com",
        phone: "97******92",
      },
    };
  },
};
</script>

<style scoped></style>
