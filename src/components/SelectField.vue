<template>
  <label class="form-label" :for="props.id">{{ props.name }}</label>
  <select class="form-select" :name="props.id">
    <option v-for="option in options" :value="option" :selected="value">{{ option }}</option>
  </select>
</template>
<script setup>
const value = defineModel('value');
const props = defineProps({id: String, name: String, "options": Array})
</script>
<script>
export default {
  name: "SelectField",
}
</script>