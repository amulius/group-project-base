$('.need_help').on('click', function () {
//        console.log($(this));
        var pk = $(this).data('pk');
//        console.log(pk);
        var data = {
            'want': 'helped',
            'pk': pk
        };
        $.ajax({
            url: "/update/",
            type: "POST",
            data: JSON.stringify(data),
            success: function (data) {
                console.log(data);
                $('.need_help').filter('[data-pk="'+data['updated']+'"]').removeClass('need_help').addClass('been_helped').text('Helped!');
            },
            error: function (data) {
                console.log('helped bad');
                console.log(data);
            }
        });
    });