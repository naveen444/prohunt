$(".toggle-1").on("click", function () {
  $(".container-1").stop().addClass("active");
});

$(".close-1").on("click", function () {
  $(".container-1").stop().removeClass("active");
});

$('#about').on('input', function () {
  this.style.height = 'auto';
  this.style.height = (this.scrollHeight) + 'px';
});

$(document).ready(function(){
  if($("#about")[0]){
    console.log($("#about")[0].scrollHeight);
    $("#about").height(($('#about')[0].scrollHeight)+'px');
  }
});

var userinp = document.querySelector("#photo")
var userimage = document.querySelector("#userimg")

if(userinp){
  userinp.addEventListener("change",function(){
    changeimg(this);
  });
}

function changeimg(input) {
  var reader;
  console.log('changeimg working');
  if(userinp.files && userinp.files[0]) {
    console.log('inside if');
    reader = new FileReader();

    reader.onload = function(e) {
      userimage.setAttribute('src', e.target.result);
    }

    reader.readAsDataURL(input.files[0]);
  }
}
