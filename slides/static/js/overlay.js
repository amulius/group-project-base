$(document).ready(function () {

    $('#btn_action').on('click', function() {
    var username = $('#myModalLabel').data('username');
    var url = 
        console.log(response);
        $.ajax({
            url: '',
            type: 'POST',
            dataType: 'json',
            data: {
                'username': username
            },
            success: function(response) {
                console.log(response);

            },
            error: function(response) {
                console.log(data);
            }
        });
    });

});