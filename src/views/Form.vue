<template>
  <section class="container form-control">
    <section class="row">
      <aside class="col-5" id="col-left">
        <img src="../../public/images/logo.png" alt="placeholder.png">
        <h1 class="card-title">{{ form.name }}</h1>
        <p class="card-text">{{ form.description }}</p>
      </aside>
      <aside class="col" id="col-right">
        <FormFields :form="form"/>
      </aside>
    </section>
  </section>
</template>
<style scoped>

aside h1 {
  text-align: center;
}

aside p {
  text-align: center;
}

aside img {
  width: 50%;
  margin: 50px 25%;
}

.container {
  padding: 0;
}

.row {
  margin: 0;
}

#col-left {
  padding: 25px;
  background: var(--bs-primary-bg-subtle);
}

</style>
<script>
import forms from '../../public/forms.json';
import Card from "@/components/Card.vue";
import FormFields from "@/components/FormFields.vue";


export default {
  name: "CardForm",
  components: {
    FormFields,
    Card
  },
  data() {
    return {
      forms: forms,
      formId: this.$route.params.formId,
    }
  },
  computed: {
    form() {
      return this.forms.find(form => form.id === this.formId);
    }
  }
}

</script>


