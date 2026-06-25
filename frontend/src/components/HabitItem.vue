<script setup>
const props = defineProps({
	habit: Object
})
</script>

<template>
<h2>{{habit.name}}</h2>
<h2>{{habit.description}}</h2>
<h2>{{habit.streak}}</h2>
<h2>{{habit.last_completed}}</h2>
<h2>{{habit.is_complete}}</h2>
</template>