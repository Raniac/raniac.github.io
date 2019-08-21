<template>
  <div class="blog-overview">
    <div class="blog-item" @click="handleViewDetail('test')">
      <img src="@/assets/img/Vegito.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: left"/>
      <div>null</div>
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
  height: 340px;
  box-shadow: 0 0 10px #808080;
  &:hover {
    box-shadow: 0 0 20px #808080;
  }
}
</style>
