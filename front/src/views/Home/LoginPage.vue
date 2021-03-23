<template>
    <div class="login-page">
        <article class="login-page-box">
            <form action="/action_page.php">
                <input class="login-page-email" type="email" id="fname" name="firstname" placeholder="Correo">
            
                <input class="login-page-password" type="password" id="lname" name="lastname" placeholder="Contraseña">
                
                <input class="login-page-login" type="submit" value="Login">

                <router-link class="login-page-recover" to="/registration">Recuperar Contraseña</router-link>
            </form>
        </article>
    </div>
</template>

<script>
export default {

}
</script>

<style>
    .login-page {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .login-page-box {
        background: #fff;
        height: 547px;
        width: 304px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        border: 2px solid #515459;
    }

    .login-page-box input {
        display: block;
        font-size: 1rem;
        padding: 16px 5px;
        border-radius: 15px;
        width: 252px;
        text-align: center;
        margin-bottom: 11px;
    }

    .login-page-recover {
        display: block;
        text-align: center;
        padding: 16px 5px;
    }

    ::placeholder, .login-page-recover {
        color: #78BFA5;
    }

    .login-page-email, .login-page-password, .login-page-login {
        border: 2px solid #82D9B9;
    }

    .login-page-login {
        background: #78BFA5;
        color: #fff;
    }
</style>