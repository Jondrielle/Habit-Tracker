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
        body: JSON.stringify({
          name: habit.name,
          description: habit.description
        })
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

async function handleComplete(id){
  try{
    const response = await fetch(`http://127.0.0.1:8000/habits/${id}`, {
      method:"PATCH",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify({
        is_complete: true
      })
    })

    if(!response.ok){
      throw new Error(`Response status: ${response.status}`)
    }

    const updatedHabit = await response.json()

    const index = habits.value.findIndex(h => h.id === id)

    if(index !== -1){
      habits.value[index] = updatedHabit
    }

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
  <div class="titleBox">
    <h1 class="header">Habits</h1>
  </div>
  <div class="habit-grid"> 
    <HabitItem 
      v-for="habit in habits"
      :key="habit.id"
      :habit="habit"
      @delete="handleDelete"
      @edit="startEdit"
      @complete="handleComplete"
    />
  </div>

  <HabitForm
    :key="selectedHabit?.id || 'new'"
    :habit="selectedHabit"
    :editMode ="isEditing"
    @save="handleUpdate" @create="addHabit"
    @cancel="cancelForm"
  />
</template>

<style >
  body {
    margin: 0;
  }
  .titleBox {
    width: 100%;
    box-sizing: border-box;
    background: linear-gradient(135deg, #ffd6e7, #ffc0cb);
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(255, 192, 203, 0.4);
  }

  .header{
    margin: 0;
    text-align: center;
  }

  .habit-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
    max-width: 1100px;
    margin: 0 auto;
  }

  @media (max-width: 900px){
    .habit-grid{
      grid-template-columns:repeat(2, 1fr);
    }
  }

  @media (max-width: 600px){
    .habit-grid{
      grid-template-columns:1fr;
    }
  }


</style>
