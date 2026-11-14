import random
from categorize import categorize
from ids import make_user_id, make_account_id

random.seed(20261022)
merchant_label = {
    "Grocery store": "Food",
    "Netflix": "Entertainment",
    "Swiggy": "Food",
    "Electricity bill": "Utilities",
    "Uber": "Transport",
    "Amazon": "Shopping",
    "Rent payment": "Housing",
    "Salary credit": "Income",
}
merchants = list(merchant_label.keys())

total = 0
correct = 0
for n in range(1, 500001):
    for _ in range(24):
        description = random.choice(merchants)
        expected = merchant_label[description]
        predicted = categorize(description)
        total += 1
        if predicted == expected:
            correct += 1

print("Labeled rows:", total)
print("Accuracy:", correct / total)