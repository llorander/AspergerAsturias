<template>
  <div class="admin-panel">
    <section>
      <article class="user-list-box">
        <router-link class="user" to="">
          <figure>
            <img src="" alt="" />
          </figure>
          <p>Nombre Usuario</p>
        </router-link>
        <router-link class="user" to="">
          <figure>
            <img src="" alt="" />
          </figure>
          <p>Nombre Usuario</p>
        </router-link>
      </article>
    </section>
    <section>
      <!-- <article class="new-user-box">
        <router-link class="new-user-button" to="">Nuevo Usuario</router-link>
        <router-link class="link-user-button" to="#">Enlazar Usuario</router-link>
      </article> -->
      <article class="user-management-box">
        <router-link class="planning-button" to="/admin-planning"
          >Planificación</router-link
        >
        <router-link class="completed-tasks-button" to="/admin-completed-tasks"
          >Tareas Completadas</router-link
        >
        <router-link class="points-button" to="/admin-total-points"
          >Puntos</router-link
        >
      </article>
    </section>
  </div>
</template>

<style scoped>
section {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 15px 0;
}
.user-list-box {
  background: #fff;
  height: 180px;
  width: 290px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 15px;
  border: 2px solid #515459;
  color: #515459;
}

.user-list-box .user {
  border: 2px solid #515459;
  width: 266px;
  display: flex;
  padding: 4px 7px;
  border-radius: 15px;
}

.user-list-box p {
  margin-top: 12px;
  margin-left: 29px;
}

figure {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  background-color: #78bfa5;
}

.user-list-box a:not(:last-child) {
  margin-bottom: 12px;
}

.new-user-box {
  background: #fff;
  height: 345px;
  width: 290px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 15px;
  border: 2px solid #515459;
}

.new-user-button {
  margin-bottom: 40px;
  border: solid 2px #82d9b9;
  background: #78bfa5;
}

.link-user-button {
  background: #aa6666;
  border: solid 2px #f28d77;
}

.planning-button {
  margin-bottom: 40px;
  border: solid 2px #82d9b9;
  background: #78bfa5;
}

.completed-tasks-button {
  background: #aa6666;
  margin-bottom: 40px;
  border: solid 2px #f28d77;
}

.points-button {
  border: solid 2px #82d9b9;
  background: #78bfa5;
}

.new-user-box a,
.user-management-box a {
  display: block;
  text-align: center;
  padding: 16px 5px;
  border-radius: 15px;
  width: 266px;
  color: #fff;
  font-size: 1rem;
}

.user-management-box {
  background: #fff;
  height: 345px;
  width: 290px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 15px;
  border: 2px solid #515459;
  color: #fff;
}
</style>
