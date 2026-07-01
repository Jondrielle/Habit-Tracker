<script setup>
	const props = defineProps({
		editMode: Boolean
	})
</script>

<template>
	<div>
		<div v-if="editMode">
			<h2>Edit Habit Form</h2>
			<button >
		    Edit Habit
		  </button>
		</div>
		<div v-else>
			<h2>Add Habit Form</h2>
			<input v-model="name" placeholder="Name"/>
  			<input v-model="description" placeholder="Description"/>
			<button>
				Add Habit
			</button>
		</div>
	  </div>
</template>