<template>
  <div class="registration">
    <form action="" method="POST" class="form-registrousuarios">
        <input type="text" name="name" placeholder="Usuario">
        <input type="email" name="email" placeholder="Email">
        <input type="password" name="password" placeholder="Contraseña">
        <input type="password" name="passwordconfirm" placeholder="Confirmas contraseña">
        <input class="submit-registrousuarios" type="submit" value="Registro">
    </form>
  </div>
</template>

<script>
export default {

}
</script>

<style>
    .registration {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .form-registrousuarios {
        background-color: white;
        padding: 50px 10px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 300px;
        border-radius: 15px;
        border: 2px solid #515459;
    }

    .form-registrousuarios input {
        display: block;
        text-align: center;
        padding: 16px 5px;
        margin-bottom: 10px;
        border-radius: 15px;
        border: 2px solid #515459;
        color: #515459;
        width: 200px;
        font-size: 18px;
    }

    input.submit-registrousuarios {
        background: #AA6666;
        border: 2px solid #AA6666;
        color: #fff;
    }
</style>