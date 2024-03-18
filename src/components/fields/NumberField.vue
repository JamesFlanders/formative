<template>
  <label class="form-label" :for="props.id">{{ props.name }}</label>
  <div>
    <input class="form-control" :name="props.id" type="number" v-model="value">
  </div>
</template>
<script setup>
const value = defineModel('value');
const props = defineProps({id: String, name: String});
</script>
<script>
export default {
  name: "NumberField",
}
</script>