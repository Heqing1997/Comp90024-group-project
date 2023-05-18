
<template>
  <div ref="mastodon_chart" class="chart-container" style="width: 1200px; height: 400px;"></div>

</template>

<script>
import axios from "axios";
import * as echarts from "echarts";

export default {
    data(){
        return{
            category:['Positive','Neutral','Negative'],
            mastodon_data:[0,0,0],
            chart:null,
            timer: null

        }
    },

    methods:{
      async get_data() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/mastodon_analysis');
          let jsonData = response.data;

          this.mastodon_data=[jsonData.Positive,jsonData.Neutral,jsonData.Negative]
          console.log(this.mastodon_data)
          this.initChart(this.chart,this.mastodon_data,"Mastodon AU Server Marriage Sentiment Data")


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

          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
            max: 'dataMax'
          },
          yAxis:
            {
                type: 'category',
                data: this.category,
                inverse: true,
                animationDuration: 300,
                animationDurationUpdate: 300,
                max: 2 // only the largest 3 bars will be displayed
            },

          series: [
            {
              realtimeSort: true,
              type: 'bar',
              barWidth: '60%',
              data: [
                  {value:chartData[0],itemStyle:{color: '#056608'}},
                  {value:chartData[1],itemStyle:{color: '#F6BE00'}},
                  {value:chartData[2],itemStyle:{color: '#a90000'}},


              ],
              label: {
                show: true,
                position: 'right',
                color: 'black',
                fontSize: 12
              }
            }
          ],
          animationDuration: 0,
          animationDurationUpdate: 3000,
          animationEasing: 'linear',
          animationEasingUpdate: 'linear'

        };
        chartInstance.setOption(option);
      },

    },
    async mounted() {
        this.chart=echarts.init(this.$refs.mastodon_chart)
        await this.get_data()
        this.timer =setInterval(this.get_data,5000)

    },
    beforeUnmount() {
        clearInterval(this.timer)
    }


}

</script>


<style scoped>
.chart-container {
  position: absolute;
  left: 200px;
  top: 300px;
  width: 500px;
  height: 400px;
}

</style>