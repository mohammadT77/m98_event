from menu.models import generate_menu_from_dict
from ticketing.manager_actions import *

manager_menu_route = {
    'name':'Maktab events manager panel',
    'children':[
        {
            'name': "Manage Events",
            'children': [
                {
                    'name': 'See all events',
                    'action': see_all_events_action,
                },
                {
                    'name': 'Event\'s detail',
                    'action': event_detail_action,
                },
                {
                    'name': 'Add new event',
                    'action': add_new_event_action,
                },
                {
                    'name': 'Delete an event',
                    'action': delete_event_action,
                },
            ]
        },
        {
            'name': 'Manager Tickets',
            'children': []
        }
    ]
}


def main():
    root_menu = generate_menu_from_dict(manager_menu_route)

    is_login = False # check login
    # TODO: Login view

    if is_login:
        root_menu()
