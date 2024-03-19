<template>
  <label class="form-label" :for="props.id">{{ props.name }}</label>
  <select class="form-select" :name="props.id">
    <option v-for="option in options" :value="option" :selected="value">{{ option }}</option>
  </select>
</template>
<script setup>
const value = defineModel('value');
const props = defineProps({id: String, name: String, required: Boolean, options: Array});
</script>
<script>
import {setRequired} from "@/js/fields";

export default {
  name: "SelectField",
  mounted() {
    setRequired(this.id, this.required)
  }
}
</script>