from ids import make_user_id, make_account_id

accounts = []
for n in range(1, 51):
    user_id = make_user_id(n)
    accounts.append((user_id, make_account_id(user_id)))

print(accounts)