<template>
  <section class="container form-control">
    <section class="row">
      <aside class="col col-left">
        <img src="../../public/images/logo.png" alt="placeholder.png">
        <h1 class="card-title">{{ form.name }}</h1>
        <p class="card-text">{{ form.description }}</p>
      </aside>
      <aside class="col col-right col-8">
        <form @submit.prevent="performAction" id="card-form">
          <article v-for="item in getFieldComponents(form.fields)">
            <component :is="item"/>
          </article>
          <input class="btn btn-success" type="submit" value="Submit">
        </form>
      </aside>
    </section>
  </section>
</template>
<style scoped>

#card-form {
  width: 90%;
  padding: 20px;
  margin: 0 5%;
  text-align: center;
}

.container {
  padding: 0;
}

.row {
  margin: 0;
}

.col-left {
  padding: 25px;
  background: var(--bs-secondary);
}


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

aside form article {
  margin: 40px 0;
}

</style>
<script>
import forms from '../../public/forms.json';
import Card from "@/components/Card.vue";
import {getFieldComponents} from "@/js/form";
import {performAction} from "@/js/actions";


export default {
  name: "CardForm",
  methods: {performAction, getFieldComponents},
  components: {
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


