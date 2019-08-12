<template>
  <div class="page-area">
    <div class="contact-card">
      <span style="background-color: #00CCFF; width: 8px; height: 200px; float: left"></span>
      <img src="@/assets/img/Vegito.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: left"/>
      <div style="float: left; margin: 20px 10px; color: #000000">
        <h1>WeChat</h1>
        <h2>Benny_Ray</h2>
      </div>
      <img src="@/assets/img/QRcode.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: right"/>
    </div>
    <div class="contact-card">
      <span style="background-color: #FF3300; width: 8px; height: 200px; float: left"></span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Contact',
  data () {
    return {
    }
  }
}
</script>

<style lang="scss">
.contact-card {
  margin-top: 40px;
  width: 1000px;
  height: 200px;
  box-shadow: 1px 0 10px #E8E8E8;
}
</style>
