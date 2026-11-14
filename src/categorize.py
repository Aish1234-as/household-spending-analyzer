KEYWORDS = {
    "swiggy": "Food",
    "netflix": "Entertainment",
    "grocery": "Food",
    "electricity": "Utilities",
}

def categorize(description):
    text = description.lower()
    for keyword, category in KEYWORDS.items():
        if keyword in text:
            return category
    return "Uncategorized"
print(categorize("SWIGGY ORDER 4521"))
print(categorize("NETFLIX.COM"))
print(categorize("RANDOM SHOP"))