<template>
  <div id="app">
    <router-view :key="$route.fullPath"/>
  </div>
</template>

<style>
#app {
  margin-top: 0px
}
</style>
