<template>

  <div id="sidebarCalc">
    <header>
      <!-- <img class="image" src="../assets/cb.png"> -->
    </header>
    <ul class="nav">
      <li>
        <a href="#">
          <i class="zmdi zmdi-view-dashboard">Calculadora de viagens</i>
        </a>
      </li>
    </ul>
  </div>
 
</template>

<script>
export default {
	name: 'Sidebar',
}
</script>

<style scoped lang="scss">	

.image{
  width: 200px;
  height: 33px;
  margin: 20px auto;
  display: block;
}


/* Sidebar Styles */

#sidebarCalc {
  z-index: 1000;
  position: fixed;
//   left: 250px;
  width: 250px;
  height: 100%;
//   margin-left: -250px;
  overflow-y: auto;
  background: #37474F;
  box-shadow: 4px 4px 4px 2px rgba(0, 0, 0, 0.2);
}


#sidebarCalc .nav{
//   position: absolute;
  padding-left: 20px;

}

#sidebarCalc .nav a{
  background: black;
  border-bottom: 1px solid #455A64;
  color: #CFD8DC;
  font-size: 14px;
  padding: 16px 24px;
}

#sidebarCalc .nav a:hover{
  background: none;
  color: #ECEFF1;
}

</style>