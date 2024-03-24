<template>
	<div class="calculator">
		<div class="calcHeader">
			<span class="material-icons">
				local_shipping
			</span> Calculadora de viagem
		</div>
		<div class="calcBody">
			<div class="search">
				<Search 
					@showRoutes="showRoutes"
				/>
			</div>

			<div class="results">
				<Results 
					:routes="routes"
					@clear="clear"
				/>
			</div>

		</div>

	</div>
</template>

<script>
import Search from '@/components/Search.vue'
import Results from '@/components/Results.vue'

export default {
	name: 'Calculator',
	components: {
		Search,
		Results,
	},
	data() {
		return {
			routes:	[],
		}
	},
	methods: {
		showRoutes(routes) {
			this.routes = routes;
		},
		clear() {
			this.routes = [];
		}
	}
}
</script>

<style scoped lang="scss">
.calculator {
	/* margin-left: auto;
			margin-right: auto; */
	width: 90%;
	height: 70%;
	background: none;
	box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.5);
}

.calcHeader {
	height: 10%;
	background: #323e44;
	color: whitesmoke;
	display: flex;
	align-items: center;
	padding-left: 3%;
	font-weight: bold;
	font-size: 100%;
}

.calcHeader .material-icons {
	font-size: 180%;
}

.calcBody {
	height: 90%;
	background: whitesmoke;
	display: flex;
	flex-direction: row;
}

.search {
	height: 100%;
	width: 35%;
	background: none;
	display: flex;
	justify-content: center;
	align-items: center;
}

.results {
	height: 100%;
	width: 65%;
	background: none;
	display: flex;
	flex-direction: column;
	// align-items: center;
	justify-content: center;
}
</style>