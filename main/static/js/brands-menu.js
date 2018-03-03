function initAccordion(){
  $('.wrapper>.tab').not(':first-of-type').hide();
  var findArticle = $('.wrapper>.header-tabs').next();
  findArticle.hide();
  $('.wrapper>.header-tabs').click(function() {
    var findArticle = $(this).next();
    var findWrapper = $(this).closest('.wrapper');
    if (findArticle.is(':visible')) {
      findArticle.slideUp(600);
      $(this).find('i').removeClass("fa-minus").addClass("fa-plus");
    }
    else {
      findWrapper.find('>.tab').slideUp('fast');
      findArticle.slideDown(600);
      $(this).find('i').removeClass("fa-plus").addClass("fa-minus");
    }
  });
}



function initBrandSelector(){
    $('.tab button').on('click', function(event){
    event.preventDefault();
    var pk = $(this).val();
    updateContent(pk);
  });
}


function initSkipButton(){
  $('#skipbutton').on('click', function(event){
    event.preventDefault();
    updateContent('skip');
  });
}


function updateContent(pk) {
  var url = "/update_content/"+ pk;
  $('.product_content').load(url, function() {
    initBuyButton();
    changeIcons();
    $('.tab button').each(function() {
        $( this ).removeClass("active");
    });
    $('.tab button[value=' + pk + ']').addClass("active");
  });
}


$(document).ready(function(){
  initAccordion();
  initBrandSelector();
  initSkipButton();
});
