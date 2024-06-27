$(document).ready(function() {
    // Toggle button text and collapse manually
    $('#readMoreButton').on('click', function() {
        var $readMoreText = $('#readMoreText-0');
        if ($readMoreText.is(':visible')) {
            $readMoreText.hide();
            $(this).text('Read More');
        } else {
            $readMoreText.show();
            $(this).text('Read Less');
        }
    });

    // Handle the collapse events to update button text
    $('#readMoreText').on('show.bs.collapse', function() {
        $('#readMoreButton').text('Read Less');
    });

    $('#readMoreText').on('hide.bs.collapse', function() {
        $('#readMoreButton').text('Read More');
    });

    // Function to display the overlay
    function showOverlay() {
        var overlay = document.getElementById("overlay");
        overlay.style.display = "block";
        fetchAccountDetails(); // Fetch and display account details
    }

    // Function to fetch and display account details
    function fetchAccountDetails() {
        // Simulated account details (replace with actual data retrieval)
        var accountDetails = {
            username: "JohnDoe",
            email: "johndoe@example.com"
            // Add more account details as needed
        };

        var accountDetailsHTML = "<h2>Account Details</h2>";
        accountDetailsHTML += "<p><strong>Username:</strong> " + accountDetails.username + "</p>";
        accountDetailsHTML += "<p><strong>Email:</strong> " + accountDetails.email + "</p>";
        // Add more account details to the HTML string as needed

        var accountDetailsContainer = document.getElementById("accountDetails");
        accountDetailsContainer.innerHTML = accountDetailsHTML;
    }

    // Add event listener to the login icon to show the overlay
    $('#loginIcon').on('click', function(event) {
        event.preventDefault(); // Prevent default link behavior
        showOverlay(); // Show the overlay
    });

    // Function to hide the overlay
    function hideOverlay() {
        var overlay = document.getElementById("overlay");
        overlay.style.display = "none";
    }

    // Add event listener to the close button to hide the overlay
    $('#closeButton').on('click', function(event) {
        event.preventDefault(); // Prevent default link behavior
        hideOverlay(); // Hide the overlay
    });
});
