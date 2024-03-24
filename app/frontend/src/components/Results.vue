<template>
	<div v-if="routes.length != 0" class="all">
		<span class="mensage">Estas são as melhores alternaticas de viagem para a data selecionada</span>
		<div v-for="route in routes" :key="route.id" class="allIn">
			<div class="detail">
				<div class="ticket">
					<div class="icon">
						<span class="material-icons">
							volunteer_activism
						</span>
					</div>
					<div class="content">
						<span class="topic">{{ route.name }}</span>
						<span>Poltrona: {{ route.bed }}</span>
						<span>Tempo: {{ route.duration }}</span>
					</div>
				</div>

				<div class="price">
					<span class="topic">Preço:</span>
					<span>{{ route.price_confort }}</span>
				</div>
			</div>
		</div>
	</div>
	<span v-else class="mensage">
		Nenhum dado selecionado
	</span>

</template>

<script>
export default {
	name: 'Results',
	props: {
		routes: {
			type: Object,
			default: () => {
				return [];
			}
		}
	},
};

</script>

<style scoped lang="scss">
.all {
	height: 100%;
	width: 100%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
}

.all .mensage {
	margin-left: 4%;
	margin-right: 35%;

}

.allIn {
	height: 20%;
	width: 100%;
	margin-bottom: 1%;
}


.mensage {
	display: flex;
	font-size: 20px;
	margin-left: auto;
	margin-right: auto;
}

.detail {
	height: 100%;
	width: 90%;
	margin-left: 4%;
	margin-bottom: 2%;
	background: none;
	display: flex;
	flex-direction: row;
	// justify-content: space-between;
	align-items: center;
}

.ticket {
	height: 100%;
	width: 67%;
	background: #e4dcdd;
	display: flex;
	justify-content: center;
	align-items: center;
	border-radius: 10px;
}

.icon {
	height: 100%;
	width: 20%;
	background: #0792d8;
	border-top-left-radius: 10px;
	border-bottom-left-radius: 10px;
	display: flex;
	align-items: center;
}

.material-icons {
	font-size: 250%;
	margin-left: auto;
	margin-right: auto;
	color: whitesmoke;
}

.content {
	height: 100%;
	width: 80%;
	// background: #e4dcdd;
	background: none;
	flex-direction: column;
	display: flex;
	justify-content: center;
	padding-left: 10%;
}

.content span {
	align-items: start;
}

.topic {
	font-weight: bold;
	font-size: 120%;
}

.price {
	margin-left: 2%;
	height: 100%;
	width: 31%;
	display: block;
	background: #e4dcdd;
	display: flex;
	justify-content: center;
	border-radius: 10px;
	flex-direction: column;
	padding-left: 10%;
}
</style>