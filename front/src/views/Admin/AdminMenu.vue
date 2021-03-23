<template>
  <div class="user-menu">
    <div class="info-menuusuarios">
        <div class="usuario-menuusuarios">
            <div class="icon-menusuarios">
            </div>
            <p>Nombre de usuario</p>
        </div>
        <div class="opciones-menuusuarios">
            <router-link class="link" to="/admin-total-points">Puntos Totales</router-link>
            <router-link class="link" to="/add-reward">Añadir Recompensa</router-link>
            <router-link class="link" to="/admin-rewards-list">Listado de Recompensas</router-link>
        </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
    .user-menu {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    div.info-menuusuarios {
  padding: 20px 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 300px;
}

div.usuario-menuusuarios {
  background-color: white;
  width: 300px;
  border-radius: 15px;
  border: 2px solid #515459;
  padding: 5px 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

div.icon-menusuarios {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #78BFA5;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 15px;
}

.usuario-menuusuarios p {
  color:#515459;
  width: 85%;
  text-align: center;
}

.opciones-menuusuarios {
  background-color: white;
  padding: 60px 5px;
  width: 300px;
  border-radius: 15px;
  border: 2px solid #515459;
  display: flex;
  flex-direction: column;
  justify-content: center;
align-items: center;
}

.opciones-menuusuarios .link {
  text-decoration: none;
  display: block;
  text-align: center;
  margin: 10px 0;
  padding: 16px 5px;
  border-radius: 15px;
  width: 250px;
  font-size: 18px;
  background-color: #78BFA5;
  color: #fff;
}

.opciones-menuusuarios .link:nth-child(2) {
  background: #AA6666;
} 
</style>