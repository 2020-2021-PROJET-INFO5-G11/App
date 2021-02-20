<template>
  <q-card class="q-mr-sm no-shadow">
    <!--<q-card-section class="text-subtitle1 text-grey-8">-->
    <!--Filter By-->
    <!--</q-card-section>-->
    <transition-group appear enter-active-class="animated fadeInLeft">
      <q-list v-for="item in filters_list" :key="item.label">
        <q-item-label class="text-weight-bolder text-grey-9 q-pt-md q-pb-sm" header>
          {{item.label}}
        </q-item-label>
        
        <q-item
          class="q-pa-none"
          v-for="it in item.items"
          :key="it.model"
          tag="label"
          v-ripple
          dense
        >
          <q-item-section side class="q-px-md text-caption">
            <q-checkbox
              @input="
                searched_results = [];
                show_load_more = false;
                log_offset = 0;
              "
              dense
              v-model="it[it.model]"
            >
              {{ it.label }}({{ it.count }})
            </q-checkbox>
          </q-item-section>
        </q-item>

      </q-list>
    </transition-group>
  </q-card>
</template>
<script>
export default {
  name: "filters",

  data() {
    return {
      filters_list: [
        {
          label: "Discount",
          items: [
            {
              Product: false,
              count: 51,
              label: "50% or more",
              model: "Product",
            },
            {
              Product: false,
              count: 3,
              label: "40% or more",
              model: "Product",
            },
            {
              Product: false,
              count: 41,
              label: "30% or more",
              model: "Product",
            },
            {
              Product: false,
              count: 16,
              label: "20% or more",
              model: "Product",
            },
            {
              Product: false,
              count: 16,
              label: "10% or more",
              model: "Product",
            },
          ],
        },

        {
          label: "Sleeve",
          items: [
            {
              Period: false,
              count: 51,
              label: "3/4 Sleeve",
              model: "Period",
            },
            {
              Period: false,
              count: 3,
              label: "Full Sleeve",
              model: "Period",
            },
            {
              Period: false,
              count: 23,
              label: "Half Sleeve",
              model: "Period",
            },
            {
              Period: false,
              count: 65,
              label: "Short Sleeve",
              model: "Period",
            },
          ],
        },
        {
          label: "Size",
          items: [
            {
              AssetType: false,
              count: 51,
              label: "XXS",
              model: "AssetType",
            },
            {
              AssetType: false,
              count: 3,
              label: "XS",
              model: "AssetType",
            },
            {
              AssetType: false,
              count: 23,
              label: "S",
              model: "AssetType",
            },
            {
              AssetType: false,
              count: 65,
              label: "M",
              model: "AssetType",
            },
            {
              AssetType: false,
              count: 35,
              label: "L",
              model: "AssetType",
            },
            {
              AssetType: false,
              count: 23,
              label: "XL",
              model: "AssetType",
            },
            {
              AssetType: false,
              count: 12,
              label: "XXL",
              model: "AssetType",
            },
          ],
        },
      ],
    };
  },
};
</script>

<style scoped></style>
