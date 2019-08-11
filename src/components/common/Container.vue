<template>
  <div id="con-area">
    alfad
    <transition>
      <router-view/>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'Container'
}
</script>

<style>
#con-area {
  padding-top: 60px;
}
</style>
