KEYWORDS = {
    "swiggy": "Food",
    "grocery": "Food",
    "netflix": "Entertainment",
    "electricity": "Utilities",
    "uber": "Transport",
    "amazon": "Shopping",
}

def categorize(description):
    text = description.lower()
    if "refund" in text:
        return "Refund"
    if "transfer" in text:
        return "Transfer"
    for keyword, category in KEYWORDS.items():
        if keyword in text:
            return category
    return "Uncategorized"

print(categorize("SWIGGY ORDER 4521"))
print(categorize("NETFLIX.COM"))
print(categorize("RANDOM SHOP"))