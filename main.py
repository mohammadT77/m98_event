from menu.models import ListMenu, PageMenu

def buy_ticket_action():
    national_id = input("Enter your National ID: ")
    event_id = input("Enter the Event id: ")
    num = input("Quantity: ")

    # TODO: find the event from database
    # TODO: calculate the price
    # ...

    print("Final ticket:", f"\ncost: 1000\nnational id: {national_id}\nevent:{event_id}\nquantity:{num}")
    print("Enjoy the event.")



root_menu = ListMenu("Maktab Events")
events_menu = ListMenu("Events", description="See all events", parent=root_menu)
tickets_menu = ListMenu("Tickets", description="See all Tickets", parent=root_menu)
buy_ticket_menu = PageMenu(buy_ticket_action, "Buy a ticket",parent=tickets_menu)

# root_menu.print_tree()
root_menu()