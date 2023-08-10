import datetime

def days_to_date(target_date):
    today = datetime.date.today()
    difference = (target_date - today).days
    return difference
