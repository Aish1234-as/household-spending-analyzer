import csv
from datetime import date

def month_dates(day, months=12):
    return [date(2026, m, day) for m in range(1, months + 1)]
print(month_dates(1))
def make_history(account_id):
    rows = []
    for d in month_dates(1):
        rows.append((account_id, d.isoformat(), "Rent", -15000))
    for d in month_dates(25):
        rows.append((account_id, d.isoformat(), "Salary", 60000))
    return rows

print(make_history("ACC-USR-000001-01")[:4])
from recurring import is_monthly_series
rent_dates = [date.fromisoformat(r[1]) for r in make_history("ACC-USR-000001-01") if r[2] == "Rent"]
print(is_monthly_series(rent_dates))
irregular = [date(2026, 1, 3), date(2026, 1, 20), date(2026, 3, 9)]
print(is_monthly_series(irregular))
from ids import make_user_id, make_account_id

monthly_count = 0
for n in range(1, 501):
    account_id = make_account_id(make_user_id(n))
    rent_dates = [date.fromisoformat(r[1]) for r in make_history(account_id) if r[2] == "Rent"]
    if is_monthly_series(rent_dates):
        monthly_count += 1
print("Monthly rent detected in", monthly_count, "of 500 accounts")
import time
start = time.time()
count = 0
for n in range(1, 2001):
    account_id = make_account_id(make_user_id(n))
    count += len(make_history(account_id))
print("Rows generated:", count, "in", round(time.time() - start, 2), "seconds")