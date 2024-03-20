<template>
  <form @submit.prevent="performAction" id="card-form">
    <article v-for="item in getFieldComponents(form.fields)">
      <Component :is="item"/>
    </article>
    <button class="btn btn-primary" id="card-submit">Submit</button>
  </form>
</template>
<style scoped>

#card-form {
  width: 90%;
  padding: 20px;
  margin: 0 5%;
  text-align: center;
}

form article {
  margin: 40px 0;
}

</style>
<script>
import {getFieldComponents} from "@/js/form";
import {performAction} from "@/js/actions";

export default {
  name: 'FormFields',
  props: ["form"],
  methods: {performAction, getFieldComponents}
}
</script>