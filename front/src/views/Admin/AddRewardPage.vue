<template>
    <div class="add-reward">
      <div class="info-menuusuarios">
                <div class="usuario-menuusuarios">
                    <div class="icon-menusuarios">
                        <i class="fas fa-user"></i>
                    </div>
                    <p>Nombre de usuario</p>
                </div>
                  <form action="" method="POST" class="form-registrotareas">
                    <label for="tarea">Título de la tarea:</label>
                    <input type="text" name="tarea">
                    <label for="descricion">Descripción de la tarea:</label>
                    <textarea name="descripion" cols="30" rows="4"></textarea>
                    <label for="puntos">Puntuación de la tarea:</label>
                    <input type="number" name="puntos" min="1000" step="100">
                    <input class="submit-registrotareas" type="submit" value="Crear Tarea">
                  </form>
            </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>
    .add-reward {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .info-menuusuarios {
        padding: 20px 10px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 300px;
    }

    .usuario-menuusuarios {
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
    .icon-menusuarios {
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
    .form-registrotareas {
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

    .form-registrotareas input, .form-registrotareas textarea {
        width: 85%;
        display: block;
        text-align: center;
        padding: 16px 5px;
        margin-bottom: 10px;
        border-radius: 15px;
        border: 2px solid #78BFA5;
        font-size: 18px;
        color: #515459;
        resize: none;
    }
    .form-registrotareas label {
        display: block;
        width: 85%;
        text-align: left;
        color: #515459;
    }

    input.submit-registrotareas {
        background: #78BFA5;
        border: none;
        color: #fff;
    }
</style>