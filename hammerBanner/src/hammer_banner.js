$.fn.hammer_banner = function () {

  var self = this;

  //创建遮罩层
  var hammerLayout = document.createElement("div");
  this.parent().append(hammerLayout);
  $(hammerLayout).attr("style", "width: 100%; height: 100%; position: absolute; background: yellow; z-index: 2; opacity: 0;");

  //绑定事件
  var stageW = this.width();
  var stageH = this.height();

  $(hammerLayout).on("mousemove", function (e) {
    var tmp_1 = ((e.offsetX - stageW/2)/stageW) * 1.05;
    var tmp_2 = ((e.offsetY - stageH/2)/stageH) * -4;

    // console.log(tmp_2);

    self
      .attr("style", "transform:rotateY("+tmp_1+"deg) rotateX("+ tmp_2 +"deg);");
      $(".warp")
   
  }).on("mouseout", function (e) {
    self
      .attr("style", "transform:rotateY(0deg) rotateX(0deg);");
  });

  return this;

}
