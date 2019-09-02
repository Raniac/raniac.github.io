<template>
  <div class="page-area">
    <div style="margin: 20px auto; width: 1000px; height: 340px; box-shadow: 0 0 10px #808080; text-align: left">
      <img src="@/assets/img/Me.jpg" style="float: left; width: auto; height: 100%; margin: 0"/>
      <div style="float: left; padding: 40px; width: 400px">
        <img src="@/assets/img/logo.png" style="width: 140px; height: 140px; margin: 0; float: right"/>
        <div style="font-size: 34px">Hi! I'm Benny.</div>
        <div style="font-size: 34px">嗨！我是炳業。</div>
        <div style="margin-top: 20px; font-size: 20px; color: #505050">Guangdong, China 中國廣東</div>
        <div style="margin-top: 20px; font-size: 20px; color: #505050">Master of Engineering</div>
        <div style="font-size: 20px; color: #505050">South China University of Technology</div>
        <div style="margin-top: 20px; font-size: 20px; color: #282828"><strong>INTERESTS:</strong> Artificial Intelligence, Web Development, Neuroinformatics, etc.</div>
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
        <div style="font-size: 18px; line-height: 150%">
          <p>{{ about_p_1 }}</p>
          <p>{{ about_p_2 }}</p>
        </div>
      </div>
    </div>
    <div style="margin: 20px auto; width: 1000px; height: auto; box-shadow: 0 0 10px #808080; text-align: left">
      <div style="width: 100%; height: 200px">
        <span style="background-color: #FF3300; width: 4px; height: 100%; float: left"></span>
        <div style="padding: 40px 40px 20px 40px">
          <strong style="font-size: 24px">EDUCATION</strong>
          <div style="font-size: 18px; padding: 10px; line-height: 150%">
            <li>South China University of Technology 華南理工大學</li>
            <div style="color: #808080">Master / Biomedical Engineering / Sep. 2018 - Present</div>
            <li>Beijing Institute of Technology 北京理工大學</li>
            <div style="color: #808080">Bachelor / Electronic Engineering / Sep. 2014 - July 2018</div>
          </div>
        </div>
      </div>
      <div style="width: 100%; height: 130px">
        <span style="background-color: #282828; width: 4px; height: 100%; float: left"></span>
        <div style="padding: 20px 40px">
          <strong style="font-size: 24px">EXPERIENCES</strong>
          <div style="font-size: 18px; padding: 10px; line-height: 150%">
            <li>Guangzhou ImageDT Technology Co., Ltd. 廣州圖匠數據科技有限公司</li>
            <div style="color: #808080">Algorithm Engineer Intern / July 2019 - Oct. 2019</div>
          </div>
        </div>
      </div>
      <div style="width: 100%; height: 260px">
        <span style="background-color: #00CCFF; width: 4px; height: 100%; float: left"></span>
        <div style="padding: 20px 40px 40px 40px">
          <strong style="font-size: 24px">TECH STACK</strong>
          <div style="font-size: 18px; padding: 10px; line-height: 150%">
            <li>Web Development</li>
            <div style="color: #808080; font-family: Courier">Vue.js Django MySQL Celery Git JQuery Gunicorn</div>
            <li>Data Science</li>
            <div style="color: #808080; font-family: Courier">Scikit-Learn Numpy Pandas Keras Pytorch Faiss MXNet</div>
            <li>Computer Science</li>
            <div style="color: #808080; font-family: Courier">Docker Linux</div>
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
      about_p_1: 'I am currently a second-year graduate student in Department of Biomedical Engineering at South China University of Technology (SCUT). Before coming to SCUT, I got my B.Eng degree from School of Information and Electronic, Beijing Institute of Technology (BIT) in 2018.',
      about_p_2: 'My research interests mainly focus on machine learning and its applications in neuroinformatics. I am also a big fan of web development and designing. I believe that the most import traits of an achiever are foresightedness and conscientiousness. My motto is "BE MORE", namely breadth and depth.'
    }
  },
  methods: {
    handleLangChange () {
      if (this.language === 'English') {
        this.about_p_1 = 'I am currently a second-year graduate student in Department of Biomedical Engineering at South China University of Technology (SCUT). Before coming to SCUT, I got my B.Eng degree from School of Information and Electronic, Beijing Institute of Technology (BIT) in 2018.'
        this.about_p_2 = 'My research interests mainly focus on machine learning and its applications in neuroinformatics. I am also a big fan of web development and designing. I believe that the most import traits of an achiever are foresightedness and conscientiousness. My motto is "BE MORE", namely breadth and depth.'
      } else if (this.language === 'Chinese') {
        this.about_p_1 = '我目前是一名華南理工大學生物醫學工程專業的碩士二年級研究生。來到華工前，我二零一八年在北京理工大學信息與電子學院取得學士學位。'
        this.about_p_2 = '我的研究興趣主要集中於機器學習及其在神經信息學領域中的應用。我也是網絡開發與設計的愛好者。我認爲一個成功人士最重要的特質包括前瞻性和責任心。我的座右銘是“BE MORE”，也即廣度與深度。'
      }
    }
  }
}
</script>

<style lang="scss">
</style>
