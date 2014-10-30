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


    $('.action_button').on('click', function() {
    var username = $('#myProfile').data('username');
    var url = window.location.pathname + window.location.hash; // or $(location).attr('href');
    var question = $('#the_question').val();
    var action = $(this).attr('id');
    var data = {
                'action': action,
                'username': username,
                'slide': url,
                'question_text': question
            };
    console.log($(this));
        console.log(url);
        $.ajax({
            url: '/student_actions/',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify(data),
            success: function(response) {
                console.log(response);

            },
            error: function(response) {
                console.log(response);
            }
        });
    });

});