$(function() {
    $('button').click(function() {
        $.ajax({
            url: '/',
            data: "TestData",
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});