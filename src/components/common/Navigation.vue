<template>
  <div id="nav-area">
    <div id="my-name">
      <router-link to="/" class="nav-link">BENNY RAY</router-link>
    </div>
    <el-menu
      id="nav-menu"
      :default-active="activeIndex2"
      mode="horizontal"
      @select="handleSelect"
      background-color="#282828"
      text-color="#FFFFFF"
      active-text-color="#00CCFF"
      float="right">
      <el-menu-item index="1"><router-link to="/" class="nav-link">HOME</router-link></el-menu-item>
      <el-menu-item index="2"><router-link to="/Projects" class="nav-link">PROJECTS</router-link></el-menu-item>
      <el-menu-item index="3"><router-link to="/" class="nav-link">BLOG</router-link></el-menu-item>
      <el-submenu index="4">
        <template slot="title">CONTACT</template>
        <el-menu-item index="4-1"><i class="el-icon-user"></i>GITHUB</el-menu-item>
        <el-menu-item index="4-2"><i class="el-icon-user"></i>E-MAIL</el-menu-item>
        <el-menu-item index="4-3"><i class="el-icon-user"></i>WECHAT</el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
export default {
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style lang="scss">
#nav-area {
  position: fixed;
  width: 100%;
  height: 60px;
  background-color: #282828;
  box-shadow: 5px 0 20px #282828;
  z-index: 10;
  text-align: left;
  #my-name {
    margin: 10px 40px;
    float: left;
    font-size: 30px;
    line-height: 40px;
    color: #FFFFFF;
  }
  #nav-menu {
    border: none;
    float: right;
  }
  .nav-link {
    text-decoration: none;
    &:link {
      color: #FFFFFF;
    }
    &:visited {
      color: #FFFFFF;
    }
    &:hover {
      color: #00CCFF;
    }
  }
}
</style>
