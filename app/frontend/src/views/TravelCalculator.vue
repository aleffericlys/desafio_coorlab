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
import { StringDecoder } from 'string_decoder';
	export default {
		name: 'TravelCalculator',
		components: {
			Search,
			Sidebar
		}
	}

</script>

<style scoped lang="scss">
	
	.sidebar {
	display: flex;
	position: fixed;
	top: 0;
	bottom: 0;
	left: 0;
	padding: 58px 0 0; /* Height of navbar */
	box-shadow: 0 2px 5px 0 rgb(0 0 0 / 5%), 0 2px 10px 0 rgb(0 0 0 / 5%);
	width: 240px;
	z-index: 600;
	}
</style>