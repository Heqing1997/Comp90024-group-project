<!-- Dropdown.vue -->
<template>
  <div class="dropdown-container">
    <el-dropdown @command="changeComponent">
      <span class="el-dropdown-link">
        SA2 Code
        <el-icon class="el-icon--right">
          <arrow-down />
        </el-icon>
      </span>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item command="/brisbane/305011107">305011107: Highgate Hill</el-dropdown-item>
          <el-dropdown-item command="/brisbane/305011110">305011110: South Brisbane</el-dropdown-item>
          <el-dropdown-item command="/brisbane/305011112">305011112: West End</el-dropdown-item>
          <el-dropdown-item command="/brisbane/305011108">305011108: Kangaroo Point </el-dropdown-item>
          <el-dropdown-item command="/brisbane/305011105">305011105: Brisbane City </el-dropdown-item>
          <el-dropdown-item command="/brisbane/305011111">305011111: Spring Hill </el-dropdown-item>
          <el-dropdown-item command="/brisbane/305011106">305011106: Fortitude Valley </el-dropdown-item>
          <el-dropdown-item command="/brisbane/305011109">305011109: New Farm </el-dropdown-item>

        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>
</template>

<script lang="ts" setup>
import { ArrowDown } from '@element-plus/icons-vue';
import { useRouter } from "vue-router";

const router = useRouter();

const changeComponent = (route) => {
  router.push(route);
};
</script>

<style scoped>
.el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}

.dropdown-container {
  position: fixed;
  top: 120px;
  left: 100px;
}
</style>
