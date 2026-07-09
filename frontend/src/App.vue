<script setup>
import {ref,onMounted} from 'vue'

import HabitItem from "./components/HabitItem.vue"

import HabitForm from "./components/HabitForm.vue"


const habits = ref([])


const isEditing = ref(false)
const selectedHabit = ref(null)

async function getHabit(){
  try{
    const response = await fetch("http://127.0.0.1:8000/");

    if (!response.ok){
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    
    habits.value = result 
    console.log(result)
  }catch(error){
    console.error(error.message)
  }
}

async function addHabit(habit){
  try{
    const response = await fetch("http://127.0.0.1:8000/habit", {
      method: "POST",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify({
        name: habit.name,
        description: habit.description
      })
    })

    if(!response.ok){
      throw new Error(`Response status: ${response.status}`)
    }

    const result = await response.json()

    habits.value.push(result)

  }catch(error){
    console.error(error.message)
  }
}

async function handleDelete(id){
  try{
    const response = await fetch(`http://127.0.0.1:8000/habit/${id}`,{
      method:"DELETE",
    })

    if(!response.ok){
      throw new Error(`Response status: ${response.status}`)
    }

    const result = await response.json()

    habits.value = habits.value.filter(habit => habit.id !== id)

    if(selectedHabit.value?.id === id){
      selectedHabit.value = null
      isEditing.value = false
    }
    
    console.log("Task was deleted")
  }catch(error){
    console.error(error.message)
  }
}

async function handleUpdate(habit){
  try{
    const response = await fetch(`http://127.0.0.1:8000/habits/${habit.id}`,{
      method:"PATCH",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify(habit)
    })

    console.log(habit)
    if(!response.ok){
      throw new Error(`Response: ${response.status}`)
    }

    const updatedHabit = await response.json()

    const index = habits.value.findIndex(h => h.id === habit.id)

    if(index !== -1){
      habits.value[index] = updatedHabit
    }

    isEditing.value = false
    selectedHabit.value = null

  }catch(error){
    console.error(error.message)
  }
}

function startEdit(habit){
  selectedHabit.value = {...habit}
  isEditing.value = true
}

function cancelForm(){
  selectedHabit.value = null
  isEditing.value = false
}

onMounted(()=>{
  getHabit()
})
</script>

<template>
  <h1>----Habits----</h1>
  <div v-for="habit in habits" :key="habit.id">
    <div>
      <HabitItem :habit="habit"
      @delete="handleDelete"
      @edit="startEdit"
      />
    </div>
  </div>

  <HabitForm
    :key="selectedHabit?.id || 'new'"
    :habit="selectedHabit"
    :editMode ="isEditing"
    @save="handleUpdate" @create="addHabit"
    @cancel="cancelForm"
  />
</template>

<style scoped></style>
