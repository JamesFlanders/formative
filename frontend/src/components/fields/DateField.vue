<template>
  <label class="form-label" :for="props.id">{{ props.name }}</label>
  <input type="date" :name="props.id" class="form-control"/>
</template>
<script setup>
const props = defineProps({id: String, name: String, required: Boolean});
</script>
<script>
import {setRequired} from "@/js/fields";

export default {
  name: "DateField",
  mounted() {
    setRequired(this.id, this.required);
  }
}
</script>