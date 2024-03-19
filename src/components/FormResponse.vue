<template>
  <main>
    <header>
      <p><b>Status</b></p>
    </header>
    <section>
      <p v-for="(value, key) in this.currentResponse"><b>{{ key }}</b>: {{ value }}</p>
    </section>
    <aside v-if="this.hasMultipleResponses" class="btn-group">
      <button @click="renderPreviousResponse" class="btn btn-primary" :disabled="offset <= 0">
        Previous
      </button>
      <button @click="renderNextResponse" class="btn btn-primary" :disabled="this.responses.length <= (offset + 1)">
        Next
      </button>
    </aside>
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

main aside {
  width: 100%;
}

main footer {
  margin: 40px 0;
  width: 100%;
}

</style>
<script>

import {renderResponse} from "@/js/actions";

export default {
  name: 'FormResponse',
  props: ['currentResponse', 'offset', 'responses'],
  data() {
    return {
      hasMultipleResponses: this.responses.length > 1
    }
  },
  methods: {
    renderPreviousResponse() {
      let offset = this.offset - 1;
      renderResponse(this.responses, offset);
    },
    renderNextResponse() {
      let offset = this.offset + 1;
      renderResponse(this.responses, offset);
    }
  }
}
</script>