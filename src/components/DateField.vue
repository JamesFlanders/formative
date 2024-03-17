<template>
  <label class="form-label" :for="props.id">{{ props.name }}</label>
  <input type="date" :name="props.id" class="form-control"/>
</template>
<script setup>
const props = defineProps({id: String, name: String});
</script>
<script>
export default {
  name: "DateField",
}
</script>