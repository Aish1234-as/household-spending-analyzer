def check_unique(ids):
    return len(ids) == len(set(ids))

print(check_unique(["USR-000001", "USR-000002"]))
print(check_unique(["USR-000001", "USR-000001"]))

def check_links(users, accounts):
    for user_id, account_id in accounts:
        if user_id not in users:
            return False
    return True

users = ["USR-000001", "USR-000002"]
print(check_links(users, [("USR-000001", "ACC-USR-000001-01")]))
print(check_links(users, [("USR-000009", "ACC-USR-000009-01")]))