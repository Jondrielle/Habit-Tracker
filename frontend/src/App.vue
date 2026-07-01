<script setup>
import {ref,onMounted} from 'vue'

import HabitItem from "./components/HabitItem.vue"

import HabitForm from "./components/HabitForm.vue"


const habits = ref([])

const name = ref("")
const description = ref("")
const id = ref(0)
const isComplete = ref(false)
const streak = ref(0)
const lastCompletion = ref("")

const isEditing = (true)

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

async function addHabit(){
  if (!name.value.trim()) return

  try{
    const response = await fetch(`http://127.0.0.1:8000/habit`,{
      method:"POST",
      headers:{
        "Content-Type":
        "application/json"
      },
      body: JSON.stringify({
        name:name.value,
        description:description.value
      })
    });

    if(!response.ok){
      throw new Error(`Response status: ${response.status}`)
    }

    const result = await response.json()

    habits.value.push(result)

    name.value = ""
    description.value = ""
  
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

    console.log("Task was deleted")
  }catch(error){
    console.error(error.message)
  }
}

async function handleUpdate(id){
  try{
    const response = await fetch(`http://127.0.0.1:8000/habits/${id}`,{
      method:"PATCH",
      headers:{
        "Content-Type":
          "application/json"
      },
      body: JSON.stringify({
        name: name.value,
        description: description.value,
      })
    })

    name.value = ""
    description.value = ""
    const updatedHabit = await response.json()

    if(!response.ok){
      throw new Error (`Response: ${response.status}`)
    }

    const index = habits.value.findIndex(habit => habit.id === id)

    if(index !== -1){
      habits.value[index] = updatedHabit
    }

    
  }catch(error){
    console.error(error.message)
  }
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
      @update="handleUpdate"
      />
    </div>
  </div>

  <input v-model="name" placeholder="Name"/>
  <input v-model="description" placeholder="Description"/>

  <button @click="addHabit">
    Add Habit
  </button>
  <HabitForm
    :editMode ="isEditing"/>
</template>

<style scoped></style>
