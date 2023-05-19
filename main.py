from menu.models import ListMenu, PageMenu, generate_menu_from_dict, MenuNode

def buy_ticket_action():
    national_id = input("Enter your National ID: ")
    event_id = input("Enter the Event id: ")
    num = input("Quantity: ")

    # TODO: find the event from database
    # TODO: calculate the price
    # ...

    print("Final ticket:", f"\ncost: 1000\nnational id: {national_id}\nevent:{event_id}\nquantity:{num}")
    print("Enjoy the event.")
    ...



# root_menu = ListMenu("Maktab Events")
# events_menu = ListMenu("Events", description="See all events", parent=root_menu)
# tickets_menu = ListMenu("Tickets", description="See all Tickets", parent=root_menu)
# buy_ticket_menu = PageMenu(buy_ticket_action, "Buy a ticket",parent=tickets_menu)

# # root_menu.print_tree()
# root_menu()



main_menu_dict = {
    'name':'Maktab events',
    'children':[
        {
            'name':'Login as manager',
            'action': lambda: None,
        },
        {
            'name': 'Events',
            'children': [
                {
                    'name':'See al events',
                    'action': lambda: None,       
                },
                {
                    'name':'See an event\'s details',
                    'action': lambda: None,
                },
                {
                    'name': 'Add new event',
                    'action': lambda: None,
                }
            ]
        },
        {
            'name': 'Tickets',
            'description':"See all Tickets",
            'children':[
                {
                    'name':'Buy ticket',
                    'action':buy_ticket_action
                },
            ]
        }
    ]
}

root_menu = generate_menu_from_dict(main_menu_dict, parent=None)
root_menu()
# root_menu.print_tree()

def main():
    # menu: login as manager -> 

    pass
