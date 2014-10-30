$('.helped').on('click', function () {
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
                $('.helped').filter('[data-pk="'+data['updated']+'"]').removeClass('btn-danger helped').addClass('btn-default').text('Helped!');
            },
            error: function (data) {
                console.log('helped bad');
                console.log(data);
            }
        });
    });