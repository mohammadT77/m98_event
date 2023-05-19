from menu.utils import get_input
from .models import Event
from datetime import datetime

def see_all_events_action(): # Done
    all_events = Event.get_all()  # list or generator

    for i, event in enumerate(all_events):
        print(i+1, event)  # __str__


def event_detail_action(): # Done
    event_id = get_input("Enter the event id: ", target_type=int)
    try:
        event = Event.find_by_id(event_id)
    except:
        print("Event not found.")
        return
    
    print("Event's detail:")
    print("  Title:", event.title)
    print("  Capacity:", event.capacity)
    print("  Availability:", event.availability)
    print("  Date:", event.event_date)
    print()


def add_new_event_action(): # DONE
    print("Enter event's detail below:")
    id = get_input("Id: ", target_type=int)
    title = get_input("Title: ", target_type=str)
    capacity = get_input("Capacity: ", target_type=int)
    date_ = get_input("Date: ", target_type=datetime.fromisoformat)

    event = Event(
        id=id,
        title=title,
        capacity=capacity,
        event_date=date_
    )

    event.save_file()
    print("Event's created.\n")

    

def delete_event_action():
    event_id = get_input("Enter the event id: ", target_type=int)
    try:
        event = Event.find_by_id(event_id)
    except:
        print("Event not found.")
        return

    event.delete()
    print("Event is deleted\n")