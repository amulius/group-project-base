$(document).ready(function () {

//    $('#testButton').on('click', function () {
//        $('#testStuff').load("/ .accordion");
        $.ajax({
            url: '/',
            type: 'GET',
            success: function (response) {
//                console.log(response);
                $('#testStuff').html(response);
                var a = $('.accordion').find('a');
                var teacher = '/teacher';
                a.each(function() {
//                    console.log( $( this));
                    var path = $( this).context.pathname;
//                    console.log( $( this).context.host);
                    $( this ).attr('href', teacher + path);
//                    console.log( $( this ).attr('href') );
                });


            },
            error: function (response) {
                console.log(response);
            }
        });
//    });


});
