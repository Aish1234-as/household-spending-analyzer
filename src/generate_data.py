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

merchants = ["Grocery store", "Netflix", "Swiggy", "Electricity bill"]
transactions = []
for user_id, account_id in accounts:
    description = random.choice(merchants)
    amount = -random.randint(5, 500)
    transactions.append((account_id, "2026-01-15", description, amount))

transactions.append(("ACC-USR-000001-01", "2026-01-16", "Refund: Swiggy", 120))
transactions.append(("ACC-USR-000002-01", "2026-01-16", "Transfer to savings", -500))

with open("data/transactions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["account_id", "date", "description", "amount"])
    writer.writerows(transactions)

category_for = {"Grocery store": "Food", "Swiggy": "Food", "Netflix": "Entertainment", "Electricity bill": "Utilities"}
ground_truth = [(account_id, category_for[desc]) for (user_id, account_id), (_, _, desc, _) in zip(accounts, transactions)]
ground_truth.append(("ACC-USR-000001-01", "Refund"))
ground_truth.append(("ACC-USR-000002-01", "Transfer"))

with open("data/ground_truth.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["account_id", "expected_category"])
    writer.writerows(ground_truth)