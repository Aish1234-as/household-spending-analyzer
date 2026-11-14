from datetime import datetime, timezone, timedelta

ist = timezone(timedelta(hours=5, minutes=30))
utc_time = datetime(2026, 1, 15, 18, 45, tzinfo=timezone.utc)
ist_time = utc_time.astimezone(ist)

print("UTC:", utc_time.isoformat())
print("IST:", ist_time.isoformat())
print("Date in UTC:", utc_time.date())
print("Date in IST:", ist_time.date())
print("Dates differ:", utc_time.date() != ist_time.date())