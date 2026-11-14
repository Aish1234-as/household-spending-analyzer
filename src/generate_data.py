import csv
import os
import random
from ids import make_user_id, make_account_id

random.seed(20261022)

accounts = []
for n in range(1, 51):
    user_id = make_user_id(n)
    accounts.append((user_id, make_account_id(user_id)))

os.makedirs("data", exist_ok=True)

with open("data/accounts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["user_id", "account_id"])
    writer.writerows(accounts)

transactions = []
for user_id, account_id in accounts:
    amount = -random.randint(5, 500)
    transactions.append((account_id, "2026-01-15", "Grocery store", amount))

with open("data/transactions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["account_id", "date", "description", "amount"])
    writer.writerows(transactions)

ground_truth = [(account_id, "Food") for user_id, account_id in accounts]

with open("data/ground_truth.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["account_id", "expected_category"])
    writer.writerows(ground_truth)