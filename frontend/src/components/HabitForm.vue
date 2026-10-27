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
    <h2>Create a new habit</h2>
    <p>Start small. Stay consistent</p>
    <form class="form" @submit.prevent="submit">
      <label>Habit name</label>
      <input
        v-model="form.name"
        placeholder="e.g. Read for 15 minutes"
      />

      <label>Description (optional)</label>
      <textarea
        v-model="form.description"
        placeholder="What do you want to achieve?"
      />

      <div class="button-row">

        <button type="submit">
          {{ editMode ? "Update Habit" : "+ Add Habit" }}
        </button>

        <button type="button" @click="cancel">
          Cancel
        </button>

      </div>
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

.button-row{
  display:flex;
  justify-content:flex-end;
  align-items:center;
  gap:10px;
}

.button-row > button{
  width:125px;
  height:30px;
  border-radius:10px;
  background-color:#FFC0CB;
}

.button-row > button:hover{
  background-color:#F9629F;
  opacity: 0.88;
}


</style>