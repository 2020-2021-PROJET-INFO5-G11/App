<template>
  <div class="row items-center q-mx-sm">
    <div class="col-12 q-mt-sm">
      <div class="q-pl-md bg-white q-pt-sm">
        <span class="text-grey-9 text-h6 text-weight-bold">
          {{title}}</span>

  <router-link
    to="/category"
    v-slot="{ href, navigate, isActive, }">
    <NavLink :active="isActive" :href="href" @click="navigate">
      <a class="text-primary q-ml-sm cursor-pointer">{{button}}</a>
    </NavLink>
  </router-link>



       <!-- <a class="text-primary q-ml-sm cursor-pointer">{{button}}</a> -->
      </div>
      <q-carousel
        v-model="latest_slide"
        transition-prev="slide-right"
        transition-next="slide-left"
        swipeable
        animated
        control-color="primary"
        navigation
        padding
        arrows
        height="260px"
        class="rounded-borders"
      >
        <q-carousel-slide
          v-for="val in [1, 2, 3]"
          :name="val"
          :key="val"
          class="column no-wrap"
        >
          <div
            class="row fit justify-start items-center q-gutter-xs q-col-gutter no-wrap"
          >
            <div
              @click="$router.push('/details')"
              class="col-lg-2 col-md-2 col-sm-12 col-xs-12 hover_border_grey text-center full-height"
            >
              <q-img
                style=""
                class="rounded-borders"
                src="https://www.famous-cbd.fr/214-large_default/cbd-amnesia-haze.jpg"
              >
              </q-img>
              <div>Redmi 8</div>
              <div class="text-caption text-weight-bold text-green">
                5000h mAh Battery
              </div>
              <div>
                <span>₹8,499</span
                ><span
                  class="q-ml-sm text-grey-6"
                  style="text-decoration: line-through"
                  >₹10,999</span
                >
              </div>
            </div>
            <div
              @click="$router.push('/details')"
              class="col-lg-2 col-md-2 col-sm-12 col-xs-12 hover_border_grey text-center full-height"
            >
              <q-img
                style=""
                class="rounded-borders"
                src="https://www.famous-cbd.fr/214-large_default/cbd-amnesia-haze.jpg"
              >
              </q-img>
              <div>Redmi 8</div>
              <div class="text-caption text-weight-bold text-green">
                5000h mAh Battery
              </div>
              <div>
                <span>₹8,499</span
                ><span
                  class="q-ml-sm text-grey-6"
                  style="text-decoration: line-through"
                  >₹10,999</span
                >
              </div>
            </div>
            <div
              @click="$router.push('/details')"
              class="col-lg-2 col-md-2 col-sm-12 col-xs-12 hover_border_grey text-center full-height"
            >
              <q-img
                style=""
                class="rounded-borders"
                src="https://www.famous-cbd.fr/214-large_default/cbd-amnesia-haze.jpg"
              >
              </q-img>
              <div>Redmi 8</div>
              <div class="text-caption text-weight-bold text-green">
                5000h mAh Battery
              </div>
              <div>
                <span>₹8,499</span
                ><span
                  class="q-ml-sm text-grey-6"
                  style="text-decoration: line-through"
                  >₹10,999</span
                >
              </div>
            </div>
            <div
              @click="$router.push('/details')"
              class="col-lg-2 col-md-2 col-sm-12 col-xs-12 hover_border_grey text-center full-height"
            >
              <q-img
                style=""
                class="rounded-borders"
                src="https://www.famous-cbd.fr/214-large_default/cbd-amnesia-haze.jpg"
              >
              </q-img>
              <div>Redmi 8</div>
              <div class="text-caption text-weight-bold text-green">
                5000h mAh Battery
              </div>
              <div>
                <span>₹8,499</span
                ><span
                  class="q-ml-sm text-grey-6"
                  style="text-decoration: line-through"
                  >₹10,999</span
                >
              </div>
            </div>
            <div
              @click="$router.push('/details')"
              class="col-lg-2 col-md-2 col-sm-12 col-xs-12 hover_border_grey text-center full-height"
            >
              <q-img
                style=""
                class="rounded-borders"
                src="https://www.famous-cbd.fr/214-large_default/cbd-amnesia-haze.jpg"
              >
              </q-img>
              <div>Redmi 8</div>
              <div class="text-caption text-weight-bold text-green">
                5000h mAh Battery
              </div>
              <div>
                <span>₹8,499</span
                ><span
                  class="q-ml-sm text-grey-6"
                  style="text-decoration: line-through"
                  >₹10,999</span
                >
              </div>
            </div>
            <div
              @click="$router.push('/details')"
              class="col-lg-2 col-md-2 col-sm-12 col-xs-12 hover_border_grey text-center full-height"
            >
              <q-img
                style=""
                class="rounded-borders"
                src="https://www.famous-cbd.fr/214-large_default/cbd-amnesia-haze.jpg"
              >
              </q-img>
              <div>Redmi 8</div>
              <div class="text-caption text-weight-bold text-green">
                5000h mAh Battery
              </div>
              <div>
                <span>₹8,499</span
                ><span
                  class="q-ml-sm text-grey-6"
                  style="text-decoration: line-through"
                  >₹10,999</span
                >
              </div>
            </div>
          </div>
        </q-carousel-slide>
      </q-carousel>
    </div>
  </div>
</template>

<script>


export default {
  components:{

},

props: {
  title: String,
  button: String,
  activeButton: Boolean,
},

  data() {
    return {
      latest_slide: 1,
    };
  },
  methods: {},
};
</script>

<style scoped>

</style>