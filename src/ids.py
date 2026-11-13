def make_user_id(number):
    return f"USR-{number:06d}"


def make_account_id(user_id):
    return f"ACC-{user_id}-01"