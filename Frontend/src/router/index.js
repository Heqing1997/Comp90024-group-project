import { createRouter, createWebHistory } from 'vue-router';
import Adelaide_main from "@/components/Adelaide/Adelaide_main.vue";
import Baisbane_main from "@/components/Brisbane/Baisbane_main.vue";
import Melbourne_main from "@/components/Melbourne/Melbourne_main.vue";
import Perth_main from "@/components/Perth/Perth_main.vue";
import Sydney_main from "@/components/Sydney/Sydney_main.vue";
import Welcome from "@/components/Welcome.vue";


const routes  = [
  { path: "/", component: Welcome },
  { path: "/adelaide", component: Adelaide_main },
  { path: "/brisbane", component: Baisbane_main },
  { path: "/melbourne", component: Melbourne_main },
  { path: "/perth", component: Perth_main },
  { path: "/sydney", component: Sydney_main },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router