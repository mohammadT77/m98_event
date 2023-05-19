# from menu.models import generate_menu_from_dict


# main_menu_dict = {
#     'name':'Maktab events',
#     'children':[
#         {
#             'name':'Login as manager',
#             'action': lambda: None,
#         },
#         {
#             'name': 'Events',
#             'children': [
#                 {
#                     'name':'See al events',
#                     'action': lambda: None,       
#                 },
#                 {
#                     'name':'See an event\'s details',
#                     'action': lambda: None,
#                 },
#                 {
#                     'name': 'Add new event',
#                     'action': lambda: None,
#                 }
#             ]
#         },
#         {
#             'name': 'Tickets',
#             'description':"See all Tickets",
#         }
#     ]
# }

# root_menu = generate_menu_from_dict(main_menu_dict, parent=None)
# root_menu.print_tree()

from ticketing.models import *
from datetime import datetime
# e1 = Event(1, "asd", 10, datetime.now())

# e1.save_file()

# with open('1.event', 'r') as f:
#     e1 = Event.from_file_content(f.read())

# print(e1)
# print(e1.title)
# print(e1.event_date)
# print(Event.get_all_path())
# print(*Event.get_all())
# e1 = Event(1,'a', 1, datetime.now())
# t1 = Ticket(1, e1, '1234')
# t1.save_file()
# print(t1)

# manager_user = ManagerUser('asqar', 'asqar', 'asqar!!!')
# print(manager_user)
# manager_user.save_file()

ManagerUser.login()