$(document).ready(function() {
    $('#second_page').hide();
    $('#second_text').hide();

    $('#first_btn').click(function() {
        // $('#first_btn').addClass('.hidden')
        // alert('this is the button');
        $('#second_text').fadeIn();
        $('#second_page').fadeIn();
        $('#first_text').fadeOut();
        $('#first_page').fadeOut();

    });
});