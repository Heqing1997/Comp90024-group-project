<template>
  <h3>adelaide_cbd</h3>

</template>

<script>
import axios from 'axios';

export default {
  name: 'Adelaide_cbd',
  data() {
    return {
      sa2Data: null,

    };
  },
  async created() {
    try {
      const response = await axios.get('http://127.0.0.1:5000/adelaide/401011001');
      this.sa2Data = response.data;
      console.log(this.sa2Data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  },
};
</script>

<style scoped>

</style>