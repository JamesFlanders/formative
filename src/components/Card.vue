<template>
  <article class="card">
    <img class="card-img-top" :src="require(`../../public/images/${form.image}`)" alt="placeholder.png">
    <aside class="card-body">
      <h1 class="card-title">{{ form.name }}</h1>
      <p class="card-text">{{ form.description }}</p>
      <router-link class="btn btn-primary" :to="'/form/' + form.id">Request</router-link>
    </aside>
  </article>
</template>
<style>
.card {
  float: left;
  width: 20%;
  margin: 2.5%;
}

.card-img-top {
  padding: 40px;
  background: var(--bs-primary-bg-subtle);
}

.card-title {
  font-size: 20px;
  font-weight: bold;;
}

.btn {
  width: 100%;
}

</style>
<script>
export default {
  name: "Card",
  props: ["form"]
}
</script>