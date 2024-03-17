<template>
  <label class="form-label" :for="props.name">{{ props.name }}</label>
  <div>
    <input class="form-control" :name="props.name" type="text" v-model="value">
  </div>
</template>
<script setup>
const value = defineModel('value');
const props = defineProps({"name": String});
</script>
<script>
export default {
  name: "ShortTextField",
}
</script>