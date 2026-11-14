from categorize import categorize

fresh = [
    ("BLINKIT GROCERY 12", "Food"),
    ("UBER EATS 5", "Food"),
    ("NETFLIX PREMIUM", "Entertainment"),
    ("PAYTM WALLET TOPUP", "Utilities"),
    ("BIGBASKET 300", "Food"),
]

correct = 0
for description, expected in fresh:
    predicted = categorize(description)
    print(description, "->", predicted, "| expected:", expected)
    if predicted == expected:
        correct += 1
print("Fresh accuracy:", correct / len(fresh))