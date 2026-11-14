def accuracy(predicted, expected):
    return sum(p == e for p, e in zip(predicted, expected)) / len(expected)

print(accuracy(["Food", "Food", "Uncategorized"], ["Food", "Food", "Food"]))
print(accuracy(["Food", "Food"], ["Food", "Food"]))