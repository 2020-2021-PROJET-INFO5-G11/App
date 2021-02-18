<template>
  <q-card
    @click="$router.push('/details')"
    class="cursor-pointer"
    :class="class_val"
    @mouseover="class_val = 'my-card shadow-20'"
    @mouseleave="class_val = 'my-card shadow-'"
  >
    <q-img src="https://www.famous-cbd.fr/214-large_default/cbd-amnesia-haze.jpg"></q-img>

    <q-card-section class="q-pb-xs q-pt-md">

      <div class="row no-wrap items-center">
        <div class="col text-subtitle2 ellipsis-2-lines text-grey-10">
          Benling C200-BLK Smartwatch (Black Strap Free Size)
        </div>
        <div class="col-auto text-grey text-caption q-pt-md row no-wrap items-center">
          <!--<q-icon name="place"></q-icon>-->
          <!--250 ft-->
        </div>
      </div>

      <q-rating v-model="stars" color="orange" :max="5" readonly size="17px"></q-rating>
    </q-card-section>

    <q-card-section class="q-py-sm">
      <div>
        <div class="text-caption text-green-8 text-weight-bolder">Special Price</div>
        <span class="text-h6">₹3,149</span
        ><span class="q-ml-sm text-grey-6" style="text-decoration: line-through"
          >₹3,699</span
        >
        <span class="q-ml-md text-caption text-green-8 text-weight-bolder q-mt-md"
          >20% off</span
        >
      </div>
    </q-card-section>

    <q-separator></q-separator>

    <q-card-actions>
      <q-btn flat class="text-weight-bold text-capitalize" dense color="primary">
        View details
      </q-btn>
    </q-card-actions>
  </q-card>
</template>


<script>
export default {
  name: "category.vue",
  data() {
    return {
      stars: 4,
      class_val: "shadow-1 my-card",
    };
  },
  computed: {
    win_width() {
      return this.$q.screen.width - 59;
    },
    win_height() {
      return this.$q.screen.height - 0;
    },
  },
};
</script>

<style scoped>
.my-card {
  width: 100%;
  max-width: 300px;
}
</style>
