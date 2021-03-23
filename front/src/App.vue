<template>
  <div id="app">
    <div id="main">
      <router-view />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "App",
  components: {
  },
};
</script>

<style>
body {
    background-image: linear-gradient(45deg, #78bfa5 25%, #a66363 25%, #a66363 50%, #78bfa5 50%, #78bfa5 75%, #a66363 75%, #a66363 100%);
    background-size: 56.57px 56.57px;
}
</style>
