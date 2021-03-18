<template>
  <!-- Header -->
    <div class="row headBand">

      <div style="text-align: center;" class="col-md-auto">
        <img class="fit-picture" src="../logo_blanc.png">
        <h5 style="padding-left: 5px;"> Osons sortir </h5>
      </div>
      <div class="col-md-auto">
        <br><br>
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

<style scoped>
.headBand {
  padding: 20px;
  background-color: rgb(65, 192, 171);
  color: rgb(245, 245, 245);
}

.fit-picture {
    width: 100px;
}

</style>
