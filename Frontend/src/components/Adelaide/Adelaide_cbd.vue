<template>
<!--  <h3>adelaide_cbd</h3>-->
  <div ref="chart" style="min-width: 300px; height: 400px;"></div>
</template>

<script>
import axios from 'axios';
import * as echarts from "echarts";

export default {
  name: 'Adelaide_cbd',
  data() {
    return {
      sa2Data: null,
    };
  },
  mounted(){
    this.get_male_data();
    this.chart = echarts.init(this.$refs.chart);

  },

  methods: {
  async get_male_data() {
    try {
      const response = await axios.get('http://127.0.0.1:5000/adelaide/401011001');
      this.sa2Data = response.data;
      console.log(this.sa2Data);
      this.initChart();

    } catch (error) {
      console.error('Error fetching data:', error);
    }

  },
  initChart() {
    const chart = echarts.init(this.$refs.chart);

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
    const data = [
      this.sa2Data.m_15_19_yr_marrd_reg_marrge,
      this.sa2Data.m_20_24_yr_marrd_reg_marrge,
      this.sa2Data.m_25_34_yr_marrd_reg_marrge,
      this.sa2Data.m_35_44_yr_marrd_reg_marrge,
      this.sa2Data.m_45_54_yr_marrd_reg_marrge,
      this.sa2Data.m_55_64_yr_marrd_reg_marrge,
      this.sa2Data.m_65_74_yr_marrd_reg_marrge,
      this.sa2Data.m_75_84_yr_marrd_reg_marrge,
    ];
    const option = {
      xAxis: {
        type: "category",
        data: ageGroups,
      },
      yAxis: {
        type: "value",
      },
      series: [
        {
          data: data,
          type: "bar",
        },
      ],
    };

    chart.setOption(option);
    },
  },
};
</script>

<style scoped></style>
