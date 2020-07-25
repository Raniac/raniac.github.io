<template>
  <div class="page-area">
    <div style="margin: 20px auto; width: 1000px; height: 340px; box-shadow: 0 0 10px #808080; text-align: left">
      <img src="@/assets/img/Me.jpg" style="float: left; width: auto; height: 100%; margin: 0"/>
      <div style="float: left; padding: 40px; width: 400px">
        <img src="@/assets/img/logo.png" style="width: 140px; height: 140px; margin: 0; float: right"/>
        <div style="font-size: 34px">Hi! I'm Benny.</div>
        <div style="font-size: 34px">嗨！我是炳业。</div>
        <div style="margin-top: 20px; font-size: 20px; color: #505050">Guangdong, China 中国广东</div>
        <div style="margin-top: 20px; font-size: 20px; color: #505050">Master of Engineering, SCUT</div>
        <div style="font-size: 20px; color: #505050">Author of <a href="https://rdcu.be/b4NCq" target="_blank">NEURO-</a><a href="https://github.com/Raniac/NEURO-LEARN-DOCKER/" target="_blank">LEARN</a></div>
        <div style="margin-top: 20px; font-size: 20px; color: #282828"><strong>INTERESTS:</strong> Web Development, Artificial Intelligence, Big Data & Cloud Computing.</div>
      </div>
      <span style="background-color: #282828; width: 4px; height: 340px; float: right"></span>
    </div>
    <div style="margin: 20px auto; width: 1000px; height: auto; box-shadow: 0 0 10px #808080; text-align: left">
      <div style="padding: 40px 40px 20px 40px">
        <el-select v-model="language" size="mini" placeholder="Language" style="float: right; width: 120px" @change="handleLangChange">
          <el-option label="English" value="English"></el-option>
          <el-option label="中文" value="Chinese"></el-option>
        </el-select>
        <span style="background-color: #282828; width: 4px; height: 30px; float: left"></span>
        <strong style="font-size: 24px; line-height: 125%">&ensp;ABOUT ME</strong>
        <div style="font-size: 18px; line-height: 150%; font-family: Georgia, Palatino, serif">
          <p>{{ about_p_1 }}</p>
          <p>{{ about_p_2 }}</p>
        </div>
      </div>
    </div>
    <div style="margin: 20px auto; width: 1000px; height: auto; box-shadow: 0 0 10px #808080; text-align: left">
      <div style="width: 100%; height: 200px">
        <span style="background-color: #FF3300; width: 4px; height: 100%; float: left"></span>
        <div style="padding: 40px 40px 20px 40px">
          <strong style="font-size: 24px">EXPERIENCES</strong>
          <div style="font-size: 18px; padding: 10px; line-height: 150%">
            <li>HUAWEI TECHNOLOGIES CO., LTD. 华为技术有限公司</li>
            <div style="color: #808080">Software Engineer Intern / June 2020 - Aug. 2020</div>
            <li>Guangzhou ImageDT Technology Co., Ltd. 广州图匠数据科技有限公司</li>
            <div style="color: #808080">Algorithm Engineer Intern / July 2019 - Oct. 2019</div>
          </div>
        </div>
      </div>
      <div style="width: 100%; height: 180px">
        <span style="background-color: #282828; width: 4px; height: 100%; float: left"></span>
        <div style="padding: 20px 40px">
          <strong style="font-size: 24px">EDUCATION</strong>
          <div style="font-size: 18px; padding: 10px; line-height: 150%">
            <li>South China University of Technology 华南理工大学</li>
            <div style="color: #808080">Master / Medical Information Engineering / Sep. 2018 - Present</div>
            <li>Beijing Institute of Technology 北京理工大学</li>
            <div style="color: #808080">Bachelor / Electronic Engineering / Sep. 2014 - July 2018</div>
          </div>
        </div>
      </div>
      <div style="width: 100%; height: 260px">
        <span style="background-color: #00CCFF; width: 4px; height: 100%; float: left"></span>
        <div style="padding: 20px 40px 40px 40px">
          <strong style="font-size: 24px">TECH STACK</strong>
          <div style="font-size: 18px; padding: 10px; line-height: 150%">
            <li>Web Development</li>
            <div style="color: #808080; font-family: Courier">Django/Flask/Tornado; Spring; Vue.js; MySQL/Redis</div>
            <li>Artificial Intelligence</li>
            <div style="color: #808080; font-family: Courier">Machine Learning; Deep Learning; Graph Neural Network</div>
            <li>Big Data & Cloud Computing</li>
            <div style="color: #808080; font-family: Courier">Docker/Kubernetes; Hadoop Ecosystem; Spark</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      language: 'English',
      about_p_1: 'I am currently a second-year graduate student majoring in Medical Information Engineering at South China University of Technology (SCUT). Before coming to SCUT, I got my B.Eng degree from School of Information and Electronic, Beijing Institute of Technology (BIT) in 2018.',
      about_p_2: 'My research interests mainly focus on machine learning and its applications in neuroinformatics. I am also a big fan of web development and designing.'
    }
  },
  methods: {
    handleLangChange () {
      if (this.language === 'English') {
        this.about_p_1 = 'I am currently a second-year graduate student majoring in Medical Information Engineering at South China University of Technology (SCUT). Before coming to SCUT, I got my B.Eng degree from School of Information and Electronic, Beijing Institute of Technology (BIT) in 2018.'
        this.about_p_2 = 'My research interests mainly focus on machine learning and its applications in neuroinformatics. I am also a big fan of web development and designing.'
      } else if (this.language === 'Chinese') {
        this.about_p_1 = '我目前是一名华南理工大学医学信息工程专业的硕士二年级研究生。来到华工前，我二零一八年在北京理工大学信息与电子学院取得学士学位。'
        this.about_p_2 = '我的研究兴趣主要集中于机器学习及其在神经信息学领域中的应用。我也是Web开发与设计的爱好者。'
      }
    }
  }
}
</script>

<style lang="scss">
a {
  text-decoration: none;
  color: #282828;
  font-weight: bold;
}
</style>
