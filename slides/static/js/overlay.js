$(document).ready(function () {

    // ACTIONS BUTTON
    $('#btn_action').on('click', function() {
    var title = $('section.present').slice(-1).find('h2').text();
        $('#myModalLabel').text(title);

    });

    // HELP BUTTON
    $('#help').on('click', function() {
    var username = $('#myProfile').data('username');
    var url = window.location.href; // or $(location).attr('href');

        console.log(url);
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

    // DONE BUTTON
    $('#done').on('click', function() {
    var username = $('#myProfilel').data('username');
    var url = window.location.href; // or $(location).attr('href');

        console.log(url);
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

    // FORM SUBMIT BUTTON
    $('#submit_q').on('click', function() {
    var username = $('#myProfile').data('username');
    var url = window.location.href; // or $(location).attr('href');

        console.log(url);
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