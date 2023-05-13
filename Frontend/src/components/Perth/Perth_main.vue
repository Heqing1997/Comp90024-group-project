<template>
   <div class = header>
      <h3>Perth Statistics</h3>
   </div>

   <div class="dropdown-wrapper">
      <Dropdown/>
    </div>

   <router-view></router-view>



</template>
<script>
import Dropdown from "@/components/Perth/Dropdown.vue";

export default {
    name: "Perth",
    components: {Dropdown}
}
</script>

<style scoped>
.header {

  font-size: 30px;
  position: fixed;
  top: 60px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60px;
  background-color: #fff;


}
.dropdown-wrapper {

  top: 10px;
}
</style>