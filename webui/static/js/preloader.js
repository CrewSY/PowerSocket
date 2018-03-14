function initPreloader() {
	$('#before-load').find('i').fadeOut().end().delay(0).fadeOut(400);
}

$(window).on('load', function() {
	initPreloader();
});
