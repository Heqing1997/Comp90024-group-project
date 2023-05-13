<template>
  <div ref="male_registered_chart" class="chart-container" style="min-width: 600px; height: 400px;"></div>
  <div ref="female_registered_chart" class="chart-container_2" style="min-width: 600px; height: 400px;"></div>
  <div ref="male_de_facto_chart" class="chart-container_3" style="min-width: 600px; height: 400px;"></div>
  <div ref="female_de_facto_chart" class="chart-container_4" style="min-width: 600px; height: 400px;"></div>
  <div ref="male_not_married_chart" class="chart-container_5" style="min-width: 600px; height: 400px;"></div>
  <div ref="female_not_married_chart" class="chart-container_6" style="min-width: 600px; height: 400px;"></div>
  <div ref="male_pie_chart" class="chart-container_7" style="min-width: 600px; height: 400px;"></div>
  <div ref="female_pie_chart" class="chart-container_8" style="min-width: 600px; height: 400px;"></div>
  <div ref="people_total_chart" class="chart-container_9" style="min-width: 1200px; height: 800px;"></div>


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
      sa2_male_de_facto: [0, 0, 0, 0, 0, 0, 0, 0, 0],
      sa2_female_de_facto: [0, 0, 0, 0, 0, 0, 0, 0, 0],
      sa2_male_not_married: [0, 0, 0, 0, 0, 0, 0, 0, 0],
      sa2_female_not_married: [0, 0, 0, 0, 0, 0, 0, 0, 0],
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


      maleRegisteredTotal:0,
      maleDefactoTotal:0,
      maleNotMarriedTotal: 0,
      femaleRegisteredTotal: 0,
      femaleDefactoTotal: 0,
      femaleNotMarriedTotal: 0,

      male_chart: null,
      male_chart_2:null,
      male_chart_3: null,
      male_chart_4: null,
      female_chart: null,
      female_chart_2: null,
      female_chart_3: null,
      female_chart_4: null,
      people_chart: null,


    };
  },
  methods: {

    async get_data() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/brisbane/305011112');
        let jsonData = response.data;


        this.sa2_male_registered = [
          jsonData.male.married.m_15_19_yr_marrd_reg_marrge,
          jsonData.male.married.m_20_24_yr_marrd_reg_marrge,
          jsonData.male.married.m_25_34_yr_marrd_reg_marrge,
          jsonData.male.married.m_35_44_yr_marrd_reg_marrge,
          jsonData.male.married.m_45_54_yr_marrd_reg_marrge,
          jsonData.male.married.m_55_64_yr_marrd_reg_marrge,
          jsonData.male.married.m_65_74_yr_marrd_reg_marrge,
          jsonData.male.married.m_75_84_yr_marrd_reg_marrge,
          jsonData.male.married.m_85ov_marrd_reg_marrge,
        ];
        this.sa2_female_registered = [
          jsonData.female.married.f_15_19_yr_marrd_reg_marrge,
          jsonData.female.married.f_20_24_yr_marrd_reg_marrge,
          jsonData.female.married.f_25_34_yr_marrd_reg_marrge,
          jsonData.female.married.f_35_44_yr_marrd_reg_marrge,
          jsonData.female.married.f_45_54_yr_marrd_reg_marrge,
          jsonData.female.married.f_55_64_yr_marrd_reg_marrge,
          jsonData.female.married.f_65_74_yr_marrd_reg_marrge,
          jsonData.female.married.f_75_84_yr_marrd_reg_marrge,
          jsonData.female.married.f_85ov_marrd_reg_marrge,
        ];
         this.sa2_male_de_facto = [
          jsonData.male.de_facto.m_15_19_yr_married_de_facto,
          jsonData.male.de_facto.m_20_24_yr_married_de_facto,
          jsonData.male.de_facto.m_25_34_yr_married_de_facto,
          jsonData.male.de_facto.m_35_44_yr_married_de_facto,
          jsonData.male.de_facto.m_45_54_yr_married_de_facto,
          jsonData.male.de_facto.m_55_64_yr_married_de_facto,
          jsonData.male.de_facto.m_65_74_yr_married_de_facto,
          jsonData.male.de_facto.m_75_84_yr_married_de_facto,
          jsonData.male.de_facto.m_85ov_married_de_facto,
        ];

        this.sa2_female_de_facto = [
          jsonData.female.de_facto.f_15_19_yr_married_de_facto,
          jsonData.female.de_facto.f_20_24_yr_married_de_facto,
          jsonData.female.de_facto.f_25_34_yr_married_de_facto,
          jsonData.female.de_facto.f_35_44_yr_married_de_facto,
          jsonData.female.de_facto.f_45_54_yr_married_de_facto,
          jsonData.female.de_facto.f_55_64_yr_married_de_facto,
          jsonData.female.de_facto.f_65_74_yr_married_de_facto,
          jsonData.female.de_facto.f_75_84_yr_married_de_facto,
          jsonData.female.de_facto.f_85ov_married_de_facto,

        ];

        this.sa2_male_not_married = [
          jsonData.male.not_married.m_15_19_yr_not_married,
          jsonData.male.not_married.m_20_24_yr_not_married,
          jsonData.male.not_married.m_25_34_yr_not_married,
          jsonData.male.not_married.m_35_44_yr_not_married,
          jsonData.male.not_married.m_45_54_yr_not_married,
          jsonData.male.not_married.m_55_64_yr_not_married,
          jsonData.male.not_married.m_65_74_yr_not_married,
          jsonData.male.not_married.m_75_84_yr_not_married,
          jsonData.male.not_married.m_85ov_not_married,
        ];

         this.sa2_female_not_married = [
          jsonData.female.not_married.f_15_19_yr_not_married,
          jsonData.female.not_married.f_20_24_yr_not_married,
          jsonData.female.not_married.f_25_34_yr_not_married,
          jsonData.female.not_married.f_35_44_yr_not_married,
          jsonData.female.not_married.f_45_54_yr_not_married,
          jsonData.female.not_married.f_55_64_yr_not_married,
          jsonData.female.not_married.f_65_74_yr_not_married,
          jsonData.female.not_married.f_75_84_yr_not_married,
          jsonData.female.not_married.f_85ov_not_married,
        ];

        const processedData = [];

        for (const age of this.ageGroups) {
          const ageFormatted = age.replace('-', '_');
          const ageKey = age === "85+" ? "p_85ov" : `p_${ageFormatted}_yr`;

          this.people_marriedArray.push(jsonData.people.married[`${ageKey}_marrd_reg_marrge`]);
          this.people_deFactoArray.push(jsonData.people.de_facto[`${ageKey}_married_de_facto`]);
          this.people_notMarriedArray.push(jsonData.people.not_married[`${ageKey}_not_married`]);
      }

         console.log(this.people_notMarriedArray);


        this.maleRegisteredTotal = this.sa2_male_registered.reduce((acc, cur) => acc + cur, 0);
        this.maleDefactoTotal = this.sa2_male_de_facto.reduce((acc, cur) => acc + cur, 0);
        this.maleNotMarriedTotal = this.sa2_male_not_married.reduce((acc, cur) => acc + cur, 0);
        this.femaleRegisteredTotal = this.sa2_female_registered.reduce((acc, cur) => acc + cur, 0);
        this.femaleDefactoTotal = this.sa2_female_de_facto.reduce((acc, cur) => acc + cur, 0);
        this.femaleNotMarriedTotal = this.sa2_female_not_married.reduce((acc, cur) => acc + cur, 0);

        this.initChart(this.male_chart,this.sa2_male_registered,'#1a78c2','Male Registered Marriages')
        this.initChart(this.female_chart,this.sa2_female_registered,'#f59ca9','Female Registered Marriages')
        this.initChart(this.male_chart_2,this.sa2_male_de_facto,'#1a78c2','Male In De Facto Relationship')
        this.initChart(this.female_chart_2,this.sa2_female_de_facto,'#f59ca9','Female In De Facto Relationship')
        this.initChart(this.male_chart_3, this.sa2_male_not_married, '#1a78c2', 'Male Not Married');
        this.initChart(this.female_chart_3, this.sa2_female_not_married, '#f59ca9', 'Female Not Married');

        this.initChart2(this.male_chart_4,this.maleRegisteredTotal,this.maleDefactoTotal,this.maleNotMarriedTotal,'Marital Status of Males')
        this.initChart2(this.female_chart_4,this.femaleRegisteredTotal,this.femaleDefactoTotal,this.femaleNotMarriedTotal,'Marital Status of Females')

        this.initChart3(this.people_chart, this.ageGroups,this.people_marriedArray,this.people_deFactoArray,this.people_notMarriedArray,'Marital Status of West End')

      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    initChart(chartInstance, chartData, barColor,titleText) {


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
            data: this.ageGroups,
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
            data: chartData,
            itemStyle: {
              color: barColor
            },
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

    // console.log(this.$refs.male_registered_chart)
    this.male_chart = echarts.init(this.$refs.male_registered_chart);
    this.female_chart= echarts.init(this.$refs.female_registered_chart);
    this.male_chart_2 = echarts.init(this.$refs.male_de_facto_chart);
    this.female_chart_2 = echarts.init(this.$refs.female_de_facto_chart);
    this.male_chart_3 = echarts.init(this.$refs.male_not_married_chart);
    this.female_chart_3= echarts.init(this.$refs.female_not_married_chart);
    this.male_chart_4 = echarts.init(this.$refs.male_pie_chart);
    this.female_chart_4 = echarts.init(this.$refs.female_pie_chart);
    this.people_chart=echarts.init(this.$refs.people_total_chart);
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
.chart-container_3 {
  position: absolute;
  left: 100px;
  top: 600px;
  width: 500px;
  height: 400px;
}
.chart-container_4 {
  position: absolute;
  left: 800px;
  top: 600px;
  width: 500px;
  height: 400px;
}
.chart-container_5 {
  position: absolute;
  left: 100px;
  top: 1050px;
  width: 500px;
  height: 400px;
}
.chart-container_6 {
  position: absolute;
  left: 800px;
  top: 1050px;
  width: 500px;
  height: 400px;
}
.chart-container_7 {
  position: absolute;
  left: 100px;
  top: 1500px;
  width: 500px;
  height: 400px;
}
.chart-container_8 {
  position: absolute;
  left: 800px;
  top: 1500px;
  width: 500px;
  height: 400px;
}
.chart-container_9 {
  position: absolute;
  left: 100px;
  top: 1950px;
  width: 500px;
  height: 400px;
}
</style>
