<template>
	<div class="searItens">
		<div class="imputs">
			<div class="title"><span class="material-icons">
					volunteer_activism
				</span> Calcule o Valor da Viagem</div>
			<div class="selectT">
				<p class="">Destino</p>
				<select @change="verify()" class="select" value="Select your destination" v-model="selectedCity">
					<option value="">Selecione a cidade de destino</option>
					<option v-for="city in cities" :key="city">{{ city }}</option>
				</select>
			</div>
			<div class="dataD">
				<p class="data">Data</p>
				<input @change="verify()" class="select" type="date" v-model="selectedDate"/>
			</div>
			
			<AlertModal
			@searchRoutes="searchRoutes"
			:showModal="showModal"
			/>
		</div>
	</div>
</template>

<script>
import { defineComponent } from 'vue';
import AlertModal from '@/components/AlertModal.vue'

export default defineComponent({
	name: 'Search',
	components: {
		AlertModal
	},
	emits: ['showRoutes'],
	data() {
		return {
			api: 'http://127.0.0.1:3000/',
			selectedDate: "",
			selectedCity: "",
			showModal: true,
			cities: [],
			routes: [],
		};
	},
	methods: {
		async searchRoutes() {
			if (this.selectedCity === "" || this.selectedDate === "") {
				this.routes = [];
			} else {
				await fetch(this.api + 'transport/' + this.selectedCity)
					.then(response => response.json())
					.then(json => this.routes = json);
					
				this.$emit('showRoutes', this.routes);
			}
		},
		verify() {
			if (this.selectedCity === "" || this.selectedDate === "") {
				this.showModal = true;
			} else {
				this.showModal = false;
			}
		}

	},
	mounted() {
		fetch(this.api + 'transport_cityes')
			.then(response => response.json())
			.then(json => this.cities = json);
	},
});

</script>

<style scoped lang="scss">
.searItens {
	height: 90%;
	width: 90%;
	background: #e4dcdd;
	display: flex;
	justify-content: center;
	align-items: center;
	border-radius: 3%;
}

.imputs {
	margin-left: auto;
	margin-right: auto;
	height: 85%;
	width: 90%;
	display: flex;
	background: none;
	display: flex;
	flex-direction: column;
	justify-content: space-evenly;
}

.selectT,
.dataD {
	flex-direction: column;
	width: 100%;
	align-content: center;
	display: flex;
}

.imputs p {
	align-self: self-start;
	font-size: 100%;
	margin-bottom: 0px;
}

.material-icons {
	font-size: 170%;
	padding-right: 10px;
}

.select {
	height: 40px;
	width: 100%;
	border-radius: 5px;
}

.title {
	font-size: 140%;
	font-weight: bold;
	display: flex;
	align-items: center;
	justify-content: center;
}
</style>
