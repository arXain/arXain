<!-- App.vue (parent app) -->
<template>
	<div class="container">
		<web3-box/>
	</div>
</template>

<script>
import Web3Box from '../components/Web3Box.vue'
export default {
			components: {Web3Box}, //Register other components
		}
</script>

<style scoped>
</style>

