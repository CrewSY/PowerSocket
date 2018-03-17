window.onscroll = function() {myFunction()};

var header = document.getElementById("headerid");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}


$(document).ready(function() {
  $('.menu-trigger').click(function() {
    $('nav ul').slideToggle(500);
  });//end slide toggle

  $(window).resize(function() {
		if (  $(window).width() > 500 ) {
			$('nav ul').removeAttr('style');
		 }
	});//end resize
});//end ready
