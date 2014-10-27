$(document).ready(function () {

//    $('#testButton').on('click', function () {
        $('#testStuff').load("/ .accordion");
        $.ajax({
            url: '/',
            type: 'GET',
            success: function (response) {
//                console.log(response);
                $('#testStuff').html(response);
                var a = $('.accordion').find('a');
                var aTag;
                for (var i = 0; i < a.length; i++){
                    console.log(a[i].html);
                }

            },
            error: function (response) {
                console.log(response);
            }
        });
//    });


});
