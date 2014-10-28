$(document).ready(function () {

    var path = window.location.pathname.split('/').slice(2).join('/');
    var slideStuff = window.location.pathname.split('/').slice(2, 4);
    var url = '/' + path;

    $.ajax({
        url: url,
        type: 'GET',
        success: function (response) {
            var slides = [];
            var i = 0;
            var j = 0;
            var k = 0;
            console.log($(response).find('.slides>section'));
            $(response).find('.slides>section').each(function() {
//                if (j != 0){
//                    k++;
//                    j--;
//                }
//                console.log(i, k, j);
                if($(this).find('h2').length > 1){
//                    j = $(this).find('h2').length;
//                    k = -1;
//                    console.log('block', i, k, j);
                }
                else if($( this).find('h2').length == 1){
                    slides.push({
                        'slide_title':$(this).find('h2').text().trim(),
                        'slide_number':i,
                        'slide_sub_number':k
                    });
//                    console.log('save', i, k, j);
                }

//                if (j == 0){
//                    i++;
//                    j = 0;
////                    k = 0;
//                }


            });
            var data = {
                'want_lecture': 'yes',
                'week': slideStuff[0].slice(4),
                'lecture': slideStuff[1],
                'title': $(response).find('h1').first().text().trim(),
                'slides': slides
            };
//             console.log($(response).find('h1').first());
            lecture(data);
        },
        error: function (response) {
            console.log(response);
        }
    });

    var lecture = function(data) {
        $.ajax({
            url: '/lecture_fragment/',
            type: 'POST',
            data: JSON.stringify(data),
            success: function (response) {
                $('.main').html(response);

            },
            error: function (response) {
                console.log(response);
            }
        });
    };
});
