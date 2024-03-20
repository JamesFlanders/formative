<template>
  <label class="form-label" :for="props.id">{{ props.name }}</label>
  <div class="form-control">
    <input class="form-check-input" type="checkbox" :name="props.id">
  </div>
</template>
<style scoped>
</style>
<script setup>
const value = defineModel('value');
const props = defineProps({id: String, name: String});
</script>
<script>
import {setChecked} from "@/js/fields";

export default {
  name: "CheckBoxField",
  mounted() {
    setChecked(this.id, this.value);
  }
}
</script>