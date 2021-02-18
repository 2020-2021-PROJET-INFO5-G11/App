<template>
  <div>
    <div class="row bg-white q-mt-sm">
      <div
        class="col-lg-2 col-md-2 col-sm-12 col-xs-12"
        style="border-right: 1px solid lightgrey"
      >
        <filters></filters>
      </div>
      <div class="col-lg-10 col-md-10 col-sm-12 col-xs-12">
        <div class="no-row q-pa-md q-gutter-md" v-for="i in [1, 2, 3]" :key="i">
          <productCard></productCard>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import productCard from "../components/productCard";
import filters from "../components/filters";

export default {
  name: "category.vue",
  components: {
    productCard,
    filters,
  },
  data() {
    return {};
  },
};
</script>

<style scoped></style>
