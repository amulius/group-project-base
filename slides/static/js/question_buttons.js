$('.answer').on('click', function () {
//        console.log($(this));
        var pk = $(this).data('pk');
//        console.log(pk);
        var data = {
            'want': 'answered',
            'pk': pk
        };
        $.ajax({
            url: "/update/",
            type: "POST",
            data: JSON.stringify(data),
            success: function (data) {
                console.log(data);
                $('.answer').filter('[data-pk="'+data['updated']+'"]').removeClass('answer').addClass('answered').text('Answered!');
            },
            error: function (data) {
                console.log('helped bad');
                console.log(data);
            }
        });
    });