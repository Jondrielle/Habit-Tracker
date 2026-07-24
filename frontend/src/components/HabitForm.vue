<script setup>
import { ref } from "vue"

const props = defineProps({
  editMode: Boolean,
  habit: Object
})

const emit = defineEmits(["save", "create", "cancel"])

const form = ref({
  id: props.habit?.id,
  name: props.habit?.name || "",
  description: props.habit?.description || ""
})

function submit() {
  if (props.editMode) {
    emit("save", form.value)

  } else {
    emit("create", form.value)
  }

  if(!props.editMode){
    form.value.name = ""
    form.value.description = ""
  }

}

function cancel() {
  emit("cancel")
}
</script>

<template>
  <div class="container">
    <form class="form" @submit.prevent="submit">
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

      <button type="button" @click="cancel">
        Cancel
      </button>
    </form>
  </div>
</template>

<style scoped>
.form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.container {
  width: 350px;
  margin: 20px auto;
  border: 1px solid pink;
  border-radius: 12px;
  padding: 16px;
  background-color: #fff0f5;
  margin-top:45px;
}

</style>