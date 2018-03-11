var brand = 0;
var category = 0;
var discount = 0;
var delivery_options = 0;


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
    brand = brand_id;

    updateContent();
  });
}


function initCategorySelector(){
    $('.category-button').click(function(event){
    event.preventDefault();
    var category_id = $(this).data('category_id');
    category = category_id;

    updateContent();
  });
}


function initDiscountSelector(){
    $('.discount-button').click(function(event){
    event.preventDefault();
    var discount_id = $(this).data('discount_id');
    discount = discount_id;

    updateContent();
  });
}


function updateContent() {
  var url = "/update_content?";
  $("#product-content").load(
      url + $.param({brand_id: brand,
                     category_id: category,
                     discount_id: discount}), function() {
        initBuyButton();
        changeIcons();
    });
    console.log(category, brand, discount);
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
  initCategorySelector();
  initDiscountSelector();
  updateContentBySearch();
});
