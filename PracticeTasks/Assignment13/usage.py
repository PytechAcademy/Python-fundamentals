import datetime
from datetimeutils import count_days, get_month

target_date = datetime.date(2023, 8, 31)
days = count_days.days_to_date(target_date)
print(f"Days to target date: {days}")

date = datetime.date(2023, 8, 10)
month = get_month.month_as_string(date)
print(f"Month: {month}")
