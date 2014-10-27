$(document).ready(function () {

        var path = window.location.pathname.split('/').slice(2).join('/');
        console.log(window.location.pathname.split('/'));

        var url = '/' + path;
        $.ajax({
            url: url,
            type: 'GET',
            success: function (response) {
                console.log(typeof $(response).find('h2'));
                $('.main').html($(response).find('h1'));
                $('.main').append($(response).find('h2'));

            },
            error: function (response) {
                console.log(response);
            }
        });
//    });


});
