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
          <el-dropdown-item command="/adelaide/401011001">401011001: Adelaide CBD</el-dropdown-item>
          <el-dropdown-item command="/adelaide/401011002">401011002: North Adelaide</el-dropdown-item>
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
