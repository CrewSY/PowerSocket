function initAccordion(){
  $('.wrapper>.tab').not(':first-of-type').hide();
  var findArticle = $('.wrapper>.header-tabs').next();
  findArticle.hide();
  $('.wrapper>.header-tabs').click(function() {
    var findArticle = $(this).next();
    var findWrapper = $(this).closest('.wrapper');
    if (findArticle.is(':visible')) {
      findArticle.slideUp(400);
      $(this).find('i').removeClass("fa-minus").addClass("fa-plus");
    }
    else {
      findWrapper.find('>.tab').slideUp('fast');
      findArticle.slideDown(400);
      $(this).find('i').removeClass("fa-plus").addClass("fa-minus");
    }
  });
}


function initBrandSelector(){
    $('.brand-button').click(function(event){
    event.preventDefault();
    var brand_id = $(this).data('brand_id');

    updateContent(brand_id);
  });
}


function updateContent(brand_id) {
  var url = "/update_content?";
  $("#product-content").load(
      url + $.param({brand_id: brand_id}), function() {
        initBuyButton();
        changeIcons();
    });
}


function updateContentBySearch(){
    $('#search-submit').click(function(e){
    e.preventDefault();
    q = $('#search-input').val();

    var url = "/search_products/?";
    $("#product-content").load(
        url + $.param({search_by: q}), function() {
            initBuyButton();
            changeIcons();
        });
  });
}


$(document).ready(function(){
  initAccordion();
  initBrandSelector();
  updateContentBySearch();
});
