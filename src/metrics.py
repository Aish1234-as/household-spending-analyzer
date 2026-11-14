import csv
from categorize import categorize

def accuracy(predicted, expected):
    return sum(p == e for p, e in zip(predicted, expected)) / len(expected)

with open("data/transactions.csv") as f:
    rows = list(csv.DictReader(f))
with open("data/ground_truth.csv") as f:
    truth = [r["expected_category"] for r in csv.DictReader(f)]

predicted = [categorize(r["description"]) for r in rows]
print(accuracy(predicted, truth))

for p, e, r in zip(predicted, truth, rows):
    if p != e:
        print(r)