<template>
	<div class="window row">
		<div class="col-sm-2">
			<Sidebar/>
		</div>
		<div class="col-sm-10">
			<Search/>
		</div>
	</div>
</template>



<script>
	import Search from '@/components/Search.vue'
	import Sidebar from '@/components/Sidebar.vue'

	export default {
		name: 'TravelCalculator',
		components: {
			Search,
			Sidebar
		}
	}

</script>

<style scoped lang="scss">
	
	
	
</style>