$(function() {
    $('.boardbutton').click(function() {
        console.log($(this))
        $.ajax({
            url: '/',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({"mp3": $(this)[0].value}),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('.stopbutton').click(function() {
        $.ajax({
            url: '/',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({"stop": true}),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        })
    });
});