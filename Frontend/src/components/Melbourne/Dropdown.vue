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
          <el-dropdown-item command="/melbourne/206041118">206041118: Docklands</el-dropdown-item>
          <el-dropdown-item command="/melbourne/206041121">206041121: Kensington</el-dropdown-item>
          <el-dropdown-item command="/melbourne/206041120">206041120: Flemington</el-dropdown-item>
          <el-dropdown-item command="/melbourne/206041124">206041124: Parkville</el-dropdown-item>
          <el-dropdown-item command="/melbourne/206041117">206041117: Carlton</el-dropdown-item>
          <el-dropdown-item command="/melbourne/206041119">206041119: East Melbourne</el-dropdown-item>
          <el-dropdown-item command="/melbourne/206041125">206041125: South Yarra</el-dropdown-item>
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
