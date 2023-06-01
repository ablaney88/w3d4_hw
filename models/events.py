from models.event import *
import datetime

event1 = Event(datetime.date(2021, 8, 17), "Comicon", "Main Hall", "BO")
event2 = Event(datetime.date(2022, 4, 5), "Hot Dog Eating Contest", "Mess Hall", "Eat as many dogs as possible")
event3 = Event(datetime.date(2023, 2, 28), "Pop and Lockathon", "Dance Hall", "Pop and lock till you drop")

events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)