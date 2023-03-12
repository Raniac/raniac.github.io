<template>
  <div>
    <div class="page-title">
      <span style="background-color: #282828; margin-top: 15px; width: 8px; height: 47px; float: left"></span>
      <div style="font-size: 50px; color: #303030; line-height: 150%">&ensp;GALLERY</div>
      <div style="font-size: 24px; color: #303030; line-height: 150%; font-family: Georgia, Palatino, serif">&ensp;The palest ink is better than the best memory.</div>
    </div>
    <div v-for="(value, index) in articles" :key="index">
      <div class="content-card" style="height: 180px" @click="handleViewDetail(value.label)">
        <span style="background-color: #282828; width: 4px; height: 180px; float: left"></span>
        <img src="@/assets/images/selfie.jpeg" style="height: 180px; float: right; float: left"/>
        <div style="float: left">
          <div class="item-title">{{ value.title }}</div>
          <div style="margin: 10px 0; line-height: 40px; color: #505050; text-align: left; margin: 0 40px; font-size: 28px">{{ value.date }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
const router = useRouter();
let articles = [
  {label: 'A04', title: 'NEURO-LEARN-DOCKER', date: '2020-07-24'},
  {label: 'A09', title: 'NEURO-LEARN', date: '2020-04-23'},
  {label: 'A01', title: 'Django+Vue前后端分离开发', date: '2019-08-20'},
  {label: 'A02', title: 'GNN——图网络相关知识整理', date: '2019-08-24'},
];
function handleViewDetail(blogName) {
  router.push({
    path: '/detail',
    query: {name: blogName}
  })
}
</script>
  
<style>
.item-title {
  float: left;
  text-align: left;
  width: 100%;
  margin: 40px 40px 20px 40px;
  font-size: 34px;
  font-family: Georgia, Palatino, serif;
}
</style>
  