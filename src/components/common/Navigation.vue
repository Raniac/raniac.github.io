<template>
  <div id="nav-area">
    <span style="background-color: #00CCFF; width: 4px; height: 60px; float: left"></span>
    <div id="my-name">
      <div class="nav-link">BENNY RAY</div>
    </div>
    <el-menu
      id="nav-menu"
      :default-active="activeIndex"
      mode="horizontal"
      @select="handleSelect"
      background-color="#282828"
      text-color="#FFFFFF"
      active-text-color="#FF3300"
      float="right">
      <el-menu-item index="1">HOME</el-menu-item>
      <el-menu-item index="2">PORTFOLIO</el-menu-item>
      <el-menu-item index="3">BLOGS</el-menu-item>
      <el-submenu index="4">
        <template slot="title">CONTACT</template>
        <el-menu-item index="4-1"><i class="el-icon-user"></i>GITHUB - Raniac</el-menu-item>
        <el-menu-item index="4-2"><i class="el-icon-user"></i>BLOGS - Raniac</el-menu-item>
        <el-menu-item index="4-3"><i class="el-icon-message"></i>E-MAIL</el-menu-item>
        <el-menu-item index="4-4"><i class="el-icon-chat-dot-round"></i>SOCIAL MEDIA</el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
export default {
  data () {
    return {
      activeIndex: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      if (key === '1') {
        this.$router.replace({
          path: '/'
        })
      } else if (key === '2') {
        this.$router.replace({
          path: '/Portfolio'
        })
      } else if (key === '3') {
        this.$router.replace({
          path: '/'
        })
      } else if (key === '4-1') {
        window.open('https://github.com/Raniac', '_blank')
      } else if (key === '4-2') {
        window.open('https://www.jianshu.com/u/99cc5e74dd78', '_blank')
      } else if (key === '4-3') {
        window.location.href = 'mailto:leibingye@outlook.com'
      } else if (key === '4-4') {
        this.$router.replace({
          path: '/Contact'
        })
      }
    }
  }
}
</script>

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
  #nav-menu {
    border: none;
    float: right;
  }
  .nav-link {
    display: block;
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
a {
  text-decoration: none;
  &:link {
    color: #FFFFFF;
  }
  &:visited {
    color: #FFFFFF;
  }
  &:hover {
    color: #FF3300;
  }
}
</style>
