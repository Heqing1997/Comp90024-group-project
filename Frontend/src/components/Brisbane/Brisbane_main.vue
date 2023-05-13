<template>
   <div class = header>
      <h3>Brisbane Statistics</h3>
   </div>

   <div class="dropdown-wrapper">
      <Dropdown/>
    </div>

   <router-view></router-view>



</template>

<script>
import Dropdown from "@/components/Brisbane/Dropdown.vue";
import Highgate_hill from "@/components/Brisbane/Highgate_hill.vue";
// import Adelaide_cbd from "@/components/Adelaide/Adelaide_cbd.vue";
// import North_adelaide from "@/components/Adelaide/North_adelaide.vue";

export default {
    name: "Brisbane_main",
    components: {
       Dropdown,
       // Highgate_hill,
       // Adelaide_cbd,
       // North_adelaide,
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