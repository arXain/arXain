<!-- App.vue (parent app) -->
<template>
	<div id="app">
		<navbar-component></navbar-component>
	</div>
</template>

<script>
import NavbarComponent from '../components/NavbarComponent.vue'
export default {
			name: 'app',
			components: {NavbarComponent}, //Register other components
		}
</script>

<style scoped>
</style>

