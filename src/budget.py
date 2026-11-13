def compare_budget(spent, budget):
    result = {}
    for category, limit in budget.items():
        spent_amount = spent.get(category, 0)
        result[category] = spent_amount > limit
    return result       
print(compare_budget({"Food": 500, "Entertainment": 1200}, {"Food": 400, "Entertainment": 1000}))
print(compare_budget({"Food": 300}, {"Food": 400}))