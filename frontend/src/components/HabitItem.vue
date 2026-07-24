<script setup>
const props = defineProps({
	habit: Object
})

const emit = defineEmits(['delete','edit','complete'])

function deleteHabit(){
	emit('delete',props.habit.id)
	console.log("Deleting habit")
}

function updateHabit(){
	emit('edit', props.habit)
	console.log("Updating habit")
}

function completeHabit(){
	console.log("Completing:", props.habit)
	emit('complete',props.habit.id)
}
</script>

<template>
<div class="card">
	<div class="title">
		<h2>{{habit.name}}</h2>
	</div>
	<h2 class="description">{{habit.description}}</h2>
	<div class="stats">
		<span class="streak">🔥  {{habit.streak}} day streak</span>
		<span class="stats">📅 {{habit.last_completed}}</span>
		<span class="stats">Status: {{habit.is_complete ? " ✅ Complete" : "⬜Incomplete"}}</span>
	</div>
	<div class="buttons">
		<button @click="deleteHabit">Delete Habit</button>

		<button @click="updateHabit">Open Edit</button>

		<button @click="completeHabit">
    		{{ habit.is_complete ? "Completed" : "Mark Complete" }}
  		</button>
	</div>
</div>
</template>

<style scoped>
	.card {
	  width: 320px;
	  display: flex;
	  flex-direction: column;
	  gap: 8px;
	  border-bottom: 2px dotted pink;
  	  box-shadow: 0 6px 8px -6px rgba(0,0,0,0.2);
	  border-radius: 8px;
	  padding: 12px;
	  position:relative;
	  min-height:220px;
	}

	.title{
	  margin:0;
	  text-transform:uppercase;
	  font-size:1.2rem;
	  margin-right:80px;
	}

	.buttons{
		display: flex;
		justify-content: flex-end;
		gap:8px;
	}

	.stats{
	  display:flex;
	  flex-wrap:wrap;
	  gap:12px;
	  font-size:14px;
	  padding:5px;
	}

	.streak{
		position:absolute;
		top:25px;
		right:10px;
	}

	.description{
		padding-left: 12px;
  		border-left: 3px solid pink;
  		font-style: italic;
  	}
</style>