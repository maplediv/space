import os
from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime, timedelta, date
import bcrypt
from flask_migrate import Migrate
from dotenv import load_dotenv
from config import Config

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Database credentials and URI setup
db_user = os.getenv('DB_USER', 'your_local_db_user')
db_password = os.getenv('DB_PASSWORD', 'your_local_db_password')
db_host = os.getenv('DB_HOST', 'localhost')  # Set the correct hostname here if different
db_name = os.getenv('DB_NAME', 'your_local_db_name')

# SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}?sslmode=require"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)
migrate = Migrate(app, db)



# User Model
class User(db.Model):
    __tablename__ = 'users'  # Ensure this matches your table name

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

# Registration route
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the username or email already exists
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
            if existing_user.email == email:
                flash('Email address already exists. Please use a different email.', 'danger')
            else:
                flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('sign_up'))

        # Hash the password before storing
        hashed_password = generate_password_hash(password)

        # Create the new user
        new_user = User(username=username, email=email, password_hash=hashed_password)

        try:
            # Add the new user to the session and commit to the database
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()  # In case another error slips through
            flash(f'An unexpected error occurred: {e}', 'danger')

    # Render the sign-up template on GET requests
    return render_template('sign_up.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        
        if user is None:
            flash('This account has been deleted. Please create a new account.', 'danger')
            return redirect(url_for('login'))

        # Check if the password matches
        if check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['username'] = user.username  # Store username in session
            return redirect(url_for('space'))  # Redirect to the desired page after login
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.clear()  # Clear the entire session
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/delete_user', methods=['POST'])
def delete_user():
    if 'user_id' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    if user:
        db.session.delete(user)
        db.session.commit()
        flash('User account deleted successfully.', 'info')
        session.clear()

    return redirect(url_for('login'))

# Update user details
@app.route("/update_user", methods=["GET", "POST"])
def update_user():
    if "user_id" not in session:
        flash("Please log in first", "warning")
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    if request.method == "POST":
        email = request.form.get("email")
        new_password = request.form.get("password")

        # Update user details
        if email:
            user.email = email
        if new_password:
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            user.password_hash = hashed_password  # Update password_hash, not password

        db.session.commit()
        flash("User details updated successfully", "success")
        return redirect(url_for("space"))

    return render_template("update_user.html", user=user)

# Homepage route
@app.route("/")
def space():
    username = session.get('username')
    return render_template("space.html", username=username)


@app.route('/iss_location')
def iss_location():
    try:
        # Retrieve username from session
        username = session.get('username')
        
        api_url = 'http://api.open-notify.org/iss-now.json'
        response = requests.get(api_url)
        response.raise_for_status()
        
        # Extract data from the response
        iss_data = response.json()
        latitude = iss_data['iss_position']['latitude']
        longitude = iss_data['iss_position']['longitude']
        timestamp = iss_data['timestamp']
        
        # Pass data to the template, including username
        return render_template("iss_location.html", username=username, latitude=latitude, longitude=longitude, timestamp=timestamp)
    
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
        
        # Retrieve username from session
        username = session.get('username')

        # Pass username to the template
        return render_template("apod.html", title=title, url=url, explanation=explanation, username=username)
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch APOD data: {e}"


@app.route("/neo")
def neo():
    try:
        # Retrieve username from session
        username = session.get('username')
        
        current_date = date.today().strftime("%Y-%m-%d")
        end_date = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")
        params = {"start_date": current_date, "end_date": end_date, "api_key": Config.NEO_API_KEY}
        
        response = requests.get(Config.NEO_API_BASE_URL + "/feed", params=params)
        response.raise_for_status()
        
        data = response.json()
        neo_objects = data.get("near_earth_objects", {}).get(current_date, [])
        
        neo_info = [
            {"name": neo.get("name", "Unknown"), "approach_date": neo.get("close_approach_date", "Unknown")}
            for neo in neo_objects
        ]
        
        # Pass username and neo_info to the template
        return render_template("neo.html", neo_info=neo_info, username=username)
    
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch NEO data: {e}"
    
    except KeyError as e:
        # Handle unexpected data structure
        return f"Error: Missing expected data: {e}"


if __name__ == '__main__':
    app.run(debug=True)
