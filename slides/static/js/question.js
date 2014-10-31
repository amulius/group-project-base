$(document).ready(function () {
        GetQuestions();
        setInterval(GetQuestions, 5000);
});


function GetQuestions(){
        var path = window.location.pathname + window.location.hash;
        var slide = '/' + path.split('/').slice(2).join('/');
        var data = {
            'want': 'question',
            'slide': slide
        };
        $.ajax({
            url: "/details/",
            type: "POST",
            data: JSON.stringify(data),
            success: function (data) {
                $('#question_stuff').html(data);
            },
            error: function (data) {
                console.log('question bad');
                console.log(data);
            }
        });
    }