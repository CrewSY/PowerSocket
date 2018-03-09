function initBuyButton(){
    $('.basket-adding').click(function(e){
        e.preventDefault();
        var current_button = $(this);
        var product_id = current_button.data("product_id");
        var url = current_button.attr("action");

        basketUpdating(product_id, url);
    });
}


function basketUpdating(product_id, url){
    var data = {};
    data["csrfmiddlewaretoken"] = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
    data.product_id = product_id;

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
    });
}


function changeIcons() {
  $('.change-icon').click(function(){
    var button = $(this);
    button.prop("disabled", "disabled");
    button.find('i').removeClass('fa-cart-plus').addClass('fa-check-circle');
  });
}


function popupImage () {
    $('.popup').click(function (event){
        var modal = $('#myModal')[0];
        var img = $(this);
        var modalImg = $("#img01")[0];
        var captionText = $("#caption")[0];

            modal.style.display = "block";
            modalImg.src = this.src;
            captionText.innerHTML = this.alt;

        var span = $(".close")[0];

        span.onclick = function() {
          modal.style.display = "none";
        }
    });
}


$(document).ready(function(){
    initBuyButton();
    changeIcons();
    popupImage ();
});
