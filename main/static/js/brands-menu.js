function initAccordion(){
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


function initBrandSelector(){
    $('.tab button').on('click', function(event){
    event.preventDefault();
    var pk = $(this).val();
    update_content(pk);
  });
}


function update_content(pk) {
  var url = "/update_content/"+ pk;
  $('.product_content').load(url, function() {
    initBuyButton();
    changeIcons();
  });
}


$(document).ready(function(){
  initAccordion();
  initBrandSelector();
});
