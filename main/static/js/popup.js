function popupImage () {
	$('.popup').click(function (event){
		var modal = $('#myModal')[0];
		var img = $(this);
		var modalImg = $("#img01")[0];
		var captionText = $("#caption")[0];

		    modal.style.display = "block";
		    modalImg.src = this.src;
		    captionText.innerHTML = this.alt;

		var span = $(".close")[0];

		span.onclick = function() {
		  modal.style.display = "none";
		}
	});
}

$(document).ready(function (){
	popupImage ();
});
