<template>
   <div class = header>
      <h3>Sydney Statistics</h3>
   </div>

   <div class="dropdown-wrapper">
      <Dropdown/>
    </div>


      <div v-if="showChart" ref="bar_chart" class="chart-container_1" style="min-width: 1200px; height: 800px;"></div>
      <div v-if="showChart" ref="pie_chart" class="chart-container_2" style="min-width: 1200px; height: 800px;"></div>



      <router-view @hideData="hideData" @showData="showData"></router-view>








</template>
<script>
import Dropdown from "@/components/Sydney/Dropdown.vue";
import axios from "axios";
import * as echarts from "echarts";

export default {
    name: "Sydney",
    components: {Dropdown},
   data(){
       return{
       showChart: true,
       ageGroups : [
        "15-19",
        "20-24",
        "25-34",
        "35-44",
        "45-54",
        "55-64",
        "65-74",
        "75-84",
        "85+",
      ],
      people_marriedArray : [],
      people_deFactoArray : [],
      people_notMarriedArray :[],

       bar_chart:null,
       pie_chart:null,

     RegisteredTotal:0,
     DefactoTotal:0,
      NotMarriedTotal: 0,





       }
    },

     methods: {
    hideData() {
      this.showChart = false;
      console.log(this.showChart)
    },

    showData() {
      this.showChart = true;
      console.log(this.showChart)
    },

       async getData() {
         try {
           const response = await axios.get('http://172.26.135.144:8080/sydney');
           let brisbaneData = response.data;

         this.RegisteredTotal=brisbaneData.p_tot_marrd_reg_marrge
         this.DefactoTotal=brisbaneData.p_tot_married_de_facto
         this.NotMarriedTotal=brisbaneData.p_tot_not_married



       for (const age of this.ageGroups) {
          const ageFormatted = age.replace('-', '_');
          const ageKey = age === "85+" ? "p_85ov" : `p_${ageFormatted}_yr`;

          this.people_marriedArray.push(brisbaneData[`${ageKey}_marrd_reg_marrge`]);
          this.people_deFactoArray.push(brisbaneData[`${ageKey}_married_de_facto`]);
          this.people_notMarriedArray.push(brisbaneData[`${ageKey}_not_married`]);
      }

         // console.log(this.people_notMarriedArray);

         this.initChart2(this.pie_chart,this.RegisteredTotal,this.DefactoTotal,this.NotMarriedTotal,'Marital Status of Sydney city in Pie Chart')
         this.initChart3(this.bar_chart, this.ageGroups,this.people_marriedArray,this.people_deFactoArray,this.people_notMarriedArray,'Marital Status of Sydney city in Bar Chart')
         } catch (error) {
           console.error('Error fetching data:', error);
         }
       },


      initChart2(chartInstance,registered, de_facto, not_married,title) {
          let option = {
            title: {
              text: title,
              // subtext: 'Data',
              left: 'center',
            },
            tooltip: {
              trigger: 'item',
            },

            series: [
              {
                name: 'Marital Status',
                type: 'pie',
                radius: '50%',
                data: [
                  { value: registered, name: 'Registered' },
                  { value: de_facto, name: 'De Facto' },
                  { value: not_married, name: 'Not Married' },
                ],
                emphasis: {
                  itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)',
                  },
                },
              },
            ],
          };
          chartInstance.setOption(option)

    },




      initChart3(chartInstance,age,marriedArray,defactoArray,notMarriedArray,titleText){
           let option = {
                    title: {
                      text: titleText,
                      left: 'center',
                      textStyle: {
                        fontWeight: 'bold'
                      }
                    },
                    legend: {
                         bottom: 'bottom',
                         left: 'center'
                    },
                    tooltip: {},
                    dataset: {
                      dimensions: ["Age","Registered","De_Facto","Not_married"],
                      source: [
                      { Age: age[0],  Registered:marriedArray[0], De_Facto: defactoArray[0], Not_married: notMarriedArray[0] },
                      { Age: age[1],  Registered:marriedArray[1], De_Facto: defactoArray[1], Not_married: notMarriedArray[1] },
                      { Age: age[2],  Registered:marriedArray[2], De_Facto: defactoArray[2], Not_married: notMarriedArray[2] },
                     { Age: age[3],  Registered:marriedArray[3], De_Facto: defactoArray[3], Not_married: notMarriedArray[3] },
                     { Age: age[4],  Registered:marriedArray[4], De_Facto: defactoArray[4], Not_married: notMarriedArray[4] },
                     { Age: age[5],  Registered:marriedArray[5], De_Facto: defactoArray[5], Not_married: notMarriedArray[5] },
                     { Age: age[6],  Registered:marriedArray[6], De_Facto: defactoArray[6], Not_married: notMarriedArray[6] },
                     { Age: age[7],  Registered:marriedArray[7], De_Facto: defactoArray[7], Not_married: notMarriedArray[7] },
                     { Age: age[8],  Registered:marriedArray[8], De_Facto: defactoArray[8], Not_married: notMarriedArray[8] },
                      ]
                    },
                    xAxis: { type: 'category' },
                    yAxis: {},
                    // Declare several bar series, each will be mapped
                    // to a column of dataset.source by default.
                    series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }]
                  };

          chartInstance.setOption(option)




         }
     },
     mounted() {
       this.bar_chart=echarts.init(this.$refs.bar_chart)
       this.pie_chart=echarts.init(this.$refs.pie_chart)
       this.getData();
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

.chart-container_1 {
  position: absolute;
  left: 100px;
  top: 200px;
  width: 500px;
  height: 400px;
}

.chart-container_2 {
  position: absolute;
  left: 100px;
  top: 1050px;
  width: 500px;
  height: 400px;
}
</style>