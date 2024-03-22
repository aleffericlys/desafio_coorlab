
<template>
	<div class="row">
		<div class=" teste col-sm-3">
			<Sidebar/>
		</div>
		<div class="col-sm-9">
			
			<!-- <HelloWorld/> -->
			<!-- <router-view/> -->
		</div>
	</div>
</template>

<script>
	import Sidebar from '@/components/Sidebar.vue'
	import HelloWorld from '@/components/HelloWorld.vue'
	export default {
		name: 'App',
		components: {
			Sidebar,
			HelloWorld
		}
	}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.teste {
  background-color: #090e13;

}
nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
