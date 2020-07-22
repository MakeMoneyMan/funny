<template>
  <div class="cheer">
    <div class="box">
      <div class="number">{{num}}</div>
      <div class="plus" :class="plus1?'fadeInUp':''">
        <img src="@/assets/plus1.png" alt="">
      </div>
      <img class="btn" style="margin-top: 40px;" src="@/assets/help.png" alt="" @click="showCheerMain=true">
      <img class="btn" src="@/assets/myheop.png" alt="" @click="$router.push('/first')">
    </div>
    <div class="cover" v-if="showCheerMain">
    </div>

    <div class="cheerMain" v-if="showCheerMain">

      <div class="roketPlus">
        <img class="fadeInUp" v-if="cheering && fuel >= -268" src="@/assets/plus2.png" alt="">
      </div>

      <div class="fueling">
        <template v-if="cheering">加油中</template>
        <template v-else-if="fuel <= -268">加油完成</template>
        
      </div>
      <div class="water" :style="`background-position: center ${fuel}px`">
      </div>
      <div class="roket">
      </div>
      <div class="part">
      </div>
      <div class="gun" :class="cheering?'gunCheering':''">
      </div>
      <div class="smoke">
        <img class="pulse" v-if="fuel <= -268" src="@/assets/smoke.png" alt="">
      </div>

      <img class="btn" style="top: 70%;" src="@/assets/fuel.png" alt="" @click="cheerFun">
      <img class="btn" src="@/assets/back_2.png" alt="" @click="goBack">

    </div>
  </div>
</template>

<script>
export default {
  name: 'cheer',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      num: 1998,
      intervalClear: 0,
      plus1: false,
      cheering: false,
      showCheerMain: false,
      fuel: -100
    }
  },
  computed:{
    hopeIndex(){
      return this.$store.state.cheer
    }
  },
  methods: {
    cheerFun(index) {
      if(this.cheering) return
      this.cheering = true
      this.intervalClear = setInterval(()=>{
        if(this.fuel <= -268){
          clearInterval(this.intervalClear)
          this.cheering = false
          // this.cheerSuccess()
        } else {
          this.fuel += -10
        }
      }, 300)
    },
    cheerSuccess() {
      if(this.plus1 == true) return
      this.plus1 = true
      setTimeout(()=>{
        // this.plus1 = false
        this.num++
      }, 1000)
    },
    goBack(){
      this.showCheerMain = false
      if(this.fuel <= -208){
        this.cheerSuccess()
      } else {
      }
    }
  },
  mounted() {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.cheer {
  width: 100%;
  height: 100%;
  background-image: url('~@/assets/cheer_bg.png');
  background-size: cover;
  background-position: center bottom;
  .box {
    width: 750px;
    height: 1380px;
    background-image: url('~@/assets/cheer_main.png');
    background-size: 100%;
    background-repeat: no-repeat;
    position: fixed;
    left: 50%;
    top: 50%;
    transform: translate(-375px, -690px);
    padding-top: 740px;
    .number {
      width: 750px;
      margin-bottom: 60px;
      text-align: center;
      font-size: 46px;
      padding-left: 10px;
      color: #01446d;
    }
    .plus {
      position: absolute;
      top: 700px;
      right: 240px;
      opacity: 0;
      animation-duration: 1s;
      animation-iteration-count: 1;
      // animation-fill-mode: forwards;
      img {
        width: 100%;
      }
    }
    .btn {
      width: 487px;
      padding-left: 160px;
      margin-bottom: 30px;
    }
  }
  .cover {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    background-size: 90%;
    background-repeat: no-repeat;
    background-position: center center;
    position: fixed;
    left: 0;
    top: 0;
    z-index: 9;

  }
  .cheerMain {
    width: 750px;
    height: 1300px;
    background-image: url('~@/assets/cheer_box.png');
    background-size: 90%;
    background-repeat: no-repeat;
    background-position: center center;
    position: fixed;
    left: 50%;
    transform: translateX(-50%);
    top: 0;
    z-index: 10;
    .fueling {
      width: 300px;
      height: 100px;
      position: absolute;
      top: 250px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 10;
      font-size: 48px;
      color: #044f87;
      text-align: center;
      img {
        width: 100%;
        animation-duration: 1s;
        animation-iteration-count: infinite;
      }
    }
    .roketPlus {
      width: 100px;
      height: 100px;
      position: absolute;
      top: 26%;
      left: 50%;
      transform: translateX(-50%);
      z-index: 10;
      img {
        width: 100%;
        opacity: 0;
        animation-duration: 1s;
        animation-iteration-count: 1;
      }
    }
    .water {
      width: 220px;
      height: 500px;
      position: absolute;
      background-image: url('~@/assets/shuiping.png');
      background-size: 90%;
      background-repeat: no-repeat;
      background-position: center 33px;//208到顶 
      top: 320px;
      left: 50%;
      transform: translateX(-50%);
      transition: 1s;
    }
    .roket {
      width: 410px;
      height: 510px;
      position: absolute;
      background-image: url('~@/assets/roket.png');
      background-size: 90%;
      background-repeat: no-repeat;
      background-position: center 0px;
      top: 320px;
      left: 50%;
      transform: translateX(-50%);
    }
    .part {
      width: 89%;
      height: 500px;
      position: absolute;
      background-image: url('~@/assets/part.png');
      background-size: 90%;
      background-repeat: no-repeat;
      background-position: center 0px;
      top: 520px;
      left: 50%;
      transform: translateX(-50%);
    }
    .gun {
      width: 200px;
      height: 500px;
      position: absolute;
      background-image: url('~@/assets/gun.png');
      background-size: 90%;
      background-repeat: no-repeat;
      background-position: center 0px;
      top: 685px;
      left: 545px;
      transform: translateX(-50%) rotate(38deg);
      transform-origin: 170px 115px;
      transition: 1s;
    }
    .smoke {
      width: 240px;
      height: 200px;
      position: absolute;
      top: 815px;
      left: 50%;
      transform: translateX(-50%);
      z-index: -1;
      img {
        width: 100%;
        animation-duration: 1s;
        animation-iteration-count: infinite;
      }
    }
    .gunCheering {
      transform: translateX(-50%) rotate(0deg);
    }
    .btn {
      width: 58%;
      position: absolute;
      top: 77%;
      left: 50%;
      transform: translateX(-50%);
    }
  }
}

</style>
