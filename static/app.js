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
    // Attach click event to the ISS nav link
    $('.nav-link[href="/iss_location"]').on('click', function(event) {
        console.log("ISS link clicked, loading message should appear.");  // Log to check if the event triggers

        event.preventDefault();  // Prevent immediate navigation

        // Show the loading message
        $('#loading-message').show();

        // Fetch ISS data
        $.get('/iss_location', function(data) {
            console.log('ISS data loaded successfully');  // Log if data is fetched
            window.location.href = '/iss_location';
        }).fail(function() {
            console.log('Error loading ISS data');  // Log if data fails to load
            $('#loading-message').hide();
            alert('Error loading ISS data. Please try again later.');
        });
    });
});








