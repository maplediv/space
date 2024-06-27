from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import date, timedelta
import bcrypt
from config import Config

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))  # Change column name to 'password'

    def __repr__(self):
        return '<User {}>'.format(self.username)


@app.route("/")
def space():
    return render_template("space.html")

@app.route('/iss_location')
def iss_location():
    try:
        api_url = 'http://api.open-notify.org/iss-now.json'
        response = requests.get(api_url)
        response.raise_for_status()
        iss_data = response.json()
        latitude = iss_data['iss_position']['latitude']
        longitude = iss_data['iss_position']['longitude']
        timestamp = iss_data['timestamp']
        return render_template('iss_location.html', latitude=latitude, longitude=longitude, timestamp=timestamp)
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch ISS location: {e}"

@app.route("/apod")
def apod():
    try:
        params = {"api_key": Config.APOD_API_KEY}
        response = requests.get(Config.APOD_API_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        title = data.get("title", "NASA Astronomy Picture of the Day")
        url = data.get("url", "")
        explanation = data.get("explanation", "")
        return render_template("apod.html", title=title, url=url, explanation=explanation)
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch APOD data: {e}"

@app.route("/neo")
def neo():
    try:
        current_date = date.today().strftime("%Y-%m-%d")
        end_date = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")
        params = {"start_date": current_date, "end_date": end_date, "api_key": Config.NEO_API_KEY}
        response = requests.get(Config.NEO_API_BASE_URL + "/feed", params=params)
        response.raise_for_status()
        data = response.json()
        neo_objects = data.get("near_earth_objects", {}).get(current_date, [])
        neo_info = [{"name": neo.get("name", "Unknown"), "approach_date": neo.get("close_approach_date", "Unknown")}
                    for neo in neo_objects]
        return render_template("neo.html", neo_info=neo_info)
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch NEO data: {e}"

@app.route("/newuser", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if the user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({"message": "Username already exists"}), 400

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create a new user object
        new_user = User(username=username, email=email, password=hashed_password)

        # Add the user object to the session and commit the transaction
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully"}), 201

    return render_template("newuser.html")

if __name__ == '__main__':
    app.run(debug=True)
