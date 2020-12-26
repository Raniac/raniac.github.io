<template>
  <div class="page-area" id="contact-area">
    <div class="page-info">
      <span style="background-color: #282828; margin-top: 15px; width: 8px; height: 44px; float: left"></span>
      <div style="font-size: 50px; color: #282828; line-height: 150%">&ensp;CONTACT</div>
      <div style="font-size: 24px; color: #505050; line-height: 150%; font-family: Georgia, Palatino, serif">&ensp;Two heads are always better than one.</div>
    </div>
    <div class="contact-card">
      <span style="background-color: #33CC00; width: 8px; height: 200px; float: left"></span>
      <img src="@/assets/img/avatar.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: left"/>
      <div style="float: left; margin: 20px 10px; color: #000000">
        <h1>WeChat</h1>
        <h2>LEIBINGYE</h2>
      </div>
      <img src="@/assets/img/WeChat_QR.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: right"/>
    </div>
    <div class="contact-card">
      <span style="background-color: #FF3300; width: 8px; height: 200px; float: left"></span>
      <img src="@/assets/img/avatar.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: left"/>
      <div style="float: left; margin: 20px 10px; color: #000000">
        <h1>Weibo</h1>
        <h2>ELRANIAC</h2>
      </div>
      <img src="@/assets/img/Weibo_QR.png" style="width: 160px; height: 160px; margin: 20px 40px; float: right"/>
    </div>
    <div class="contact-card">
      <span style="background-color: #00CCFF; width: 8px; height: 200px; float: left"></span>
      <img src="@/assets/img/avatar.jpg" style="width: 160px; height: 160px; margin: 20px 40px; float: left"/>
      <div style="float: left; margin: 20px 10px; color: #000000">
        <h1>Alipay</h1>
        <h2>ELRANIAC</h2>
      </div>
      <img src="@/assets/img/Alipay_QR.png" style="width: 160px; height: 160px; margin: 20px 40px; float: right"/>
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
#contact-area {
  margin: 0 auto;
  width: 1000px;
  .contact-card {
    margin: 20px auto;
    width: 1000px;
    height: 200px;
    text-align: left;
    box-shadow: 0 0 10px #808080;
  }
}
</style>
