<template>
  <label class="form-label" :for="props.id">{{ props.name }}</label>
  <select multiple class="form-select" :name="props.id">
    <option v-for="option in options" :value="option">{{ option }}</option>
  </select>
</template>
<script setup>
const value = defineModel('value');
const props = defineProps({id: String, name: String, required: Boolean, options: Array});
</script>
<script>
import {setChecked, setRequired} from "@/js/fields";

export default {
  name: "MultiSelectField",
  mounted() {
    setRequired(this.id, this.required)
    setChecked(this.id, this.value);
  }
}
</script>