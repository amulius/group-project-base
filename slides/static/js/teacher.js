$(document).ready(function () {

    var path = window.location.pathname.split('/').slice(2).join('/');
    var slideStuff = window.location.pathname.split('/').slice(2, 4);
    var url = '/' + path;
    var week = slideStuff[0].slice(4);
    var lectureNum = slideStuff[1];

    $.ajax({
        url: url,
        type: 'GET',
        success: function (response) {
            var slides = [];
            var i = 0;
            $(response).find('.slides>section').each(function() {
                var subSections = $(this).find('section>h2:first-child');
                var j = 0;
                if(subSections.length > 1){
                    subSections.each(
                        function(){
                            slides.push({
                                'slide_title':$(this).text().trim(),
                                'slide_number':i,
                                'slide_sub_number':j,
                                'slide_data': slide_data(week, lectureNum, i, j)
                            });
                            j += 1;
                        }
                    );
                }
                else{
                    if (i){
                        slides.push({
                            'slide_title':$(this).find('h2:first-child').text().trim(),
                            'slide_number':i,
                            'slide_sub_number':j,
                            'slide_data': slide_data(week, lectureNum, i, j)
                        });
                    }
                }
                i += 1;
            });
            var data = {
                'want_lecture': 'yes',
                'week': week,
                'lecture': lectureNum,
                'title': $(response).find('h1').first().text().trim(),
                'slides': slides
            };
            lecture(data);
        },
        error: function (response) {
            console.log(response);
        }
    });

    var slide_data = function(w,l,n,sN) {
        var path = '/week'+w+'/'+l+'/#/'+n;
        if(sN){
            path += '/'+sN;
        }
        return path;
    };

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
