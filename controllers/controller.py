from flask import render_template, request
from app import app
from models.events import events, add_new_event
from models.event import Event

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/events")
def show_events():
    return render_template("index.html", events=events)

@app.route("/events", methods=['POST'])
def add_events():
    date = request.form['Date']
    name_of_event = request.form['Event']
    room_location = request.form['Room Location']
    events_description = request.form['Description']
    new_event = Event(date, name_of_event, room_location, events_description)

    add_new_event(new_event)
    return render_template("index.html", events=events)
