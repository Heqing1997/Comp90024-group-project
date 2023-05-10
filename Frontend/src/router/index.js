import { createRouter, createWebHistory } from 'vue-router';
import Adelaide_main from "@/components/Adelaide/Adelaide_main.vue";
import Brisbane_main from "@/components/Brisbane/Baisbane_main.vue";
import Melbourne_main from "@/components/Melbourne/Melbourne_main.vue";
import Perth_main from "@/components/Perth/Perth_main.vue";
import Sydney_main from "@/components/Sydney/Sydney_main.vue";
import Welcome from "@/components/Welcome.vue";
import Adelaide_cbd from "@/components/Adelaide/Adelaide_cbd.vue";
import North_adelaide from "@/components/Adelaide/North_adelaide.vue";

const routes  = [
 { path: "/", component: Welcome },
  {
    path: "/adelaide",
    component: Adelaide_main,
    children: [
      { path: "401011001", component: Adelaide_cbd },
      { path: "401011002", component: North_adelaide },
    ],
  },
  { path: "/brisbane", component: Brisbane_main },
  { path: "/melbourne", component: Melbourne_main },
  { path: "/perth", component: Perth_main },
  { path: "/sydney", component: Sydney_main },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router