from ids import make_user_id, make_account_id

accounts = []
for n in range(1, 51):
    user_id = make_user_id(n)
    accounts.append((user_id, make_account_id(user_id)))

import csv
import os

os.makedirs("data", exist_ok=True)
with open("data/accounts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["user_id", "account_id"])
    writer.writerows(accounts)