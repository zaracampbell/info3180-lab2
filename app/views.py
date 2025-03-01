from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime


###
# Routing for your application.
###

def format_date_joined(date):
    return date.strftime("%B, %Y")  
    
@app.route('/profile')
def profile():
    profile_info = {
        "full_name": "Zara Campbell",
        "username": "zara_christina",
        "location": "Kingston, Jamaica",
        "date_joined": format_date_joined(datetime.date(2025, 2, 1)),  # Example date
        "bio": "I am a young and passionate computing student with a love for helping others and making a difference. I am currently doing WEB DEVELOPMENT II-INFO3180 where I am expanding my knowledge on Python and learning Flask.",
        "posts": 10,
        "followers": 1032,
        "following": 700,
        "profile_image": "profile.jpeg"  # Ensure this image is in the 'static' folder
    }

    return render_template("profile.html", profile=profile_info)


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Zara Campbell")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
