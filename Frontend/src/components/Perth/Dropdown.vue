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
          <el-dropdown-item command="/perth/503021037">503021037: Kings Park</el-dropdown-item>
          <el-dropdown-item command="/perth/503021042">503021042: Shenton Park</el-dropdown-item>
          <el-dropdown-item command="/perth/503021043">503021043: West Leederville</el-dropdown-item>
          <el-dropdown-item command="/perth/503021038">503021038: Leederville</el-dropdown-item>
          <el-dropdown-item command="/perth/503021040">503021040: North Perth</el-dropdown-item>
          <el-dropdown-item command="/perth/503021039">503021039: Mount Lawley</el-dropdown-item>
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
