<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div id="nav-area">
    <span style="background-color: #00CCFF; width: 4px; height: 60px; float: left"></span>
    <div id="my-name">
      <RouterLink id="nav-link" to="/about">LEI BINGYE</RouterLink>
    </div>
    <div id="nav-menu">
      <RouterLink id="nav-page" to="/toolkit">ToolKit</RouterLink>
      <RouterLink id="nav-page" to="/blog">Blog</RouterLink>
      <RouterLink id="nav-page" to="/gallery">Gallery</RouterLink>
    </div>
  </div>
</template>
  
<style lang="scss">
#nav-area {
  position: fixed;
  width: 100%;
  min-width: 720px;
  height: 60px;
  background-color: #282828;
  box-shadow: 0 0 20px #282828;
  z-index: 10;
  text-align: left;
  #my-name {
    margin: 10px 40px;
    float: left;
    font-size: 30px;
    line-height: 40px;
    color: #FFFFFF;
  }
  #nav-link {
    display: block;
    text-decoration: none;
    &:link {
      color: #FFFFFF;
    }
    &:visited {
      color: #FFFFFF;
    }
    &:hover {
      color: #AAAAAA;
    }
  }
  #nav-menu {
    padding-right: 20px;
  }
  #nav-page {
    display: block;
    padding: 10px 20px;
    float: right;
    line-height: 40px;
    font-size: 20px;
    font-weight: 400;
    font-family: "Arial";
    text-decoration: none;
    &:link {
      color: #DDDDDD;
    }
    &:visited {
      color: #DDDDDD;
    }
    &:hover {
      background-color: #202020;
    }
  }
}
</style>