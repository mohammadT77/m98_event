def get_input(prompt, retry=True, target_type=str):
    """
    Get and Return user inputs after validating them
    """
    assert callable(target_type)

    user_input = input(prompt)
    try:
        user_input = target_type(user_input)
    except Exception as err:
        if retry:
            print("Invalid input, try again")
            return get_input(prompt, retry, target_type)
        else:
            raise TypeError("Invalid input, try again") from err  # NewException -> err
    return user_input


"""
Example dictionary:

main_menu_dict = {
    'name':'Maktab events',
    'children':[
        {
            'name':'Events',
            'description':"See all events",
            'children':[
                
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

"""
def generate_menu_from_dict(dict, parent=None):
    """
    Returns root (MenuNode) object creating children menu nodes
    """
    pass