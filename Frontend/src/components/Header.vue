<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    :collapse="false"
    style="width: 100%; overflow: visible;"
  >
    <el-menu-item index="1">
      <router-link to="/adelaide">Adelaide</router-link>
    </el-menu-item>
    <el-menu-item index="2">
      <router-link to="/brisbane">Brisbane</router-link>
    </el-menu-item>
    <el-menu-item index="3">
      <router-link to="/melbourne">Melbourne</router-link>
    </el-menu-item>
    <el-menu-item index="4">
      <router-link to="/perth">Perth</router-link>
    </el-menu-item>
    <el-menu-item index="5">
      <router-link to="/sydney">Sydney</router-link>
    </el-menu-item>

  </el-menu>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const activeIndex = ref('1')
// const handleSelect = (key: string, keyPath: string[]) => {
//   console.log(key, keyPath)
// }
</script>

<style scoped>
.el-menu-demo {
  position: fixed;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
}
</style>

