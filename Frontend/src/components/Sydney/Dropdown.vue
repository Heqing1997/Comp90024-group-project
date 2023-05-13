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
          <el-dropdown-item command="/sydney/117031330">117031330: Alexandria</el-dropdown-item>
          <el-dropdown-item command="/sydney/117031330">117031331: Kensington</el-dropdown-item>
          <el-dropdown-item command="/sydney/117031333">117031333: Potts Point</el-dropdown-item>
          <el-dropdown-item command="/sydney/117031329">117031329: Darlinghurst</el-dropdown-item>
          <el-dropdown-item command="/sydney/117031336">117031329: Surry Hills</el-dropdown-item>
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
