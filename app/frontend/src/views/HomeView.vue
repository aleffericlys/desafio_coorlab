<template>
	<div class="background-div">

		<div class=" subdiv1">
			<Sidebar />
		</div>
		<div class="subdiv2">
			<div id="topdiv">

			</div>
			<Calculator/>
		</div>


	</div>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue'
import Calculator from '@/components/Calculator.vue'

export default {
	name: 'HomeView',
	components: {
		Sidebar,
		Calculator,
	}
}
</script>

<style scoped lang="scss">
.subdiv2 {
	position: fixed;
	margin-left: 20%;
	width: 80%;
	height: 100%;
	background-color: none;
	display: flex;
	justify-content: center;
	align-items: center;
}

#topdiv {
	width: 100%;
	height: 50px;
	background-color: none;
	box-shadow: 4px 0px 4px 2px rgba(0, 0, 0, 0.5);
	position: absolute;
	top: 0;
	left: 0;
}
</style>