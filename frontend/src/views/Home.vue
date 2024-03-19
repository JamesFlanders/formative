<template>
  <div v-for="form in forms">
    <FormCard :form="form"/>
  </div>
</template>
<script>
import forms from '../../public/forms.json';
import FormCard from "@/components/FormCard.vue";

export default {
  name: "Home",
  components: {
    FormCard
  },
  data() {
    return {
      forms
    }
  }
}
</script>