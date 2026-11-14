from categorize import categorize

unseen = [
    ("POS PURCHASE ZOMATO 88", "Food"),
    ("PAYTM BILL PAYMENT", "Utilities"),
    ("HOTSTAR SUBSCRIPTION", "Entertainment"),
    ("ATM WITHDRAWAL", "Cash"),
    ("DMART SHOPPING", "Food"),
]

correct = 0
for description, expected in unseen:
    predicted = categorize(description)
    print(description, "->", predicted, "| expected:", expected)
    if predicted == expected:
        correct += 1
print("Unseen accuracy:", correct / len(unseen))
