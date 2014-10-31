$(document).ready(function () {
        GetDones();
        setInterval(GetDones, 5000);
});


function GetDones(){
        var path = window.location.pathname + window.location.hash;
        var slide = '/' + path.split('/').slice(2).join('/');
        var data = {
            'want': 'done',
            'slide': slide
        };
        $.ajax({
            url: "/details/",
            type: "POST",
            data: JSON.stringify(data),
            success: function (data) {
                $('#done_stuff').html(data);
            },
            error: function (data) {
                console.log('done bad');
                console.log(data);
            }
        });
    };