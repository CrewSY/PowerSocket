$(document).ready(function(){
    var form = $('#form_buying_product');


    function basketUpdating(product_id, nmb, is_delete){
        var data = {};
        data.smartphone_id = smartphone_id;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");

        console.log(data)
         $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
             },
             error: function(){
                 console.log("error")
             }
         })

    }


// function initBuyButton() {
//   var indicator = $('#ajax-progress-indicator');

//   $('.button-buy').click(function(event){
//     var sm = $(this);
//     $.ajax( {
//       url: {% url "button_buy" %},
//       type: 'POST',
//       async: true,
//       dataType: 'json',
//       data: {
//         'id': box.data('sm-id'),
//         'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
//       },
//       'beforeSend': function(xhr, settings){
//         indicator.show();
//       },
//       'error': function(xhr, status, error){
//         alert(error);
//         indicator.hide();
//       },
//       'success': function(data, status, xhr){
//         indicator.hide();
//       }
//     });
//   });
// }


// $(document).ready(function(){
//   initBuyButton();
// });
