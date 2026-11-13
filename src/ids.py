def make_user_id(number):
    return f"USR-{number:06d}"

print(make_user_id(1))
print(make_user_id(250))

def make_account_id(user_id):
    return f"ACC-{user_id}-01"