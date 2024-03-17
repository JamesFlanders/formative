<template>
  <label class="form-label" :for="props.name">{{ props.name }}</label>
  <div>
    <textarea class="form-control" :value="value"></textarea>
  </div>
</template>
<script setup>
const value = defineModel("value")
const props = defineProps({name: String})
</script>
<script>
export default {
  name: "LongTextField",
  props: ["name"]
}
</script>