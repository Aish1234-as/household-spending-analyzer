import random
from categorize import categorize
from ids import make_user_id, make_account_id

random.seed(20261022)
merchants = ["Grocery store", "Netflix", "Swiggy", "Electricity bill", "Uber", "Amazon", "Rent payment", "Salary credit"]

rows = 0
correct = 0
for n in range(1, 10001):
    account_id = make_account_id(make_user_id(n))
    for _ in range(4):
        description = random.choice(merchants)
        predicted = categorize(description)
        rows += 1
        if predicted != "Uncategorized":
            correct += 1

print("Rows categorized:", rows)
print("Matched a rule:", correct, "of", rows)