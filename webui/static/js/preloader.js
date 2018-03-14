function initPreloader() {
	$('#before-load').find('i').fadeOut().end().delay(200).fadeOut('slow');
}

$(window).on('load', function() {
	initPreloader();
});
