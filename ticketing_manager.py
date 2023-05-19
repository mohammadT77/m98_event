from menu.models import generate_menu_from_dict
from ticketing.manager_actions import *
from ticketing.models import ManagerUser

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


root_menu = generate_menu_from_dict(manager_menu_route)

def main():
    username = get_input("Username: ")
    password = get_input("Password: ")
    
    try:
        login = ManagerUser.login(username, password)
    except AssertionError:
        print("Manager user is not set")
        exit()

    if login:
        print("Welcome manager...\n")
        root_menu()
    else:
        print("invalid username or password")


main()