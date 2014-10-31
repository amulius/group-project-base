    $('.more_info').on('click', function () {
        var slide = $(this).data('slide');
        var id = $(this).data('id');
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
                $('#slide'+id).toggleClass( "loop" );
//                GetDone(slide);
                var loop = setInterval(loopInfo, 5000);
            },
            error: function (data) {
                console.log('bad');
                console.log(data);
            }
        });
    });

    function loopInfo(){
        $('.loop').each(GetInfo);
    }

    function GetInfo(){
        var slide = $(this).data('slide');
        var id = $(this).data('id');
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
    }

var GetDone = function(slide){
        var data = {
            'want': 'done',
            'slide': slide
        };
        $.ajax({
            url: "/details/",
            type: "POST",
            data: JSON.stringify(data),
            success: function (data) {
                console.log(data);
            },
            error: function (data) {
                console.log('done bad');
                console.log(data);
            }
        });
    };
