<template>
  <div class="total-points">
        <div class="info-menuusuarios">
            <div class="usuario-menuusuarios">
                <div class="icon-menusuarios">
                </div>
                <p>Nombre de usuario</p>
            </div>
            <div class="opciones-menuusuarios">
                <div class="tarea-puntos">
                    <p class="nombre-puntos">Ducharse: </p>
                    <p class="puntos-puntos">3000</p>
                </div>
                <div class="tarea-puntos">
                    <p class="nombre-puntos">Limpiarse los dientes: </p>
                    <p class="puntos-puntos">5000</p>
                
                </div>
                <div class="tarea-puntos">
                    <p class="nombre-puntos">Coger el autobús: </p>
                    <p class="puntos-puntos">2500</p>
                </div>
                <div class="tarea-puntos">
                    <p class="nombre-puntos">Hacer los deberes: </p>
                    <p class="puntos-puntos">7000</p>
                </div>
                <div class="tarea-puntos">
                    <p class="nombre-puntos">Recoger la habitación: </p>
                    <p class="puntos-puntos">4000</p>
                </div>
        
                <div class="tarea-puntos">
                    <p class="nombre-puntos">Hacer ejercicio: </p>
                    <p class="puntos-puntos">3500</p>
                </div>
                <div class="totalpuntos">
                    <p>TOTAL: </p>
                    <p class="puntos-totalpuntos"> 25000</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>
    .total-points {
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
        background-color: #515459;
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

    .tarea-puntos {
        width: 80%;
        margin: 10px 0;
        display: flex;
        justify-content: space-between;
        color: #AA6666;
    }
    .nombre-puntos {
        color: #515459
    }

    .totalpuntos {
        border-top: 2px solid #515459;
        padding-top: 10px;
        width: 80%;
        margin: 10px 0;
        display: flex;
        justify-content: flex-end;
        color: #AA6666;
    }

    .totalpuntos p:first-child {
        padding-right: 10px;
        font-weight: bold;
        color: #515459
    }
</style>