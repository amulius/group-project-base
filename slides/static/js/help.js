$(document).ready(function () {
        GetDone();
        setInterval(GetDone, 5000);
});


function GetDone(){
        var path = window.location.pathname + window.location.hash;
        var slide = '/' + path.split('/').slice(2).join('/');
        var data = {
            'want': 'help',
            'slide': slide
        };
        $.ajax({
            url: "/details/",
            type: "POST",
            data: JSON.stringify(data),
            success: function (data) {
                $('#help_stuff').html(data);
            },
            error: function (data) {
                console.log('done bad');
                console.log(data);
            }
        });
    }