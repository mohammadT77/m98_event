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