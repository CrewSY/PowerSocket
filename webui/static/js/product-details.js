function initVotes(){
    $('.fa-star').click(function(e){
        e.preventDefault();
        var data = {};
        var csrf_token = $('#rating [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        data.vote = $(this).data("vote");
        data.product_id = $('#rating').data("product_id");
        var url = $('#rating').data("url");


        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: location.reload(),
        });

    });
}


function initRating(){
    rating = $('#rating').data("rating");
    $(".fa-star").each(function( index ) {
        if (index <= rating){
            $(this).addClass('checked');
        }
        else{
            $(this).removeClass('checked');
        }
    });
}


function initStars(){
    buttons = $(".fa-star");
    buttons.mouseover(function(){
        button = $(this);
        buttons.each(function(index){
            if (button.attr("id") >= $(this).attr("id")){
                $(this).addClass('checked');
            }
            else{
                $(this).removeClass('checked');
            }
        });
    });
    buttons.mouseleave(function(){
        initRating();
    });
}


$(document).ready(function(){
    initVotes();
    initStars();
    initRating();
});
