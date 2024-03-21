<template>
  <label class="form-label" :for="props.id">{{ props.name }}</label>
  <div class="form-control">
    <div class="form-check" v-for="(option, index) in options">
      <label :for="props.id + '-option-' + index">{{ option }}</label>
      <br/>
      <input type="radio" :name="props.id" :id="props.id + '-option-' + index" :value="option">
    </div>
  </div>
</template>
<style scoped>

.form-control {
  overflow: auto;
}

.form-check {
  width: 40%;
  padding: 0;
  margin: 0 5%;
  float: left;
}

</style>
<script setup>
const value = defineModel('value');
const props = defineProps({id: String, name: String, required: Boolean, options: Array});
</script>
<script>
import {setChecked, setRequired} from "@/js/fields";

export default {
  name: "RadioField",
  mounted() {
    setRequired(this.id, this.required);
    setChecked(this.id, this.value);
  }
}
</script>