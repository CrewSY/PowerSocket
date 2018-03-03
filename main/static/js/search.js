function initSearchForm(){
    $('#searchsubmit').on('click', function(e){
    e.preventDefault();
    q = $('#search').val();
    updateContentBySearch(q);
  });
}


function updateContentBySearch(q) {
    var url = "/search_products/" + q
    $('.product_content').load(url, function() {
        initBuyButton();
        changeIcons();
    });
}

$(document).ready(function(){
    initSearchForm();
});
