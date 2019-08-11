<template>
  <div id="nav-area">
    <el-menu
      id="nav-menu"
      :default-active="activeIndex2"
      mode="horizontal"
      @select="handleSelect"
      background-color="#282828"
      text-color="#FFFFFF"
      active-text-color="#00CCFF"
      float="right">
      <el-menu-item index="1">HOME</el-menu-item>
      <el-menu-item index="2">PROJECTS</el-menu-item>
      <el-menu-item index="3">BLOG</el-menu-item>
      <el-submenu index="4">
        <template slot="title">CONTACT</template>
        <el-menu-item index="4-1">选项1</el-menu-item>
        <el-menu-item index="4-2">选项2</el-menu-item>
        <el-menu-item index="4-3">选项3</el-menu-item>
        <el-submenu index="4-4">
          <template slot="title">选项4</template>
          <el-menu-item index="4-4-1">选项1</el-menu-item>
          <el-menu-item index="4-4-2">选项2</el-menu-item>
          <el-menu-item index="4-4-3">选项3</el-menu-item>
        </el-submenu>
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
  #nav-menu {
    border: none;
    float: right;
  }
}
</style>
