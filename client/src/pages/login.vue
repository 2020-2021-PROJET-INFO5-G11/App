<template>
  <div>
    LOGIN PAGE
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: 'mayu',
      password: 'mayur@qu',
      remember_me: false,
    };
  },
  mounted() {},
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
    <style>
.my-card {
  /*width: 55%;*/
  height: 30%;
}

#particles-js {
  position: absolute;
  width: 100%;
  height: 100%;
  /*background: linear-gradient(145deg, #abbaab 15%, #ffffff 70%);*/
  /*background: linear-gradient(145deg,#f7f8f8 11%, #627e79 75%);*/
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 50% 50%;
}

.login-form {
  position: absolute;
}
</style>
