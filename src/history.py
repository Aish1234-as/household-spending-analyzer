import csv
from datetime import date
import time
from ids import make_user_id, make_account_id
from recurring import is_monthly_series

def month_dates(day, months=12):
    return [date(2026, m, day) for m in range(1, months + 1)]

def make_history(account_id):
    rows = []
    for d in month_dates(1):
        rows.append((account_id, d.isoformat(), "Rent", -15000))
    for d in month_dates(25):
        rows.append((account_id, d.isoformat(), "Salary", 60000))
    return rows

monthly_count = 0
for n in range(1, 501):
    account_id = make_account_id(make_user_id(n))
    rent_dates = [date.fromisoformat(r[1]) for r in make_history(account_id) if r[2] == "Rent"]
    if is_monthly_series(rent_dates):
        monthly_count += 1
print("Monthly rent detected in", monthly_count, "of 500 accounts")

start = time.time()
count = 0
for n in range(1, 500001):
    account_id = make_account_id(make_user_id(n))
    count += len(make_history(account_id))
print("Rows generated:", count, "in", round(time.time() - start, 2), "seconds")