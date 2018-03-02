function initQuantity(){
	$('.button_minus').click(function(e){
        e.preventDefault();
        var num_count = $(this).parent('.quantity_goods').find('.num_count');
        var qty = parseInt(num_count.val());
        var product_id = num_count.data("product_id");
        var url = num_count.attr("action");

        if (qty==1){
        	qty = 1;
        }
        else{
        	qty = qty - 1;
        }

        num_count.val(qty);
        updateQuantity(qty, product_id, url);
    });
    $('.button_plus').click(function(e){
        e.preventDefault();
        var num_count = $(this).parent('.quantity_goods').find('.num_count');
        var qty = parseInt(num_count.val());
        var product_id = num_count.data("product_id");
        var url = num_count.attr("action");
        qty = qty + 1;
        num_count.val(qty);
        updateQuantity(qty, product_id, url);
    });

}


function updateQuantity(qty, product_id, url){
    var data = {};
    var csrf_token = $('#quantity_goods [name="csrfmiddlewaretoken"]').val();
    data["csrfmiddlewaretoken"] = csrf_token;
    data.product_id = product_id;
    data.qty = qty;

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
    });

}


$(document).ready(function(){
    initQuantity();
});
