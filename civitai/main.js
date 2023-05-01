// 展开元素
setInterval(function() {
    var targetElements = document.querySelectorAll(".icon-tabler-eye");
    for (var i = 0; i < targetElements.length; i++) {
        targetElements[i].parentNode.click();
    }
  }, 1000); // 每 1000 毫秒检测一次
