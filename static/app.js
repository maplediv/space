document.addEventListener("DOMContentLoaded", function() {
    const explanationElement = document.querySelector(".apodresponsive-text");
    if (explanationElement) {
        // Get the raw text
        let text = explanationElement.textContent;

        // Variable to track punctuation count
        let punctuationCount = 0;

        // Replace punctuation with a line break every other time
        text = text.replace(/([.?!])/g, function(match) {
            punctuationCount++;
            // Insert line break after every 2nd punctuation mark
            if (punctuationCount % 2 === 0) {
                return match + "<br><br>"; // Add line break after every second punctuation
            }
            return match; // Otherwise, just return the punctuation mark
        });

        // Update the inner HTML with the line breaks
        explanationElement.innerHTML = text;
    }
});







$(document).ready(function() {
    $('#load-iss-btn').on('click', function() {
        // Show the loading message
        $('#loading-message').show();

        // Make the GET request to the /iss_data route
        $.get('/iss_data', function(data) {
            console.log(data); // Log the ISS data to the console (optional)

            // Redirect to the ISS page after the data is loaded
            window.location.href = '/iss_location';
        }).fail(function() {
            // If the request fails, hide the loading message and alert the user
            $('#loading-message').hide();
            alert('Error loading ISS data. Please try again later.');
        });
    });
});


