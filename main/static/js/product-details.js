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
    if(rating=='1'){
        $('#vote-1').addClass('checked');
    }
    if(rating=='2'){
        $('#vote-1').addClass('checked');
        $('#vote-2').addClass('checked');
    }
    if(rating=='3'){
        $('#vote-1').addClass('checked');
        $('#vote-2').addClass('checked');
        $('#vote-3').addClass('checked');
    }
    if(rating=='4'){
        $('#vote-1').addClass('checked');
        $('#vote-2').addClass('checked');
        $('#vote-3').addClass('checked');
        $('#vote-4').addClass('checked');
    }
    if(rating=='5'){
        $('#vote-1').addClass('checked');
        $('#vote-2').addClass('checked');
        $('#vote-3').addClass('checked');
        $('#vote-4').addClass('checked');
        $('#vote-5').addClass('checked');
    }
}


function initStar1(){
    $('#vote-1').mouseover(function(e){
        $(this).addClass('checked');
    });
    $('#vote-1').mouseleave(function(e){
        $(this).removeClass('checked');
    });
}

function initStar2(){
    $('#vote-2').mouseover(function(e){
        $('#vote-1').addClass('checked');
        $(this).addClass('checked');
    });
    $('#vote-2').mouseleave(function(e){
        $('#vote-1').removeClass('checked');
        $(this).removeClass('checked');
    });
}

function initStar3(){
    $('#vote-3').mouseover(function(e){
        $('#vote-1').addClass('checked');
        $('#vote-2').addClass('checked');
        $(this).addClass('checked');
    });
    $('#vote-3').mouseleave(function(e){
        $('#vote-1').removeClass('checked');
        $('#vote-2').removeClass('checked');
        $(this).removeClass('checked');
    });
}

function initStar4(){
    $('#vote-4').mouseover(function(e){
        $('#vote-1').addClass('checked');
        $('#vote-2').addClass('checked');
        $('#vote-3').addClass('checked');
        $(this).addClass('checked');
    });
    $('#vote-4').mouseleave(function(e){
        $('#vote-1').removeClass('checked');
        $('#vote-2').removeClass('checked');
        $('#vote-3').removeClass('checked');
        $(this).removeClass('checked');
    });
}

function initStar5(){
    $('#vote-5').mouseover(function(e){
        $('#vote-1').addClass('checked');
        $('#vote-2').addClass('checked');
        $('#vote-3').addClass('checked');
        $('#vote-4').addClass('checked');
        $(this).addClass('checked');
    });
    $('#vote-5').mouseleave(function(e){
        $('#vote-1').removeClass('checked');
        $('#vote-2').removeClass('checked');
        $('#vote-3').removeClass('checked');
        $('#vote-4').removeClass('checked');
        $(this).removeClass('checked');
    });
}

$(document).ready(function(){
    initVotes();
    initStar1();
    initStar2();
    initStar3();
    initStar4();
    initStar5();
    initRating();
});
