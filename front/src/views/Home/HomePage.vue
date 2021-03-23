<template>
  <div class="home-page">
    <article class="home-page-box">
      <router-link class="login-button" to="/login-page">Login</router-link>
      <router-link class="register-button" to="/registration-page">Registro</router-link>
    </article>
  </div>
</template>

<script>

export default {
  name: "Home",
  data() {
    return {

    };
  },
};
</script>

<style scoped>   
  .register-button {
      background: #AA6666;
      border: solid 2px #F28D77;
  }

  .home-page {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  .home-page-box {
    background: #fff;
    height: 336px;
    width: 245px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-radius: 15px;
    border: 2px solid #515459;
  }

  .login-button, .register-button {
    display: block;
    text-align: center;
    padding: 16px 5px;
    border-radius: 15px;
    width: 179px;
    color: #fff;
    font-size: 1rem;
  }

  .login-button {
    margin-bottom: 45px;
    border: solid 2px #82D9B9;
    background: #78BFA5;
  }

  .register-button {
      background: #AA6666;
      border: solid 2px #F28D77;
  }
</style>
