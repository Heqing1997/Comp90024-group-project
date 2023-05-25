<template>
    <div ref="adelaide_chart" class="chart-container" style="width: 400px; height: 400px;"></div>
    <div ref="brisbane_chart" class="chart-container_1" style="width: 400px; height: 400px;"></div>
    <div ref="melbourne_chart" class="chart-container_2" style="width: 400px; height: 400px;"></div>
    <div ref="perth_chart" class="chart-container_3" style="width: 400px; height: 400px;"></div>
    <div ref="sydney_chart" class="chart-container_4" style="width: 400px; height: 400px;"></div>
    <div ref="others_chart" class="chart-container_5" style="width: 400px; height: 400px;"></div>

</template>
<script >
import axios from "axios";
import * as echarts from "echarts";
export default{
    name: 'twitter analysis',
    data(){
        return{
            category:["Negative", "Neutral", "Positive"],
            adelaide_twitter_data:[0,0,0],
            brisbane_twitter_data:[0,0,0],
            melbourne_twitter_data:[0,0,0],
            perth_twitter_data:[0,0,0],
            sydney_twitter_data:[0,0,0],
            others_twitter_data:[0,0,0],
            adelaide_chart: null,
            brisbane_chart:null,
            melbourne_chart:null,
            perth_chart:null,
            sydney_chart:null,
            others_chart:null,

        }
    },
    methods:{
      async get_data() {
        try {
          const response = await axios.get('http://172.26.135.144:8080/twitter_analysis');
          let jsonData = response.data;

          this.adelaide_twitter_data = [
             jsonData.Adelaide.Negative,
              jsonData.Adelaide.Neutral,
             jsonData.Adelaide.Positive
          ];


          this.brisbane_twitter_data = [
            jsonData.Brisbane.Negative,
            jsonData.Brisbane.Neutral,
             jsonData.Brisbane.Positive

          ];
           this.melbourne_twitter_data = [
             jsonData.Melbourne.Negative,
             jsonData.Melbourne.Neutral,
             jsonData.Melbourne.Positive

          ];

          this.perth_twitter_data = [
            jsonData.Perth.Negative,
              jsonData.Perth.Neutral,
            jsonData.Perth.Positive,

          ];

          this.sydney_twitter_data = [
               jsonData.Sydney.Negative,
               jsonData.Sydney.Neutral,
              jsonData.Sydney.Negative

          ];

           this.others_twitter_data = [
              jsonData.Other_places.Negative,
                jsonData.Other_places.Neutral,
               jsonData.Other_places.Positive

          ];



          this.initChart(this.adelaide_chart,this.adelaide_twitter_data,'Adelaide marriage tweets emotion statistics')
          this.initChart(this.brisbane_chart,this.brisbane_twitter_data,"Brisbane marriage tweets emotion statistics")
          this.initChart(this.melbourne_chart,this.melbourne_twitter_data,"Melbourne marriage tweets emotion statistics")
          this.initChart(this.perth_chart,this.perth_twitter_data,"Perth marriage tweets emotion statistics")
          this.initChart(this.sydney_chart,this.sydney_twitter_data,"Sydney marriage tweets emotion statistics")
          this.initChart(this.others_chart,this.others_twitter_data,"Other cities marriage tweets emotion statistics")


        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },

      initChart(chartInstance, chartData,titleText) {

        let option = {
            title: {
            text: titleText,
            left: 'center',
            textStyle: {
              fontWeight: 'bold'
            }
          },

          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            },

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
              data: this.category,
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
              barWidth: '30%',
              data: [
                  {value:chartData[0],itemStyle:{color: '#a90000'}},
                  {value:chartData[1],itemStyle:{color: '#F6BE00'}},
                  {value:chartData[2],itemStyle:{color: '#056608'}},


              ],

              label: {
                show: true,
                position: 'top',
                color: 'black',
                fontSize: 12
              }
            }
          ]

        };
      chartInstance.setOption(option);
    },




    },
    mounted() {
        this.adelaide_chart = echarts.init(this.$refs.adelaide_chart)
        this.brisbane_chart = echarts.init(this.$refs.brisbane_chart)
        this.melbourne_chart = echarts.init(this.$refs.melbourne_chart)
        this.perth_chart = echarts.init(this.$refs.perth_chart)
        this.sydney_chart = echarts.init(this.$refs.sydney_chart)
        this.others_chart = echarts.init(this.$refs.others_chart)
        this.get_data()

    }


}



</script>



<style scoped>
.chart-container {
  position: absolute;
  left: 100px;
  top: 155px;
  width: 500px;
  height: 400px;
}
.chart-container_1 {
  position: absolute;
  left: 600px;
  top: 150px;
  width: 500px;
  height: 400px;
}
.chart-container_2 {
  position: absolute;
  left: 1100px;
  top: 150px;
  width: 500px;
  height: 400px;
}
.chart-container_3 {
  left: 100px;
  top: 655px;
  width: 500px;
  height: 400px;
}
.chart-container_4 {
  position: absolute;
  left: 600px;
  top: 660px;
  width: 500px;
  height: 400px;
}
.chart-container_5 {
  position: absolute;
  left: 1100px;
  top: 660px;
  width: 500px;
  height: 400px;
}

</style>