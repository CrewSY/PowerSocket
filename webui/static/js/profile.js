function updateUserData(){

    $('#update-profile').click(function(event){
        event.preventDefault();
        var data = {};

        data["csrfmiddlewaretoken"] = $('#profile-form [name="csrfmiddlewaretoken"]').val();
        data["first_name"] = $('#first-name').val();
        if(data.first_name == ''){
            data["first_name"] = $('#first-name').attr('placeholder');
        }
        data["last_name"] = $('#last-name').val();
        if(data.last_name == ''){
            data["last_name"] = $('#last-name').attr('placeholder');
        }
        data["phone_number"] = $('#phone-number').val();
        if(data.phone_number == ''){
            data["phone_number"] = $('#phone-number').attr('placeholder');
        }
        data["address"] = $('#address').val();
        if(data.address == ''){
            data["address"] = $('#address').attr('placeholder');
        }
        var url = $('#update-profile').attr('action');

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            success: location.reload(),
        });
    });
}

$(document).ready(function(){
    updateUserData();
});
