function initBuyButton(){
    $('.basket-adding').click(function(e){
        e.preventDefault();
        var test = $(this);
        var product_id = test.data("product_id");
        var url = test.attr("action");

        basketUpdating(product_id, url);
    });
}


function basketUpdating(product_id, url){
    var data = {};
    var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();

    data["csrfmiddlewaretoken"] = csrf_token;
    data.product_id = product_id;

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
    });
}


function changeIcons() {
  $('.fa-cart-arrow-down').click(function(){
    $(this).removeClass('fa-cart-arrow-down').addClass('fa-cart-plus');
  });
}




$(document).ready(function(){
    initBuyButton();
    changeIcons();
});
