    $('.more_info').on('click', function () {
        var slide = $(this).data('slide');
        var id = $(this).attr('id');
        var data = {
            'want': 'basic',
            'slide': slide
        };
        $('#arrow'+id).toggleClass( "rotate" );
        $.ajax({
            url: "/details/",
            type: "POST",
            data: JSON.stringify(data),
            success: function (data) {
                $('#slide'+id).html(data);
            },
            error: function (data) {
                console.log('bad');
                console.log(data);
            }
        });
    });
