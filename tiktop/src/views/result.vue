<template>
  <div class="result">
    <canvas id="canvas"></canvas>
    <div class="main" :style="isIpad? 'width: 50%;': ''">
      <img src="@/assets/pabulish_main.png" @load="imageOnload" id="img" alt="">
      <!-- <p class="on">鹅厂第 <span>20888</span> 位许下愿望的人</p> -->
    </div>
    <p class="save">长按保存图片</p>
  </div>
</template>

<script>
export default {
  name: 'result',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      changed: false,
      isIpad: false
    }
  },
  mounted(){
    // var canvas=document.getElementById('canvas');
    // var context=canvas.getContext('2d');
    // var image=new Image();
    
    // image.src=imageData;

    // image.οnlοad=function(){
    //   alert(123)
    //   context.drawImage(this, 10, 10);
    // };

    // var image = document.getElementById( 'img' );
    // image.src = 'http://pic.sc.chinaz.com/Files/pic/pic9/201912/zzpic22192_s.jpg';

  },
  methods:{
    imageOnload(event){
        if(this.changed) return

        var width = 686//document.body.offsetWidth > 375? 375: document.body.offsetWidth
        var height = 1126//document.body.offsetHeight > 800? 750: 660

        //ipad
        // if(document.body.offsetWidth > 767) {
        //   this.isIpad = true
        //   width = 375
        //   height = 750
        // }
        

        var proportion = width/ height

        // console.log(document.body.offsetWidth, document.body.offsetHeight)

        this.changed = true
        var image = document.getElementById( 'img' );
        var cas = document.createElement('canvas');
        cas.width = width
        cas.height = height
        var ctx = cas.getContext('2d');
        ctx.drawImage(event.target, 0, 0, width, height);
        
        // 设置字体
        ctx.font = "24px bold Microsoft YaHei";
        // 设置颜色
        ctx.fillStyle = "#3d3d3d";
        // 设置水平对齐方式
        ctx.textAlign = "left";
        // 设置垂直对齐方式
        ctx.textBaseline = "middle";
        // 绘制文字（参数：要写的字，x坐标，y坐标）
        ctx.fillText(`鹅厂第                位许下愿望的人`, 70, height*0.15);

        // 设置颜色
        ctx.fillStyle = "#5d87c9";
        // 设置垂直对齐方式
        ctx.textBaseline = "middle";
        // 绘制文字（参数：要写的字，x坐标，y坐标）
        ctx.fillText(`             ${Math.ceil(Math.random() * 100000)} `, 70, height*0.15);

        

        // 把画布的内容转换为base64编码格式的图片
        var data = cas.toDataURL( 'image/png', 1 );  //1表示质量(无损压缩)
        image.src = data;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.result {
  width: 100%;
  height: 100%;
  background-image: url('~@/assets/bg_3.png');
  background-size: cover;
  background-position: center bottom;
  .main {
    width: 686px;
    height: 1126px;
    position: fixed;
    top: 0%;
    left: 50%;
    transform: translateX(-50%);
    img {
      width: 686px;
      height: 1126px;
    }
    .on {
      position: absolute;
      z-index: 10;
      left: 10%;
      top: 9%;
      // transform: translateX(-50%);
      color: #3d3d3d;
      span {
        color: #5d87c9;
      }
    }
  }
  .save {
    position: fixed;
    z-index: 10;
    left: 50%;
    bottom: 10%;
    transform: translateX(-50%);
    color: #fff;
    text-shadow: 1px 1px #000;
  }
}
</style>
