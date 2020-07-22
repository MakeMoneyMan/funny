<template>
  <div class="chooseHope">
    <div class="box">
      <div class="btns">
        <ul>
          <li :class="hopeIndex==1?'checked':''">
            <img src="@/assets/mark_1.png" alt="" @click="chooseHopeFun(1)">
          </li>
          <li :class="hopeIndex==2?'checked':''">
            <img src="@/assets/mark_2.png" alt="" @click="chooseHopeFun(2)">
          </li>
          <li :class="hopeIndex==3?'checked':''">
            <img src="@/assets/mark_3.png" alt="" @click="chooseHopeFun(3)">
          </li>
          <li :class="hopeIndex==4?'checked':''">
            <img src="@/assets/mark_4.png" alt="" @click="chooseHopeFun(4)">
          </li>
          <li :class="hopeIndex==5?'checked':''">
            <img src="@/assets/mark_5.png" alt="" @click="chooseHopeFun(5)">
          </li>
          <li :class="hopeIndex==6?'checked':''">
            <img src="@/assets/mark_6.png" alt="" @click="chooseHopeFun(6)">
          </li>
          <li class="function">
            <img src="@/assets/back2.png" alt="" @click="$router.push('/enterText/back')">
            <img src="@/assets/publish.png" alt="" @click="$router.push('/result')">
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'chooseHope',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      num: 1998,
      intervalClear: 0
    }
  },
  computed:{
    hopeIndex(){
      return this.$store.state.chooseHope
    }
  },
  methods: {
    chooseHopeFun(index) {
      this.$store.dispatch('setChooseHopeFun', index)
    }
  },
  mounted() {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.chooseHope {
  width: 100%;
  height: 100%;
  background-image: url('~@/assets/bg_2.png');
  background-size: cover;
  background-position: center bottom;
  .box {
    width: 750px;
    height: 1280px;
    background-image: url('~@/assets/choose.png');
    background-size: 100%;
    background-repeat: no-repeat;
    position: fixed;
    left: 50%;
    top: 50%;
    transform: translate(-375px, -640px);
    .btns {
      width: 467px;
      padding-left: 170px;
      padding-top: 250px;
      img {
        width: 100%;
        height: 73px;
        margin-bottom: 50px;
      }
      .checked {
        position: relative;
        img {
          transform: scale(1.05);
        }
        &::after {
          content: '';
          width: 50px;
          height: 50px;
          background-image: url('~@/assets/pen.png');
          background-repeat: no-repeat;
          background-size: 50%;
          position: absolute;
          left: -12px;
          top: -21px;
        }
      }
      .function {
        img {
          width: 210px;
        }
        :nth-child(2) {
          float: right;
        }
      }
    }
  }
}

</style>
