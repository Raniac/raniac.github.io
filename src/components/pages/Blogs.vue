<template>
  <div class="blogs-overview" v-if="show_detail == 0">
    <div class="blog-item" @click="handleViewDetail('test')">
      <img src="@/assets/img/Vegito.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: left"/>
      <div>null</div>
    </div>
  </div>
  <div class="blog-detail" v-else-if="show_detail == 1">
    <div v-html="blogDetail" v-highlight></div>
  </div>
</template>

<script>
import readme from '@/assets/README.md'
export default {
  name: 'Blogs',
  data () {
    return {
      show_detail: 0,
      blogDetail: ''
    }
  },
  methods: {
    handleViewDetail (blogName) {
      this.show_detail = 1
      if (blogName === 'test') {
        this.blogDetail = this.md2html(readme)
      }
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
.blog-detail {
  margin: 20px auto;
  padding: 20px 40px;
  width: 1000px;
  height: auto;
  text-align: left;
  box-shadow: 0 0 10px #808080;
}
</style>
