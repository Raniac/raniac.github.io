<template>
  <div id="con-area">
    <transition name="slide-fade">
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
  width: 1100px;
  margin: 0 auto;
}
.slide-fade-enter-active {
  transition: all .4s ease;
}
.slide-fade-leave-active {
  transition: all 0s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-active {
  transform: translateX(-40px);
  opacity: 0;
}
</style>
