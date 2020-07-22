<template>
  <div class="init">
    <div class="box">
      <div class="text">{{num}}</div>
    </div>
    <div class="loading">
      <img src="@/assets/first_main.png"  alt="">
      <img src="@/assets/stay.png" >
      <img src="@/assets/preview.png" >
      <img src="@/assets/back.png" >
      <img src="@/assets/mark.png" >
      <img src="@/assets/first.png" >
      <img src="@/assets/pabulish_main.png" >
      <img src="@/assets/bg.png" >
      <img src="@/assets/bg_2.png" >
      <img src="@/assets/bg_3.png" >
    </div>
  </div>
</template>

<script>
export default {
  name: 'init',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      num: 1998,
      intervalClear: 0
    }
  },
  mounted() {
    this.intervalClear = setInterval(()=>{
      this.num++
      if(this.num>2017) {
        clearInterval(this.intervalClear)
        this.$router.push('/first')
      }
    }, 200)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.init {
  width: 100%;
  height: 100%;
  background-image: url('~@/assets/init.png');
  background-size: cover;
  background-position: center center;
  .box {
    width: 262px;
    height: 50px;
    background-image: url('~@/assets/2018.png');
    background-size: 100%;
    background-repeat: no-repeat;
    position: fixed;
    left: 50%;
    top: 54%;
    transform: translateX(-50%);
    .text {
      color: #000;
      letter-spacing: 51px;
      padding: 3px 0 0 16px;
      font-size: 32px;
    }
  }
  .loading {
    display: none;
    opacity: 0;
  }
}

</style>
