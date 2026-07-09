<script setup>
import { ref } from "vue"

const props = defineProps({
  editMode: Boolean,
  habit: Object
})

const emit = defineEmits(["save","create","cancel"])

const form = ref({
  id: props.habit?.id,
  name: props.habit?.name || "",
  description: props.habit?.description || "",
  is_complete: props.habit?.is_complete || false
})

function submit() {
  if(props.editMode){
    emit("save", form.value)
  }
  else{
    emit("create", form.value)
  }  
}

function cancel(){
  emit('cancel')
}

</script>

<template>
  <form @submit.prevent="submit">
    <input
      v-model="form.name"
      placeholder="Habit name"
    />

    <input
      v-model="form.description"
      placeholder="Description"
    />

    <button type="submit">
      {{ editMode ? "Update Habit" : "Add Habit" }}
    </button>
    <button @click="cancel" type="button">Cancel</button>
  </form>
</template>