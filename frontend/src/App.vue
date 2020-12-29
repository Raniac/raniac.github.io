<template>
  <div id="app">
    <!-- <img src="./assets/logo.png">
    <router-view/> -->
    <Navigation></Navigation>
    <Container></Container>
  </div>
</template>

<script>
import Navigation from '@/components/common/Navigation'
import Container from '@/components/common/Container'

export default {
  name: 'App',
  components: {
    Navigation,
    Container
  }
}
</script>

<style>
html, body {
  margin: 0;
  padding: 0;
  font-family: 'Arial';
  height: 100%;
  background-image: linear-gradient(45deg,slategray 25%,rgb(100, 115, 130) 0,rgb(100, 115, 130) 50%,slategray 0,slategray 75%,rgb(100, 115, 130) 0);
  background-size: 40px 40px;
}
#app {
  min-width: 1200px;
  height: 100%;
}
</style>
