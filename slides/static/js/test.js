$(document).ready(function () {

        $.ajax({
            url: '/',
            type: 'GET',
            success: function (response) {
                $('#testStuff').html(response);
                var a = $('.accordion').find('a');
                var teacher = '/teacher';
                a.each(function() {
                    var path = $( this).context.pathname;
                    $( this ).attr('href', teacher + path);
                });
            },
            error: function (response) {
                console.log(response);
            }
        });

});
