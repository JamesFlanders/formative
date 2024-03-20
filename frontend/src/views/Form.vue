<template>
  <section class="container form-control">
    <section class="row">
      <aside class="col-4" id="col-left">
        <img :src="require(`../../public/images/${form.image}`)" :alt="form.image">
        <h1 class="card-title">{{ form.name }}</h1>
        <p class="card-text">{{ form.description }}</p>
      </aside>
      <aside class="col-8" id="col-right">
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
import FormCard from "@/components/FormCard.vue";
import FormFields from "@/components/FormFields.vue";
import {getFormConfiguration} from "@/js/form";


export default {
  name: "CardForm",
  components: {
    FormFields,
    FormCard
  },
  data() {
    return {
      form: {},
      formId: this.$route.params.formId,
    }
  },
  async beforeMount() {
    this.form = await getFormConfiguration("/config/forms.json").then((forms) => {
          return forms.find(form => form.id === this.formId)
        }
    );
  }
}

</script>


