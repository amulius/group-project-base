$(document).ready(function () {
        GetDones();
        setInterval(GetDones, 5000);
});


// Could you have done.js, help.js, and question.js share some of the AJAX and html creation code?
// Seem like there could be some reuse
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
