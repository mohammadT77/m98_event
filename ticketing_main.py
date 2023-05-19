from ticketing.main_actions import *
from menu.models import generate_menu_from_dict
main_menu_route = {
    'name':'Maktab events',
    'children':[
        {
            'name': 'See all events',
            'action': see_all_events_action,
        },
        {
            'name': 'See my tickets',
            'action': see_my_tickets_action
        }
    ]
}

root_menu = generate_menu_from_dict(main_menu_route)

def main():
    root_menu()

main()