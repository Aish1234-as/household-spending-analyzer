import random
import time
from categorize import categorize

random.seed(20261022)

phrases = [
    ("UPI-SWIGGY 4521", "Food"),
    ("SWGY ORDER 77", "Food"),
    ("NETFLIX.COM", "Entertainment"),
    ("REFUND SWGY 120", "Refund"),
    ("RFND AMAZON 40", "Refund"),
    ("NEFT TRANSFER SAVINGS", "Transfer"),
    ("TRF TO SAVINGS", "Transfer"),
    ("GROCERY MART", "Food"),
    ("ELECTRICITY BILL", "Utilities"),
    ("UBER TRIP", "Transport"),
    ("AMAZON ORDER", "Shopping"),
    ("RENT PAYMENT", "Housing"),
    ("SALARY CREDIT", "Income"),
]

start = time.time()
total = 0
correct = 0
for n in range(1, 500001):
    for _ in range(24):
        description, expected = random.choice(phrases)
        total += 1
        if categorize(description) == expected:
            correct += 1

print("Rows checked:", total)
print("Accuracy:", correct / total)
print("Seconds:", round(time.time() - start, 2))