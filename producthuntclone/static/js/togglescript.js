var i=0;
function read(dots,more,btn){
  if (!i) {
    document.getElementById(more).style.display = "inline";
    document.getElementById(dots).style.display = "none";
    document.getElementById(btn).innerHTML = "read less"
    i=1;
  }
  else {
    document.getElementById(more).style.display = "none";
    document.getElementById(dots).style.display = "inline";
    document.getElementById(btn).innerHTML = "read more"
    i=0;
  }
}
