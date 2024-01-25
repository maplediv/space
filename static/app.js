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
</script>
