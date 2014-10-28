$(document).ready(function () {

        var hr = '<div class="col-lg-12" id="border"></div>';
        $('section > h2:first-child').after(hr);
//    var slideNum = $('.slide-number').text();
//    console.log(slideNum);
//    if (slideNum == '0') {
//        $('#btn_action').hide();
//        $('#btn_login').hide();
//    }

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
                'username': username,
                'url': url
            },
            success: function(response) {
                console.log(response);

            },
            error: function(response) {
                console.log(response);
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
                'username': username,
                'url': url
            },
            success: function(response) {
                console.log(response);

            },
            error: function(response) {
                console.log(response);
            }
        });
    });

    // FORM SUBMIT BUTTON
    $('#submit_q').on('click', function() {
    var username = $('#myProfile').data('username');
    var url = window.location.href; // or $(location).attr('href');
    var question = $('#the_question').val();
        console.log(url);
        $.ajax({
            url: '',
            type: 'POST',
            dataType: 'json',
            data: {
                'username': username,
                'url': url,
                'question': question
            },
            success: function(response) {
                $('#the_question').val('');
                console.log(response);

            },
            error: function(response) {
                console.log(response);
            }
        });
    });

});