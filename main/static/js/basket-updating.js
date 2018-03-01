function initBuyButton(){
    $('.button-buy').click(function(e){
        e.preventDefault();
        var test = $(this);
        var smartphone_id = test.data("smartphone_id");
        var url = test.attr("action");

        basketUpdating(smartphone_id, url);
    });
}


function basketUpdating(smartphone_id, url){
    var data = {};
    var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();

    data["csrfmiddlewaretoken"] = csrf_token;
    data.smartphone_id = smartphone_id;

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
    });
}


$(document).ready(function(){
    initBuyButton();
});
