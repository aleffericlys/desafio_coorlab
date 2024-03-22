<template>
	<div class="row">
		<div class=" teste col-sm-2">
			<!-- <Sidebar/> -->
		</div>
		
	
		<div class="home col-sm-10">
			<img alt="Vue logo" src="../assets/logo.png">
			<!-- <HelloWorld msg="Welcome to Your Vue.js App pata testesaaaaaaaaaaaa"/> -->
		</div>
	</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Sidebar from '@/components/Sidebar.vue'
	

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
	Sidebar
  }
}
</script>


<style scoped lang="scss">
	.teste {
		background-color: #f8f9fa;
		padding: 0;
		margin: 0;
	}
</style>