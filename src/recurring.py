import csv
from datetime import date

def day_gaps(dates):
    gaps = []
    for i in range(1, len(dates)):
        gap = (dates[i] - dates[i - 1]).days
        gaps.append(gap)
    return gaps

def is_monthly(gaps):
    return len(gaps) > 0 and all(28 <= g <= 31 for g in gaps)

def is_monthly_series(dates):
    gaps = day_gaps(dates)
    return is_monthly(gaps)

def load_transactions(path):
    by_account = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            by_account.setdefault(row["account_id"], []).append(row)
    return by_account

accounts = load_transactions("data/transactions.csv")
print(len(accounts))

for account_id, rows in accounts.items():
    dates = [date.fromisoformat(r["date"]) for r in rows]
    print(account_id, is_monthly_series(dates))