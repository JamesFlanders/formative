<template>
  <div v-for="form in forms">
    <Card :form="form"/>
  </div>
</template>
<script>
import forms from '../../public/forms.json';
import Card from "@/components/Card.vue";

export default {
  name: "Home",
  components: {
    Card
  },
  data() {
    return {
      forms
    }
  }
}
</script>