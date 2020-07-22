<template>
  <div class="first">
    <div class="main">
      <img src="@/assets/first_main.png" class="img fadeInDown" alt="">
      <img src="@/assets/stay.png" class="btn fadeIn" alt="" @click="$router.push('/enterText')">
    </div>
  </div>
</template>

<script>
export default {
  name: 'first',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.first {
  width: 100%;
  height: 100%;
  background-image: url('~@/assets/first.png');
  background-size: cover;
  background-position: center center;
  .main {
    width: 600px;
    height: 1000px;
    left: 50%;
    top: 50%;
    position: fixed;
    transform: translate(-300px, -500px);
    .img {
      width: 100%;
      animation-duration: 2s;
      animation-iteration-count: 1;
    }
    .btn {
      width: 360px;
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      opacity: 0;
      animation-delay: 2s;
      animation-duration: 1s;
      animation-iteration-count: 1;
      animation-fill-mode: forwards;
    }
  }
}
</style>
