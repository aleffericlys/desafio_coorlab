<template>
	<!-- <div class="row">
		<div class=" teste ">
			<Sidebar/>
		</div>
		
	
		<div class="home">
			<img alt="Vue logo" src="../assets/logo.png">
			<HelloWorld msg="Welcome to Your Vue.js App pata testesaaaaaaaaaaaa"/>
			
		</div>
	</div> -->
	<div class="background-div">

		<div class="subdiv1">
			<Sidebar/>
		</div>
		<div class="subdiv2">
			<div id="topdiv">
				
			</div>
			<div id="subsubdiv">
				<div id="calculatorDiv">
					<span class="material-icons">
						local_shipping
					</span>
					Calculadora de viagem
				</div>
				<div class="inputs">
					<Search/>
				</div>
				<div class="results">
					results
				</div>
			</div>
		</div>


	</div>

</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Sidebar from '@/components/Sidebar.vue'
import Search from '@/components/Search.vue'
	

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
	Sidebar,
	Search
  }
}
</script>


<style scoped lang="scss">

	html, body {
        margin: 0;
        padding: 0;
        height: 100%;
    }

    .background-div {
        position: fixed;
        width: 100%;
        height: 100%;
        background-color: #f5f5f5;
    }
	.subdiv2 {
		position: fixed;
		margin-left: 20%;
		width: 80%;
		height: 100%;
		background-color: none;
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
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
	#calculatorDiv {
		width: 100%;
		height: 10%;
		background-color: #323e44;
		position: absolute;
		top: 0;
		color: whitesmoke;
		display: flex;
		align-items: center;
		padding: 10px;
		font-size: 20px;
	}

	.material-icons {
		font-size: 40px;
		padding-right: 10px;
	}

	#subsubdiv {
		width: 90%;
		height: 70%;
		background-color: none;
		display: flex;
		justify-content: center;
		align-items: center;
		box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.5);
		position: relative;
	}

	.inputs {
		margin-top: 5%;
		margin-left: -10%;
		height: 85%;
		width: 30%;
		display: flex;
		background: rgb(228, 220, 221);
		border-radius: 2%;
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		
	}
	.results {
		margin-top: 5%;
		margin-left: 10px;
		height: 85%;
		width: 55%;
		display: flex;
		background: none;
		
	}
</style>