function initBrandSelector() {
  $('.tab button').click(function(){
    var brand = $(this).val();
    if (brand) {
      $.cookie('current_brand', brand, {'path': '/', 'expires': 365});
    } else {
      $.removeCookie('current_brand', {'path': '/'});
    }
    location.reload(true);
    return true;
  });
}


$(document).ready(function(){
  var brand = $.cookie('current_brand');
  if (brand) {
    $('.tab button[value=' + brand + ']').addClass("active");
  }

  initBrandSelector();

});
