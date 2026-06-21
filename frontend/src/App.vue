<script setup>
import {ref,onMounted} from 'vue'

const habits = ref([])

const name = ref("")
const description = ref("")

async function getHabitList(){
  try{
    const response = await fetch("http://127.0.0.1:8000/");

    if (!response.ok){
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    
    console.log(result)
  }catch(error){
    console.error(error.message)
  }
}

async function addHabit(){
  console.log(name.value)
  console.log(description.value)
}

onMounted(()=>{
  habits = getHabitList()}
)
</script>

<template>
  <input v-model="name" placeholder="Name"/>
  <input v-model="description" placeholder="Description"/>

  <button @click="addHabit" :name>
    Add Habit
  </button>
</template>

<style scoped></style>
