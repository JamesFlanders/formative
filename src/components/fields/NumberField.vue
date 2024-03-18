<template>
  <label class="form-label" :for="props.id">{{ props.name }}</label>
  <div>
    <input class="form-control" :name="props.id" type="number" v-model="value">
  </div>
</template>
<script setup>
const value = defineModel('value');
const props = defineProps({id: String, name: String, required: Boolean});
</script>
<script>
import {setRequired} from "@/js/fields";

export default {
  name: "NumberField",
  mounted() {
    setRequired(this.id, this.required);
  }
}
</script>