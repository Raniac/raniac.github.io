<template>
  <div class="blog-overview">
    <div class="blog-item" @click="handleViewDetail('A03')">
      <span style="background-color: #282828; width: 4px; height: 180px; float: left"></span>
      <div style="float: left">
        <div class="blog-title"><i class="el-icon-document"></i> Ubuntu Tips and Tricks</div>
        <div style="margin: 10px 0; line-height: 40px; color: #505050; text-align: left; margin: 0 40px; font-size: 28px">2019-08-28</div>
      </div>
    </div>
    <div class="blog-item" @click="handleViewDetail('A02')">
      <span style="background-color: #282828; width: 4px; height: 180px; float: left"></span>
      <div style="float: left">
        <div class="blog-title"><i class="el-icon-document"></i> GNN——图网络相关知识整理</div>
        <div style="margin: 10px 0; line-height: 40px; color: #505050; text-align: left; margin: 0 40px; font-size: 28px">2019-08-24</div>
      </div>
    </div>
    <div class="blog-item" @click="handleViewDetail('A01')">
      <span style="background-color: #282828; width: 4px; height: 180px; float: left"></span>
      <div style="float: left">
        <div class="blog-title"><i class="el-icon-document"></i> Django+Vue前后端分离开发</div>
        <div style="margin: 10px 0; line-height: 40px; color: #505050; text-align: left; margin: 0 40px; font-size: 28px">2019-08-20</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Blog',
  data () {
    return {
    }
  },
  methods: {
    handleViewDetail (blogName) {
      this.$router.push({
        path: '/BlogDetail',
        query: {name: blogName}
      })
    }
  }
}
</script>

<style lang="scss">
.blog-item {
  margin: 20px auto;
  width: 1000px;
  height: 180px;
  box-shadow: 0 0 10px #808080;
  &:hover {
    box-shadow: 0 0 20px #808080;
  }
  .blog-title {
    float: left;
    text-align: left;
    width: 100%;
    margin: 40px 40px 20px 40px;
    font-size: 34px;
    font-family: Georgia, Palatino, serif;
  }
}
</style>
