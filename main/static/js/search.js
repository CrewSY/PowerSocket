function initSearchForm(){
    $('#search-submit').click(function(e){
    e.preventDefault();
    q = $('#search-input').val();
    updateContentBySearch(q);
  });
}


function updateContentBySearch(q) {
    var url = "/search_products/?";
    $("#product-content").load(
        url + $.param({search_by: q}), function() {
            initBuyButton();
            changeIcons();
        });
}

$(document).ready(function(){
    initSearchForm();
});
