<template>
  <label class="form-label" :for="props.name">{{ props.name }}</label>
  <select class="form-select">
    <option v-for="option in options" :value="option" :selected="value">{{ option }}</option>
  </select>
</template>
<script setup>
const value = defineModel('value');
const props = defineProps({"name": {type: String}, "options": {type: Array}})
</script>
<script>
export default {
  name: "SelectField",
}
</script>