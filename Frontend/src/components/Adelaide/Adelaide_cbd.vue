<template>
  <div ref="male_registered_chart" class="chart-container" style="min-width: 600px; height: 400px;"></div>
  <div ref="female_registered_chart" class="chart-container_2" style="min-width: 600px; height: 400px;"></div>
</template>


<script>
import axios from 'axios';
import * as echarts from "echarts";

export default {
  name: 'Adelaide_cbd',
  data() {
    return {
      sa2_male_registered: [0, 0, 0, 0, 0, 0, 0, 0, 0],
      sa2_female_registered:[0, 0, 0, 0, 0, 0, 0, 0, 0],
      male_chart: null,
      female_chart: null,
      response:null,
    };
  },
  methods: {

    async get_data() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/adelaide/401011001');
        let jsonData = response.data;
        this.sa2_male_registered = [
          jsonData.male.m_15_19_yr_marrd_reg_marrge,
          jsonData.male.m_20_24_yr_marrd_reg_marrge,
          jsonData.male.m_25_34_yr_marrd_reg_marrge,
          jsonData.male.m_35_44_yr_marrd_reg_marrge,
          jsonData.male.m_45_54_yr_marrd_reg_marrge,
          jsonData.male.m_55_64_yr_marrd_reg_marrge,
          jsonData.male.m_65_74_yr_marrd_reg_marrge,
          jsonData.male.m_75_84_yr_marrd_reg_marrge,
          jsonData.male.m_85ov_marrd_reg_marrge,
        ];
        this.sa2_female_registered = [
          jsonData.female.f_15_19_yr_marrd_reg_marrge,
          jsonData.female.f_20_24_yr_marrd_reg_marrge,
          jsonData.female.f_25_34_yr_marrd_reg_marrge,
          jsonData.female.f_35_44_yr_marrd_reg_marrge,
          jsonData.female.f_45_54_yr_marrd_reg_marrge,
          jsonData.female.f_55_64_yr_marrd_reg_marrge,
          jsonData.female.f_65_74_yr_marrd_reg_marrge,
          jsonData.female.f_75_84_yr_marrd_reg_marrge,
          jsonData.female.f_85ov_marrd_reg_marrge,
        ];
         console.log(this.sa2_female_registered);
        // this.initChart();
        this.initChart(this.male_chart,this.sa2_male_registered)
        this.initChart(this.female_chart,this.sa2_female_registered)
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    initChart(chartInstance, chartData) {
      const ageGroups = [
        "15-19",
        "20-24",
        "25-34",
        "35-44",
        "45-54",
        "55-64",
        "65-74",
        "75-84",
        "85+",
      ];

      let option = {

        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          },
          //   formatter:function(params){
          //     let number = params[0].data;
          //     console.log(number)
          //
          //     let ageGroup = params[0].axisValue;
          //     return `Age Group: ${ageGroup}<br>Registered marriage: ${number}`;
          // }

        },

        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: ageGroups,
            axisTick: {
              alignWithLabel: true
            }
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Direct',
            type: 'bar',
            barWidth: '60%',
            data: chartData
          }
        ]
      };
      chartInstance.setOption(option);
    },
  },


  mounted() {

    // console.log(this.$refs.male_registered_chart)
    this.male_chart = echarts.init(this.$refs.male_registered_chart);
    this.female_chart= echarts.init(this.$refs.female_registered_chart);
     // this.initChart();
    this.get_data();

  },
};
</script>

<style scoped>
.chart-container {
  position: absolute;
  left: 100px;
  top: 150px;
  width: 500px;
  height: 400px;
}
.chart-container_2 {
  position: absolute;
  left: 800px;
  top: 150px;
  width: 500px;
  height: 400px;
}
</style>
