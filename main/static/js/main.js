
function initBrandSelector() {
  $('.tab button').click(function(e){
    e.preventDefault();

    var brand = $(this).val();
    if (brand) {
      $.cookie('current_brand', brand, {'path': '/', 'expires': 365});

    } else {
      $.removeCookie('current_brand', {'path': '/'});
    }

    location.reload(true);

    $(this).addClass("active")

    return true;
  });
}


$(document).ready(function(){
  initBrandSelector();

});
