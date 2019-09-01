<template>
  <div class="page-area">
    <div class="page-info">
      <span style="background-color: #282828; margin-top: 15px; width: 8px; height: 44px; float: left"></span>
      <div style="font-size: 50px; color: #282828; line-height: 150%">&ensp;PORTFOLIO</div>
      <div style="font-size: 24px; color: #505050; line-height: 150%; font-family: Georgia, Palatino, serif">&ensp;Here are the projects that I've been working on.</div>
    </div>
    <div class="project-card">
      <span style="background-color: #282828; width: 4px; height: 200px; float: right"></span>
      <img src="@/assets/img/UI.png" style="height: 200px; width: 300px; float: left"/>
      <el-tooltip content="Check out the repository at GITHUB" placement="bottom" style="float: right; margin: 40px 40px 0 0; font-size: 40px; color: #505050">
        <i class="el-icon-connection" @click="handleRedirect('nlw-git')"></i>
      </el-tooltip>
      <el-tooltip content="Check out the demo page" placement="left" style="float: right; margin: 40px 20px 0 0; font-size: 40px; color: #505050">
        <i class="el-icon-s-promotion" @click="handleRedirect('nlw-home')"></i>
      </el-tooltip>
      <div style="float: left; width: 50%">
        <div class="project-title"><i class="el-icon-folder-opened"></i> NEURO-LEARN</div>
        <div class="project-intro">A decentralized solution for pattern analysis of neuroimaging data.</div>
      </div>
    </div>
    <div class="project-card">
      <span style="background-color: #282828; width: 4px; height: 200px; float: right"></span>
      <el-tooltip content="Check out the repository at GITHUB" placement="left" style="float: right; margin: 40px 40px 0 0; font-size: 40px; color: #505050">
        <i class="el-icon-connection" @click="handleRedirect('np-git')"></i>
      </el-tooltip>
      <div style="float: left; width: 80%">
        <div class="project-title"><i class="el-icon-folder-opened"></i> neuroimaging_with_python</div>
        <div class="project-intro">Neuroimaging data analysis using ML tools with Python.</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Portfolio',
  data () {
    return {
    }
  },
  methods: {
    handleRedirect (loc) {
      if (loc === 'nlw-git') {
        window.open('https://github.com/Raniac/NEURO-LEARN')
      } else if (loc === 'nlw-home') {
        window.open('https://raniac.github.io/neurolearn_demo/')
      } else if (loc === 'np-git') {
        window.open('https://github.com/Raniac/neuroimaging_with_python')
      }
    }
  }
}
</script>

<style lang="scss">
.page-info {
  text-align: left;
  margin: 20px auto;
  width: 1000px;
  height: 120px;
}
.project-card {
  margin: 20px auto;
  width: 1000px;
  height: 200px;
  box-shadow: 0 0 10px #808080;
  &:hover {
    box-shadow: 0 0 20px #808080;
  }
  .project-title {
    text-align: left;
    margin: 40px 40px 20px 40px;
    font-size: 34px;
    font-family: Georgia, Palatino, serif;
  }
  .project-intro {
    line-height: 30px;
    color: #505050;
    text-align: left;
    margin: 0 40px;
    font-size: 28px;
    font-family: serif;
  }
}
</style>
