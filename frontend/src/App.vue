<template>
  <nav class="navbar navbar-light bg-primary">
    <RouterLink class="navbar-brand" to="/">
      <img src="../public/images/logo.png" width="30" height="30" alt="">
    </RouterLink>
  </nav>
  <main>
    <RouterView v-slot="{ Component, route }">
      <Component :is="Component" view-prop="value"/>
    </RouterView>
  </main>
</template>
<style>

.navbar-brand {
  padding: 0 15px;
}


body {
  margin: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  background-color: #DBDBDB;
}

body main {
  padding: 50px;
}

</style>
<script>

import Home from "@/views/Home.vue";

export default {
  name: "App",
  components: {
    Home
  }
}
</script>