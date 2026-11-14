import csv
from collections import defaultdict

with open("data/transactions.csv") as f:
    rows = list(csv.DictReader(f))

totals = defaultdict(int)
for r in rows:
    totals[r["account_id"]] += int(r["amount"])

seen = set()
duplicates = 0
for r in rows:
    key = (r["account_id"], r["date"], r["description"], r["amount"])
    if key in seen:
        duplicates += 1
    seen.add(key)

print("Accounts with totals:", len(totals))
print("Total of all amounts:", sum(totals.values()))
print("Duplicate rows:", duplicates)