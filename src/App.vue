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
body {
  margin: 0;
  padding: 0;
  font-family: 'Arial';
}
#app {
  min-width: 1200px;
}
</style>
