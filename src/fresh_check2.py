from categorize import categorize

fresh2 = [
    ("SWIGGY INSTAMART 44", "Food"),
    ("NETFLIX.COM SUBSCRIPTION", "Entertainment"),
    ("UBER RIDE 9", "Transport"),
    ("AMAZON PRIME 999", "Shopping"),
    ("GROCERY OUTLET 3", "Food"),
]

correct = 0
for description, expected in fresh2:
    predicted = categorize(description)
    print(description, "->", predicted, "| expected:", expected)
    if predicted == expected:
        correct += 1
print("Second fresh accuracy:", correct / len(fresh2))