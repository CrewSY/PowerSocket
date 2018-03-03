function initVotes(){
    $('.fa-star').click(function(e){
        e.preventDefault();
        var data = {};
        var csrf_token = $('#rating [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        data.vote = $(this).data("vote");
        data.product_id = $('#rating').data("product_id");
        var url = $('#rating').data("url");
        console.log(url);


        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: location.reload(),
        });

    });
}


$(document).ready(function(){
    initVotes();
});
