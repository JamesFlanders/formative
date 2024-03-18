<template>
  <label class="form-label" :for="props.id">{{ props.name }}</label>
  <div>
    <textarea class="form-control" :name="props.id" :value="value"></textarea>
  </div>
</template>
<script setup>
const value = defineModel("value")
const props = defineProps({id: String, name: String, required: Boolean});
</script>
<script>
import {setRequired} from "@/js/fields";

export default {
  name: "LongTextField",
  mounted() {
    setRequired(this.id, this.required);
  }
}
</script>