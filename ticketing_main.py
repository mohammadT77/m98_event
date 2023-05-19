main_menu_route = {
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
        }
    ]
}