View the live app here: https://space-exp.onrender.com/


# NASA Space Explorer - Flask App


## Overview
NASA Space Explorer is a Flask web application that enables users to delve into space-related data using various NASA APIs.

By utilizing NASA’s public APIs, this application provides real-time data, creating an engaging and educational experience for space exploration enthusiasts.

## Features
- Image of the Day: Display NASA’s Astronomy Picture of the Day (APOD) with detailed information about the image and its context.
- Near-Earth Object (NEO) Data: Access and explore information about asteroids and comets that come close to Earth.
- International Space Station (ISS) Tracking: View real-time data and information about the ISS, including its current position and upcoming pass predictions.


## Technologies Used


### Backend:
- Flask: A lightweight web framework used to manage the app's routing, logic, and rendering of dynamic content.
- NASA APIs: The application integrates with various NASA APIs such as:
 - Astronomy Picture of the Day (APOD) API
 - Mars Rover Photos API
 - Near-Earth Object Web Service (NeoWs) API
 - NASA Solar System OpenData API

 ### Frontend:
- HTML5, CSS3: For structuring and styling the user interface.
- Jinja2: Flask's templating engine, used to dynamically render HTML content based on the data received from NASA's APIs.

 ### Database:
- PostgreSQL: A relational database is used to store user data, such as saved searches, favorite images, and exploration history.


### APIs & Libraries:
- Flask-WTF: For form handling, including search forms for celestial objects and other space data.
- Requests: Used for making API requests to NASA’s services.
- SQLAlchemy: Object-Relational Mapping (ORM) library used for database interaction and management.

 ### Authentication:
- Flask-Login: Used to manage user sessions, allowing users to create accounts, log in, and save favorite images or data.


## How It Works
1. User Interactions: Users can browse various sections of the app to explore different NASA-provided content (e.g., images, Mars rover data). They can search for celestial objects or view the Image of the Day.
2. API Requests: When users request information, the app makes real-time API calls to NASA's public APIs, fetches the data, and renders it on the page dynamically.
3. Rendering: Data is presented to users through Flask's Jinja2 templating, with a clean and user-friendly interface.


NASA Space Explorer is a dynamic, educational web application that leverages the power of NASA's public APIs to bring the wonders of space exploration to users.



