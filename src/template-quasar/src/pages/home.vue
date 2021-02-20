<template>
  <q-page class="q-mt-sm">



  </q-page>
</template>

<script>
import categoryCard from "../components/categoryCard";


export default {
  components:{
    categoryCard
  },
  data() {
    return {
      slide: "first",
      trending_slide: 1,
      latest_slide: 1,
    };
  },
  methods: {},
};
</script>

<style scoped>
.custom-caption {
  text-align: center;
  padding: 8px;
  color: white;
  background-color: rgba(0, 0, 0, 0.3);
}
</style>
