<template>
  <label class="form-label" :for="props.name">{{ props.name }}</label>
  <input type="date" class="form-control"/>
</template>
<script setup>
const props = defineProps({name: String});
</script>
<script>
export default {
  name: "DateField",
}
</script>