

    // Toggle button text and collapse manually
    $('#readMoreButton').on('click', function () {
        var buttonText = $(this).text().trim();
        if (buttonText === 'Read More') {
            $('#readMoreText').collapse('show');
            $(this).text('Read Less');
        } else {
            $('#readMoreText').collapse('hide');
            $(this).text('Read More');
        }
    });

    // Handle the collapse events to update button text
    $('#readMoreText').on('show.bs.collapse', function () {
        $('#readMoreButton').text('Read Less');
    });

    $('#readMoreText').on('hide.bs.collapse', function () {
        $('#readMoreButton').text('Read More');
    });

   
