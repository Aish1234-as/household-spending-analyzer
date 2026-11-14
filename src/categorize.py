KEYWORDS = {
    "swiggy": "Food",
    "swgy": "Food",
    "zomato": "Food",
    "grocery": "Food",
    "dmart": "Food",
    "netflix": "Entertainment",
    "hotstar": "Entertainment",
    "electricity": "Utilities",
    "paytm": "Utilities",
    "uber": "Transport",
    "amazon": "Shopping",
    "rent payment": "Housing",
    "salary credit": "Income",
    "atm": "Cash",
}

REFUND_WORDS = ["refund", "rfnd", "reversal", "cashback"]
TRANSFER_WORDS = ["transfer", "trf", "neft", "imps"]

def categorize(description):
    text = description.lower()
    for word in REFUND_WORDS:
        if word in text:
            return "Refund"
    for word in TRANSFER_WORDS:
        if word in text:
            return "Transfer"
    for keyword, category in KEYWORDS.items():
        if keyword in text:
            return category
    return "Uncategorized"