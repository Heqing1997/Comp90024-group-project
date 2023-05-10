<template>
   <div class = header>
      <h3>Adelaide Statistics</h3>
   </div>

   <div class="dropdown-wrapper">
      <Dropdown/>
    </div>

   <router-view></router-view>



</template>

<script>
import Dropdown from "@/components/Adelaide/Dropdown.vue";
import Adelaide_cbd from "@/components/Adelaide/Adelaide_cbd.vue";
import North_adelaide from "@/components/Adelaide/North_adelaide.vue";

export default {
    name: "Adelaide_main",
    components: {
       Dropdown,
       Adelaide_cbd,
       North_adelaide,
    },


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