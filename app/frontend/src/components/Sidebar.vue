<template>

  <div id="sidebarCalc">
	
	<header class="header">
		<img class="image" src="../assets/cb.png">
	</header>


	<a href="#">
	<div class="nav">
			<span class="material-icons">
				calculate
			</span>
			
			Calculadora de viagens
		</div>
		</a>
		
	
  </div>
 
</template>

<script>
export default {
	name: 'Sidebar',
}
</script>

<style scoped lang="scss">	
.header{
	border-bottom: #37474F 1px solid;
	width: 100%;
	display: flex;
	justify-content: center;
}

.image{
  width: 200px;
  height: 33px;
  margin-top: 20px;
  display: block;
}


/* Sidebar Styles */

#sidebarCalc {
  position: fixed;
  width: 20%;
  height: 100%;
  background: #323e44;
  box-shadow: 4px 0px 4px 2px rgba(0, 0, 0, 0.2);
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  
}


#sidebarCalc a{
	margin-top: 20px;
	display: flex;
	// justify-content: center;
	align-items: center;
	width: 100%;
	text-decoration: none;
}

.zmdi{
  font-size: 14px;
}

#sidebarCalc a .nav{
width: 100%;
  background: none;
  border-bottom: 1px solid #455A64;
  color: #CFD8DC;
  font-size: 20px;
  padding: 16px;
  display: flex;
  align-items: center;
 
}

.material-icons{
padding-right: 10px;
  font-size: 25px;
  color: #CFD8DC;
  
}

#sidebarCalc a .nav:hover{
  background: none;
  color: #ECEFF1;
}

</style>