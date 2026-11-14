def accuracy(predicted, expected):
    return sum(p == e for p, e in zip(predicted, expected)) / len(expected)

print(accuracy(["Food", "Food", "Uncategorized"], ["Food", "Food", "Food"]))
print(accuracy(["Food", "Food"], ["Food", "Food"]))
import csv
from categorize import categorize

with open("data/transactions.csv") as f:
    rows = list(csv.DictReader(f))
with open("data/ground_truth.csv") as f:
    truth = {r["account_id"]: r["expected_category"] for r in csv.DictReader(f)}

predicted = [categorize(r["description"]) for r in rows]
expected = [truth[r["account_id"]] for r in rows]
print(accuracy(predicted, expected))