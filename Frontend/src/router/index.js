import { createRouter, createWebHistory } from 'vue-router';
import Adelaide_main from "@/components/Adelaide/Adelaide_main.vue";
import Brisbane_main from "@/components/Brisbane/Brisbane_main.vue";
import Melbourne_main from "@/components/Melbourne/Melbourne_main.vue";
import Perth_main from "@/components/Perth/Perth_main.vue";
import Sydney_main from "@/components/Sydney/Sydney_main.vue";
import Welcome from "@/components/Welcome.vue";
import Adelaide_cbd from "@/components/Adelaide/Adelaide_cbd.vue";
import North_adelaide from "@/components/Adelaide/North_adelaide.vue";
import Highgate_hill from "@/components/Brisbane/Highgate_hill.vue";
import South_brisbane from "@/components/Brisbane/South_brisbane.vue";
import West_end from "@/components/Brisbane/West_end.vue";
import Brisbane_cbd from "@/components/Brisbane/Brisbane_cbd.vue";
import Spring_hill from "@/components/Brisbane/Spring_hill.vue";
import Fortitude_valley from "@/components/Brisbane/Fortitude_valley.vue";
import New_farm from "@/components/Brisbane/New_farm.vue";
import Kangaroo_point from "@/components/Brisbane/Kangaroo_point.vue";
import Carlton from "@/components/Melbourne/Carlton.vue";
import Docklands from "@/components/Melbourne/Docklands.vue";
import East_melbourne from "@/components/Melbourne/East_melbourne.vue";
import Flemington from "@/components/Melbourne/Flemington.vue";
import Kensington from "@/components/Melbourne/Kensington.vue";
import Parkville from "@/components/Melbourne/Parkville.vue";
import South_yarra from "@/components/Melbourne/South_yarra.vue";
import Kings_park from "@/components/Perth/Kings_park.vue";
import Leederville from "@/components/Perth/Leederville.vue";
import Mount_lawley from "@/components/Perth/Mount_lawley.vue";
import North_perth from "@/components/Perth/North_perth.vue";
import Shenton_park from "@/components/Perth/Shenton_park.vue";
import West_leederville from "@/components/Perth/West_leederville.vue";
import Alexandria from "@/components/Sydney/Alexandria.vue";
import Darlinghurst from "@/components/Sydney/Darlinghurst.vue";
import Kensington_sydney from "@/components/Sydney/Kensington_sydney.vue";
import Potts_point from "@/components/Sydney/Potts_point.vue";
import Surry_hills from "@/components/Sydney/Surry_hills.vue";
import Twitter_analysis from "@/components/Twitter_analysis.vue";
import Mastodon_analysis from "@/components/Mastodon_analysis.vue";


const routes  = [
 { path: "/", component: Welcome },
  {
    path: "/adelaide",
    component: Adelaide_main,
    children: [
      { path: "401011001", component: Adelaide_cbd, },
      { path: "401011002", component: North_adelaide },
    ],
  },
  { path: "/brisbane",
    component: Brisbane_main,
    children: [
      { path: "305011107", component: Highgate_hill },
       { path: "305011110", component: South_brisbane },
      { path: "305011112", component: West_end },
      { path: "305011108", component: Kangaroo_point },
      { path: "305011105", component: Brisbane_cbd },
      { path: "305011111", component: Spring_hill },
      { path: "305011106", component: Fortitude_valley },
      { path: "305011109", component: New_farm },
      // { path: "401011002", component: North_adelaide },
    ],
  },
    {
    path: "/melbourne",
    component: Melbourne_main,
    children: [
      { path: "206041118", component: Docklands },
      { path: "206041121", component: Kensington },
      { path: "206041120", component: Flemington },
      { path: "206041124", component: Parkville },
      { path: "206041117", component: Carlton },
      { path: "206041119", component: East_melbourne },
      { path: "206041125", component: South_yarra },
    ],
  },


  {
    path: "/perth",
    component: Perth_main,
       children: [
      { path: "503021037", component: Kings_park },
      { path: "503021042", component: Shenton_park },
      { path: "503021043", component: West_leederville },
      { path: "503021038", component: Leederville },
      { path: "503021040", component: North_perth },
      { path: "503021039", component: Mount_lawley },
    ],
  },

  { path: "/sydney",
    component: Sydney_main,
      children: [
      { path: "117031330", component: Alexandria },
      { path: "117031331", component: Kensington_sydney },
      { path: "117031333", component: Potts_point },
      { path: "117031329", component: Darlinghurst },
      { path: "117031336", component: Surry_hills },
    ],
  },

  { path: "/twitters", component: Twitter_analysis},
  { path: "/mastodon", component: Mastodon_analysis}

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router