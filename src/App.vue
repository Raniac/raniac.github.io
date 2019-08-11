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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  // margin-top: 60px;
}
</style>
