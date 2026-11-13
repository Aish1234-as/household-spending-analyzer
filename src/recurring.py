from datetime import date
def day_gaps(dates):
    gaps = []
    for i in range(1, len(dates)):
        gap = (dates[i] - dates[i - 1]).days
        gaps.append(gap)
    return gaps
print(day_gaps([date(2026, 1, 1), date(2026, 2, 1), date(2026, 3, 3)]))
def is_monthly(gaps):
    return all(28 <= g <= 31 for g in gaps)

def is_monthly_series(dates):
    gaps = day_gaps(dates)
    return is_monthly(gaps)

print(is_monthly_series([date(2026, 1, 1), date(2026, 2, 1), date(2026, 3, 3)]))
print(is_monthly_series([date(2026, 1, 1), date(2026, 1, 15), date(2026, 2, 1)]))