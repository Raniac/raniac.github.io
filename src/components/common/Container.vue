<template>
  <div id="con-area">
    <iframe
      frameborder="no"
      border="0"
      marginwidth="0"
      marginheight="0"
      width=260
      height=50
      style="float: right"
      src="//music.163.com/outchain/player?type=2&id=1610850&auto=1&height=32">
    </iframe>
    <div id="content">
      <transition name="slide-fade">
        <router-view/>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Container'
}
</script>

<style lang="scss">
#con-area {
  padding-top: 60px;
  text-align: center;
  #content {
    width: 1000px;
    margin: -10px auto;
    background-color: #000;
  }
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
