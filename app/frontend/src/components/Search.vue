<template>
	<div class="imputs">
	  <select v-model="selectedCity">
		<option disabled value="">Select a item</option>
		<option v-for="city in cities" :key="city">{{ city }}</option>
	  </select>
	  <input type="date" v-model="selectedDate"/>
	  <button class="btn btn-primary" @click="searchRoutes">Search</button>
	</div>
	<div v-if="routes">
		<div v-for="route in routes" :key="route.id">
			<p>{{ route.name }}</p>
			<p>{{ route.duration }}</p>
			<p>{{ route.seat }}</p>
			<p>{{ route.price_confort }}</p>
		</div>
	</div>
  </template>
  
  <script>
  export default {
	name: 'Search',
	
	data() {
	  return {
		api: 'http://127.0.0.1:3000/',
		selectedDate: null,
		selectedCity: null,
		cities: [],
		routes: []
	  };
	},
	methods: {
	  searchRoutes() {
		fetch(this.api+'transport/'+this.selectedCity)
		.then(response => response.json())
		.then(json => this.routes = json);
	  }
	},
	mounted() {
	  fetch(this.api + 'transport_cityes')
	  .then(response => response.json())
	  .then(json => this.cities = json);
	},
  };
  </script>

<style scoped lang="scss">
	
</style>