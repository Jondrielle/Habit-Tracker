<script setup>
const props = defineProps({
	habit: Object
})

const emit = defineEmits(['delete','update'])

function deleteHabit(){
	emit('delete',props.habit.id)
	console.log("Deleting habit")
}

function updateHabit(){
	emit('update', props.habit.id)
	console.log("Updating habit")
}
</script>

<template>
<div class="card">
	<div class="title">
		<h2 >Habit: {{habit.name}}</h2>
	</div>
	<h2>Description: {{habit.description}}</h2>
	<h2>Streak: {{habit.streak}}</h2>
	<h2>Last Completed: {{habit.last_completed}}</h2>
	<h2>Is Complete: {{habit.is_complete}}</h2>
	<div class="buttons">
		<button @click="deleteHabit">Delete Habit</button>
		<button @click="updateHabit">Update Habit</button>
	</div>
</div>
</template>

<style scoped>
	.card{
		display: flex;
		grid-row: 2;
		gap: 12px;
	}

	.title{
		display: flex;
		flex-direction:
	}

	.buttons{
	
	}
</style>