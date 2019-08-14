<template>
  <div class="page-area">
    <div class="project-card">
      <img src="@/assets/img/Vegito.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: left"/>
      <div>null</div>
    </div>
    <div class="project-card">
      <img src="@/assets/img/Vegito.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: left"/>
      <div>null</div>
    </div>
    <div class="project-card">
      <img src="@/assets/img/Vegito.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: left"/>
      <div>null</div>
    </div>
    <div class="project-card">
      <img src="@/assets/img/Vegito.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: left"/>
      <div>null</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Portfolio',
  data () {
    return {
    }
  }
}
</script>

<style lang="scss">
.project-card {
  margin: 20px auto;
  width: 1000px;
  height: 340px;
  box-shadow: 0 0 10px #808080;
  &:hover {
    box-shadow: 0 0 20px #808080;
  }
}
</style>
