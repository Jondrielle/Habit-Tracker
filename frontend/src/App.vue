<script setup>
import {ref,onMounted} from 'vue'

const habits = ref([])

const name = ref("")
const description = ref("")

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

    console.log(`${result.name} was added`)
  
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
  </div>

  <input v-model="name" placeholder="Name"/>
  <input v-model="description" placeholder="Description"/>

  <button @click="addHabit">
    Add Habit
  </button>
</template>

<style scoped></style>
