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

function accordion(){
  $('.wrapper>.tab').not(':first-of-type').hide();
  $('.wrapper>.header-tabs').click(function() {

    var findArticle = $(this).next();
    var findWrapper = $(this).closest('.wrapper');
    if (findArticle.is(':visible')) {
      findArticle.slideUp('fast');
    }
    else {
      findWrapper.find('>.tab').slideUp('fast');
      findArticle.slideDown('fast');
    }
  });
}


$(document).ready(function(){
  var brand = $.cookie('current_brand');
  if (brand) {
    $('.tab button[value=' + brand + ']').addClass("active");
  }
  initBrandSelector();
  accordion();
});
