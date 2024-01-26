<script>
    function displayLocation() {
        var latitude = parseFloat("{{ latitude }}");
        var longitude = parseFloat("{{ longitude }}");

        console.log("Latitude:", latitude);
        console.log("Longitude:", longitude);

        var geocodingApiUrl = `https://nominatim.openstreetmap.org/reverse?lat=${latitude}&lon=${longitude}&format=json`;

        $.ajax({
            url: geocodingApiUrl,
            method: "GET",
            success: function (data) {
                console.log("Geocoding API response:", data);
                var location = data.display_name;
                $("#location").text(location);
            },
            error: function (error) {
                console.error("Geocoding API error:", error);
                $("#location").text("Location not available");
            }
        });
    }

    $(document).ready(function () {
        displayLocation();
    });

// Add a script to toggle the button text
        document.getElementById('readMoreButton').addEventListener('click', function () {
            var buttonText = this.innerHTML.trim();
            if (buttonText === 'Read More') {
                this.innerHTML = 'Read Less';
            } else {
                this.innerHTML = 'Read More';
            }
        });
</script>
