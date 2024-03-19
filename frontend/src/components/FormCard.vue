<template>
  <article class="card">
    <img class="card-img-top" :src="require(`../../public/images/${form.image}`)" :alt="form.image">
    <aside class="card-body">
      <h1 class="card-title">{{ form.name }}</h1>
      <p class="card-text">{{ form.description }}</p>
      <RouterLink class="btn btn-primary" :to="'/form/' + form.id">Request</RouterLink>
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

.card-text {
  font-size: 14px;
  height: 75px;
}

.btn {
  width: 100%;
}

</style>
<script>
export default {
  name: "FormCard",
  props: ["form"]
}
</script>