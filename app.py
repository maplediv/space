from flask import Flask, render_template, jsonify
import requests
from datetime import date, timedelta
from config import Config

app = Flask(__name__, static_url_path='/static')

# Configuration variables for API endpoints and keys
APOD_API_BASE_URL = "https://api.nasa.gov/planetary/apod"

NEO_API_BASE_URL = "https://api.nasa.gov/neo/rest/v1"



# Route for the homepage
@app.route("/")
def space():
    return render_template("space.html")

# Route for displaying ISS location
@app.route('/iss_location')
def iss_location():
    try:
        api_url = 'http://api.open-notify.org/iss-now.json'
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for any HTTP error

        iss_data = response.json()
        latitude = iss_data['iss_position']['latitude']
        longitude = iss_data['iss_position']['longitude']
        timestamp = iss_data['timestamp']
        return render_template('iss_location.html', latitude=latitude, longitude=longitude, timestamp=timestamp)
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch ISS location: {e}"

# Route for displaying the Astronomy Picture of the Day (APOD)
@app.route("/apod")
def apod():
    try:
        params = {"api_key": Config.APOD_API_KEY}
        response = requests.get(APOD_API_BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for any HTTP error

        data = response.json()
        title = data.get("title", "NASA Astronomy Picture of the Day")
        url = data.get("url", "")
        explanation = data.get("explanation", "")

        return render_template("apod.html", title=title, url=url, explanation=explanation)
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch APOD data: {e}"

# Route for displaying near-Earth objects (NEO)
@app.route("/neo")
def neo():
    try:
        current_date = date.today().strftime("%Y-%m-%d")
        end_date = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")
        params = {"start_date": current_date, "end_date": end_date, "api_key": Config.NEO_API_KEY}

        response = requests.get(NEO_API_BASE_URL + "/feed", params=params)
        response.raise_for_status()  # Raise an exception for any HTTP error

        data = response.json()
        neo_objects = data.get("near_earth_objects", {}).get(current_date, [])

        neo_info = [{"name": neo.get("name", "Unknown"), "approach_date": neo.get("close_approach_date", "Unknown")}
                    for neo in neo_objects]

        return render_template("neo.html", neo_info=neo_info)
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch NEO data: {e}"




if __name__ == '__main__':
    app.run(debug=True)
