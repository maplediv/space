// Toggle button text and collapse manually
$(document).ready(function(){
    $('#readMoreButton').on('click', function () {
        var $readMoreText = $('#readMoreText-0');
        if ($readMoreText.is(':visible')) {
            $readMoreText.hide();
            $(this).text('Read More');
        } else {
            $readMoreText.show();
            $(this).text('Read Less');
        }
    });
});

// Handle the collapse events to update button text
$('#readMoreText').on('show.bs.collapse', function () {
    $('#readMoreButton').text('Read Less');
});

$('#readMoreText').on('hide.bs.collapse', function () {
    $('#readMoreButton').text('Read More');
});
