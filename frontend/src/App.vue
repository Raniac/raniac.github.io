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
}
#app {
  min-width: 1200px;
  height: 100%;
}
</style>
