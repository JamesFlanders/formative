<template>
  <main>
    <header id="status">
      <p><b>Status</b>: {{ this.currentResponse.status }}</p>
    </header>
    <section id="data">
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
      <RouterLink tag="button" class="btn btn-primary" to="#">Go to home</RouterLink>
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
  mounted() {
    this.setDataText(this.currentResponse.data);
    this.setBackgroundColorByStatus(this.currentResponse.status);
  },
  methods: {
    setDataText(json) {
      let section = document.getElementById("data")
      for (const key in json) {
        if (json.hasOwnProperty(key)) {
          if (typeof json[key] === "object") {
            this.setDataText(json[key])
          } else {
            let paragraph = document.createElement("p");
            paragraph.style.margin = "0";
            let boldElement = document.createElement("b");
            boldElement.innerText = key
            let spanElement = document.createElement("span");
            spanElement.innerText = ": " + json[key];
            paragraph.appendChild(boldElement);
            paragraph.appendChild(spanElement);
            section.appendChild(paragraph);
          }
        }
      }
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
    clearDataText() {
      let section = document.getElementById("data");
      section.innerText = "";
    },
    renderPreviousResponse() {
      let offset = this.offset - 1;
      this.clearDataText();
      this.setDataText(this.responses[offset].data);
      this.setBackgroundColorByStatus(this.responses[offset].status);
      renderResponse(this.responses, offset);
    },
    renderNextResponse() {
      let offset = this.offset + 1;
      this.clearDataText();
      this.setDataText(this.responses[offset].data);
      this.setBackgroundColorByStatus(this.responses[offset].status);
      renderResponse(this.responses, offset);
    }
  }
}
</script>