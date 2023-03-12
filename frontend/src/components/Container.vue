<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div id="ctnr-area">
    <iframe
      frameborder="no"
      marginwidth="0"
      marginheight="0"
      width=260
      height=50
      style="position: fixed; right: 0; z-index: 100"
      src="//music.163.com/outchain/player?type=2&id=1610850&auto=1&height=32">
    </iframe>
    <transition name="slide-fade">
      <RouterView class="ctnr-view"/>
    </transition>
    <div>
      <div style="width: 100%; height: 36px; background-color: #E8E8E8; text-align: left">
        <div style="width: auto; color: #282828; font-size: 16px; padding: 10px 20px">
          &copy; 2019 - 2024 Benny Ray |
          Made with <a href="https://cn.vuejs.org/" target="_" style="color: #00CC99; font-weight: bold">Vue</a> |
          Hosted on <a href="https://pages.github.com/" target="_" style="color: #000033; font-weight: bold">GitHub.io</a>
        </div>
      </div>
      <span style="background-color: #FF3300; width: 10%; height: 4px; float: left"></span>
      <span style="background-color: #282828; width: 80%; height: 4px; float: left"></span>
      <span style="background-color: #00CCFF; width: 10%; height: 4px; float: right"></span>
    </div>
  </div>
</template>
  
<style lang="scss">
#ctnr-area {
  width: 100%;
  padding-top: 60px;
  text-align: center;
  height: calc(100% - 60px);
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
.ctnr-view {
  width: 1000px;
  margin: 0 auto;
  text-align: center;
  min-height: 100%;
}
.content-card {
  margin: 20px auto;
  width: 1000px;
  box-shadow: 0 0 10px #282828;
  text-align: left;
  background-color: #FFFFFF;
  &:hover {
    box-shadow: 0 0 20px #282828;
  }
}
.page-title {
  margin: 20px auto;
  width: 1000px;
  text-align: left;
}
</style>
