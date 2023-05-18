
<template>
  <div class="center">
    <h1>Welcome to our website</h1>
    <p>Please select the city in the navigation bar</p>
  </div>
</template>
<script>
export default {
  name: "Welcome"
}
</script>
<style scoped>
h1 {
  font-size: 2rem;
  margin-top: 3rem;
  margin-bottom: 1.5rem;
}

p {
  font-size: 1.5rem;
  margin-bottom: 2rem;
}
.center {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>