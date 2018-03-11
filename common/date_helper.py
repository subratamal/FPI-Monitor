from datetime import datetime, timedelta
from calendar import monthrange


class DateHelper:
    def __init__(self):
        pass

    @staticmethod
    def diff_month(d1, d2):
        return (d1.year - d2.year) * 12 + d1.month - d2.month + 1

    @staticmethod
    def subtract_days_from_date(number_of_days):
        return datetime.today() - timedelta(days=number_of_days)
