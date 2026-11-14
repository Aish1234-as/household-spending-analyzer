from categorize import categorize

fresh3 = [
    ("FRESHMART ORDER 8", "Food"),
    ("CAB RIDE 17", "Transport"),
    ("ZEPTO GROCER 2", "Food"),
    ("YOUTUBE PREMIUM", "Entertainment"),
    ("BOOK TRIP STAY", "Transport"),
]

correct = 0
for description, expected in fresh3:
    predicted = categorize(description)
    print(description, "->", predicted, "| expected:", expected)
    if predicted == expected:
        correct += 1
print("Fallback fresh accuracy:", correct / len(fresh3))