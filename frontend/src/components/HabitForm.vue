<script setup>
import { ref } from "vue"

const props = defineProps({
  editMode: Boolean,
  habit: Object
})

const emit = defineEmits(["save"])

const form = ref({
  name: props.habit?.name || "",
  description: props.habit?.description || ""
})

function submit() {
  emit("save", form.value)
}
</script>

<template>
  <form @submit.prevent="submit">
    <input v-model="form.name" placeholder="Name" />

    <input 
      v-model="form.description"
      placeholder="Description"
    />

    <button type="submit">
      {{ editMode ? "Update Habit" : "Add Habit" }}
    </button>
  </form>
</template>