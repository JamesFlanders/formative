<template>
  <div v-for="form in forms">
    <FormCard :form="form"/>
  </div>
</template>
<script>
import FormCard from "@/components/FormCard.vue";
import {getFormConfiguration} from "@/js/form";

export default {
  name: "Home",
  components: {
    FormCard
  },
  data() {
    return {
      forms: undefined
    }
  },
  async beforeMount() {
    this.forms = await getFormConfiguration("/config/forms.json")
  }
}
</script>