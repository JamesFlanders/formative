<template>
  <main class="col-8">
    <header id="status">
      <p><b>Status</b>: {{ this.currentResponse.status }}</p>
    </header>
    <section>
      <span @click="copyToClipboard" class="material-icons">content_copy</span>
      <pre>{{ this.currentResponse.data }}</pre>
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
  border-radius: .25rem;
}

main section {
  position: relative;
  margin: 40px 0;
  background: var(--bs-gray-200);
  border: 1px solid var(--bs-gray-300);
  border-radius: .25rem;
}

main section pre {
  padding: 10px;
  width: 100%;
  overflow-x: scroll;
}

main section span {
  position: absolute;
  font-size: 20px;
  top: 8px;
  right: 8px;
}

main section span:hover {
  cursor: pointer;
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
  mounted() {
    this.setBackgroundColorByStatus(this.currentResponse.status);
  },
  methods: {
    copyToClipboard() {
      let pre = document.getElementsByTagName("pre")[0];
      navigator.clipboard.writeText(pre.innerText);
    },
    setBackgroundColorByStatus(status) {
      let header = document.getElementById("status");
      if (status <= 100) {
        header.style.backgroundColor = "var(--bs-info-bg-subtle)";
        header.style.borderColor = "var(--bs-info-border-subtle)";
      }
      if (status >= 200 && status < 400) {
        header.style.backgroundColor = "var(--bs-success-bg-subtle)";
        header.style.borderColor = "var(--bs-success-border-subtle)";
      } else {
        header.style.backgroundColor = "var(--bs-danger-bg-subtle)";
        header.style.borderColor = "var(--bs-danger-border-subtle)";
      }
    },
    renderPreviousResponse() {
      let offset = this.offset - 1;
      this.setBackgroundColorByStatus(this.responses[offset].status);
      renderResponse(this.responses, offset);
    },
    renderNextResponse() {
      let offset = this.offset + 1;
      this.setBackgroundColorByStatus(this.responses[offset].status);
      renderResponse(this.responses, offset);
    }
  }
}
</script>