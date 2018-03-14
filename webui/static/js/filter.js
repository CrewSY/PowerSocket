var brand = 0;
var category = 0;
var discount = 0;
var delivery_options = 0;
var sort = 0;


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
    brand_buttons = $('.brand-button');
    brand_buttons.click(function(event){
      event.preventDefault();
      brand_button = $(this);
      var brand_id = brand_button.data('brand_id');
      brand = brand_id;

      brand_buttons.removeClass('button-active');
      brand_button.addClass('button-active');

      updateContent();
  });
}


function initCategorySelector(){
    category_buttons = $('.category-button');
    category_buttons.click(function(event){
      event.preventDefault();
      category_button = $(this);
      var category_id = category_button.data('category_id');
      category = category_id;

      category_buttons.removeClass('button-active');
      category_button.addClass('button-active');

    updateContent();
  });
}


function initDiscountSelector(){
    discount_buttons = $('.discount-button');
    discount_buttons.click(function(event){
      event.preventDefault();
      discount_button = $(this);
      var discount_id = discount_button.data('discount_id');
      discount = discount_id;

      discount_buttons.removeClass('button-active');
      discount_button.addClass('button-active');

    updateContent();
  });
}


function initDeliverySelector(){
    $('input[type=radio][name=radio]').change(function() {
        var delivery_options_id = $(this).value;
        delivery_options = delivery_options_id;
        updateContent();
    });
}


function initSortSelector() {
  $('#dropdown select').change(function(event){
    var sort_id = $(this).val();
    sort = sort_id;

    updateContent();
  });
}


function updateContent() {
  var url = "/update_content?";
  $("#product-content").load(
      url + $.param({brand_id: brand,
                     category_id: category,
                     discount_id: discount,
                     delivery_options_id: delivery_options,
                     sort_id: sort}), function() {
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
  initCategorySelector();
  initDiscountSelector();
  initDeliverySelector();
  initSortSelector();
  updateContentBySearch();
});


 $(document).ajaxStart(function(){
    $("#loading").show();
 });

 $( document ).ajaxComplete(function() {
    $("#loading").fadeOut(400);
 });
