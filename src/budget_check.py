taxonomy = {"Food", "Entertainment", "Utilities", "Transport", "Shopping", "Housing", "Income"}

budgets = {"Food": 5000, "Entertainment": 800, "Groceries": 3000}

for category in budgets:
    if category not in taxonomy:
        print("Budget category not in taxonomy:", category)
    else:
        print("OK:", category)