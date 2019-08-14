<template>
  <div class="page-area">
    <div style="margin: 10px auto; width: 1000px; height: 340px; box-shadow: 0 0 10px #808080; text-align: left">
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
        <el-select v-model="language" size="mini" placeholder="Language" style="float: right; width: 120px">
          <el-option label="English" value="English"></el-option>
          <!-- <el-option label="中文" value="Chinese"></el-option> -->
        </el-select>
        <span style="background-color: #282828; width: 4px; height: 30px; float: left"></span>
        <strong style="font-size: 24px; line-height: 125%">&ensp;ABOUT ME</strong>
        <div style="font-size: 18px; line-height: 125%">
          <p>{{ about_p_1 }}</p>
          <p>{{ about_p_2 }}</p>
        </div>
      </div>
    </div>
    <div style="margin: 20px auto; width: 1000px; height: auto; box-shadow: 0 0 10px #808080; text-align: left">
      <div style="width: 100%; height: 340px">
        <span style="background-color: #FF3300; width: 4px; height: 100%; float: left"></span>
        <div style="padding: 40px 40px 20px 40px">
          <strong style="font-size: 24px">EDUCATION</strong>
          <div style="font-size: 18px; padding: 10px; line-height: 150%">
            <li>South China University of Technology</li>
            <div style="color: #808080">Master / Biomedical Engineering / Sep. 2018 - Present</div>
            <li>Beijing Institute of Technology</li>
            <div style="color: #808080">Bachelor / Electronic Engineering / Sep. 2014 - July 2018</div>
          </div>
          <br/>
          <strong style="font-size: 24px">EXPERIENCES</strong>
          <div style="font-size: 18px; padding: 10px; line-height: 150%">
            <li>Guangzhou ImageDT Technology Co., Ltd.</li>
            <div style="color: #808080">Algorithm Engineer Intern / July 2019 - Oct. 2019</div>
          </div>
        </div>
      </div>
      <div style="width: 100%; height: 340px">
        <span style="background-color: #282828; width: 4px; height: 100%; float: left"></span>
        <div style="padding: 20px 40px">
          <strong style="font-size: 24px">TECH STACK</strong>
          <div style="font-size: 18px; padding: 10px; line-height: 150%">
            <li>Web Developing</li>
            <div style="color: #808080">Vue.js Django Java</div>
            <br/>
            <li>Data Science</li>
            <div style="color: #808080">Scikit-Learn Numpy Pandas Keras</div>
          </div>
        </div>
      </div>
      <div style="width: 100%; height: 340px">
        <span style="background-color: #00CCFF; width: 4px; height: 100%; float: left"></span>
        <div style="padding: 20px 40px 40px 40px">
          <strong style="font-size: 24px">PROJECTS</strong>
          <div style="font-size: 18px; padding: 10px; line-height: 150%">
            <li>NEURO-LEARN: A Decentralized Solution for Pattern Analysis of Neuroimaging Data</li>
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
  }
}
</script>

<style lang="scss">
</style>
