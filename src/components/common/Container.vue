<template>
  <div id="con-area">
    <iframe
      frameborder="no"
      border="0"
      marginwidth="0"
      marginheight="0"
      width=260
      height=50
      style="position: fixed; right: 0"
      src="//music.163.com/outchain/player?type=2&id=1610850&auto=1&height=32">
    </iframe>
    <div id="content">
      <transition name="slide-fade">
        <router-view/>
      </transition>
    </div>
    <div>
      <div style="width: 100%; height: 36px; background-color: #E8E8E8; text-align: left">
        <div style="width: auto; color: #282828; font-size: 16px; padding: 10px 20px">
          &copy; 2019 - 2020 Benny Ray /
          Made with <a href="https://cn.vuejs.org/" target="_" style="color: #00CC99"><strong>Vue</strong></a> /
          Hosted on <a href="https://pages.github.com/" target="_" style="color: #000033"><strong>GitHub.io</strong></a>
        </div>
      </div>
      <span style="background-color: #FF3300; width: 10%; height: 4px; float: left"></span>
      <span style="background-color: #282828; width: 80%; height: 4px; float: left"></span>
      <span style="background-color: #00CCFF; width: 10%; height: 4px; float: right"></span>
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
  height: calc(100% - 80px);
  #content {
    // width: 1000px;
    margin: 0 auto;
    text-align: center;
    min-height: calc(100% - 40px);
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
