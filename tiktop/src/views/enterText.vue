
<template>
  <div class="enterText" >
    
    <input type="file" style="opacity: 0;" ref="file" accept="image/png,image/jpg,image/jpeg" @change="change($event)">
    
      <template v-if="!isShow">
        <div class="body enterBg">
            <textarea class="textarea" name="" id="" v-model="text"></textarea>
            <img class="upload" @click="$refs.file.click()" v-if="imageDataCp" :src="imageDataCp" alt="" >
            <img class="upload" @click="$refs.file.click()" id="img" v-if="!imageDataCp" src="@/assets/add.png" alt="" >
            <img class="btn" src="@/assets/preview.png" alt="" @click="previewFun">
        </div>
      </template>
      <template v-else>
        <div class="body showBg">
          <div class="board">{{text ? text: '我的愿望以图为鉴！'}}</div>
          <img :style="!text?'width: 222px':''" class="upload" :src="imageDataCp" alt="" >
          <img class="btn backBtn" src="@/assets/back.png" alt="" @click="isShow=false">
          <img class="btn markBtn" src="@/assets/mark.png" alt="" @click="$router.push('/chooseHope')">
        </div>
      </template>

  </div>
</template>

<script>
export default {
  name: 'enterText',
  data () {
    return {
      isShow: false,
      text: ''
    }
  },
  computed: {
    imageDataCp() {
      return this.$store.state.imageData
    }
  },
  watch:{
    text(newText, old) {
      if(newText.length > 120) this.text = newText.substr(0, 120)
    }
  },
  methods : {
    change( event ) {
        let image = document.getElementById('img'); //预览对象
        this.clip(event , {
          resultObj : image,
          aspectRatio : 1, 
          result : result=>{
            this.$store.dispatch('setImageFun', result)
          }
        })
    },
    previewFun(){
      if(this.imageDataCp) {
        this.isShow = true
      } else {
        alert('请先上传图片')
      }
    }
  },
  mounted() {
    let isBack = this.$route.params
    if(Object.keys(isBack).length > 0) {
      this.isShow = true
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.enterText {
  width: 100%;
  height: 100%;
  background-image: url('~@/assets/bg.png');
  background-size: cover;
  background-position: center bottom;
  position: relative;
  overflow: hidden;
  .enterBg {
    background-image: url('~@/assets/enter.png');
  }
  .showBg {
    background-image: url('~@/assets/show_text.png');
  }
  .body {
    width: 750px;
    height: 1380px;
    background-size: 100%;
    background-repeat: no-repeat;
    background-position: center 60px;
    position: fixed;
    left: 50%;
    top: 50%;
    transform: translate(-375px, -690px);
    position: absolute;
    .board,
    .textarea {
      background: #fff;
      padding: 10px;
      width: 565px;
      height: 300px;
      font-size: 28px;
      position: absolute;
      left: 50%;
      top: 455px;
      transform: translateX(-50%);
      line-height:initial;
      overflow: hidden;
      word-wrap: break-word;
    }
    .board {
      top: 15%;
    }
    .upload {
      position: absolute;
      width: 290px;
      height: 290px;
      left: 50%;
      top: 815px;
      transform: translateX(-50%);
    }
    .board {
      background: none;
    }
    .btn {
      position: absolute;
      width: 240px;
      height: 70px;
      left: 50%;
      top: 1135px;
      transform: translateX(-50%);
    }
    .backBtn {
      bottom: 30%;
    }
    .markBtn {

    }
  }
  .showBg {
    height: 1380px;
    transform: translate(-375px, -700px);
    background-position: center 0px;
    .board {
      width: 504px;
      font-family: Arial Bold;
      font-size: 28px;
      line-height: 40px;
      top: 220px;
    }
    .upload {
      top: 490px;
      width: 385px;
      height: 385px;
    }
    .backBtn {
      width: 328px;
      height: 70px;
      top: 919px;
    }
    .markBtn {
      width: 328px;
      height: 70px;
      top: 1025px;
    }
  }
}

</style>
