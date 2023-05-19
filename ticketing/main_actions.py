from .models import Ticket, Event
from menu.utils import get_input

def see_all_events_action():
    pass  # TODO

def see_my_tickets_action():
    customer_id = get_input("Enter customer id: ")
    my_tickets = filter(lambda ticket: ticket.customer_id == customer_id, Ticket.get_all())

    for i, ticket in enumerate(my_tickets):
        print(i+1, ticket)