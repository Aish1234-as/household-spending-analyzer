def compare_budget(spent, budget):
    result = {}
    for category, limit in budget.items():
        spent_amount = spent.get(category, 0)
        result[category] = spent_amount > limit
    return result       
