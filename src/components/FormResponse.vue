<template>
  <main>
    <header>
      <p><b>Status</b></p>
    </header>
    <section>
      <p v-for="(value, key) in data"><b>{{ key }}</b>: {{ value }}</p>
    </section>
    <footer>
      <button onclick="window.location.reload();" class="btn btn-danger">Resend request</button>
      <router-link class="btn btn-primary" to="/">Go to home</router-link>
    </footer>
  </main>
</template>
<style scoped>

.btn {
  margin: 10px 0;
}

p {
  margin: 0;
}

main {
  width: 90%;
  padding: 20px;
  margin: 0 5%;
}

main header {
  margin: 40px 0;
  padding: 10px;
  background: var(--bs-success-bg-subtle);
  border: 1px solid var(--bs-success-border-subtle);
  border-radius: .25rem;
}

main section {
  margin: 40px 0;
  padding: 10px;
  background: var(--bs-gray-200);
  border: 1px solid var(--bs-gray-300);
  border-radius: .25rem;
}

main footer {
  margin: 40px 0;
  width: 100%;
}

</style>
<script>

export default {
  name: 'FormResponse',
  props: ['data']
}
</script>