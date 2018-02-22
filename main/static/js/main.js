
function initBrandSelector() {
  // look up select element with groups and attach our even handler
  // on field "change" event
  $('#brand-selector select').change(function(event){
    // get value of currently selected group option
    var brand = $(this).val();

    if (brand) {
      // set cookie with expiration date 1 year since now;
      // cookie creation function takes period in days
      $.cookie('current_brand', brand, {'path': '/', 'expires': 365});
    } else {
      // otherwise we delete the cookie
      $.removeCookie('current_brand', {'path': '/'});
    }

    // and reload a page
    location.reload(true);

    return true;
  });
}

$(document).ready(function(){
  initBrandSelector();

});
