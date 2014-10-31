$(document).ready(function () {

//        $('body').find('#button_action').append('<button type="button" class="btn btn-primary btn_action" data-toggle="modal" data-target="#myModal">Actions</button>');
//        $('body').find('#button_login').append("<a href='/account/'><button id='btn_login' type='button' class='btn btn-primary btn-lg btn-block'>Student Login</button></a>");
        var loggedIn = $('#button_action').filter('[data-type="logged_in"]').length;
        if(loggedIn){
            $('section > h2:first-child').append('<button type="button" class="btn btn-primary btn_action" data-toggle="modal" data-target="#myModal">Actions</button>');
        }
        else{
            $('section > h2:first-child').append("<a href='/account/'><button id='btn_login' type='button' class='btn btn-primary btn_action'>Student Login</button></a>");
        }

//      // add blue keyline in 100% width under H2 and Action button
        var hr = '<div class="col-lg-12" id="border"></div>';
        $('section > h2:first-child').after(hr);

//      //this is for making the edit profile image as the upload button
        $("#upfile1").click(function () {
            $("#file1").trigger('click');
        });

//      // try to hide button on the first blue slides, requiring page reload ***
//      var slideNum = $('.slide-number').text();
//      console.log(slideNum);
//      if (slideNum == '0') {
//        $('#btn_action').hide();
//        $('#btn_login').hide();
//      }

    // ACTIONS BUTTON
    $('.btn_action').on('click', function() {
    var title = $('section.present').slice(-1).find('h2').text().slice(0,-7);
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