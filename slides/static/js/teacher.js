$(document).ready(function () {

    var path = window.location.pathname.split('/').slice(2).join('/');
    var slideStuff = window.location.pathname.split('/').slice(2, 4);
    console.log(slideStuff);

    var url = '/' + path;
    $.ajax({
        url: url,
        type: 'GET',
        success: function (response) {
//            $('.main').html($(response).find('h1').text());
//            $('.main').append($(response).find('h2').text());
            var data = {
                'slide_stuff': slideStuff,
                'title': $(response).find('h1').text(),
                'slides': $(response).find('h2')
            };
            $('.main').load("/lecture_fragment", data);

        },
        error: function (response) {
            console.log(response);
        }
    });
//    });


});
