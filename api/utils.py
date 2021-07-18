import numpy as np
from datetime import date, timedelta


def calculate_business_days(total_days):
    tomorrow = date.today() + timedelta(1)
    business_days = np.busday_count(tomorrow, tomorrow + timedelta(total_days))
    return business_days

def calculate_gain(total_days, gain_per_day):
    business_days = calculate_business_days(total_days)
    return business_days * gain_per_day

print(calculate_gain(30, 100))