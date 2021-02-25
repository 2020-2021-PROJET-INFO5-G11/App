<template>
  <!-- Header -->
    <div class="row headBand">
      <div style="text-align: center;" class="col-md-auto">
        <img class="fit-picture" src="../logo_blanc.png"  >
        <h6 style="padding-left: 5px;"> Nom application</h6>
      </div>
      <div class="col-md-auto">
        <br>
        <h1> {{title}}</h1>
      </div>
    </div>
</template>

<script>
export default {
  props: ['title'],
  data() {
    return{};
  },
};
</script>

<style>
.headBand {
  padding: 100 px;
  background-color: rgb(65, 192, 171);
  color: rgb(245, 245, 245);
}

.fit-picture {
    width: 100px;
}

h2 {
  left: 0px;
}

</style>
