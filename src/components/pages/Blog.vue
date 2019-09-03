<template>
  <div class="blog-overview">
    <div class="page-info">
      <span style="background-color: #282828; margin-top: 15px; width: 8px; height: 44px; float: left"></span>
      <div style="font-size: 50px; color: #282828; line-height: 150%">&ensp;BLOG</div>
      <div style="font-size: 24px; color: #505050; line-height: 150%; font-family: Georgia, Palatino, serif">&ensp;The palest ink is better than the best memory.</div>
    </div>
    <div v-for="(value, index) in articles" :key="index">
      <div class="blog-item" @click="handleViewDetail(value.label)">
        <span style="background-color: #282828; width: 4px; height: 180px; float: left"></span>
        <div style="float: left">
          <div class="blog-title"><i class="el-icon-document"></i> {{ value.title }}</div>
          <div style="margin: 10px 0; line-height: 40px; color: #505050; text-align: left; margin: 0 40px; font-size: 28px">{{ value.date }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Blog',
  data () {
    return {
      articles: [
        {label: 'A07', title: 'Docker Tips and Tricks', date: '2019-09-08'},
        {label: 'A06', title: 'MySQL Tips and Tricks', date: '2019-09-06'},
        {label: 'A05', title: 'Git Tips and Tricks', date: '2019-09-04'},
        {label: 'A04', title: 'Literature Reading | 19-08-30', date: '2019-08-30'},
        {label: 'A03', title: 'Ubuntu Tips and Tricks', date: '2019-08-28'},
        {label: 'A02', title: 'GNN——图网络相关知识整理', date: '2019-08-24'},
        {label: 'A01', title: 'Django+Vue前后端分离开发', date: '2019-08-20'}
      ]
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
