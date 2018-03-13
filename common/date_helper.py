from datetime import datetime, timedelta
from calendar import monthrange


class DateHelper:
    def __init__(self):
        pass

    @staticmethod
    def diff_month(d1, d2):
        """
        returns the difference is number of months e.g., for both dates in Month of March, 2018 , 0 would be rturned.
        If start date is in March, 2018 and end date is in January, 2017, 3 would be returned.
        
        :param d1: start_date 
        :param d2: end_date
        :return: difference in number of months
        """
        return (d1.year - d2.year) * 12 + d1.month - d2.month

    @staticmethod
    def add_sub_days(date=datetime.today(), number_of_days=0):
        return date + timedelta(days=number_of_days)

    @staticmethod
    def date_range_calc(end_date=datetime.today(), number_of_days=0):
        """
        returns start and end date of months in-between the time duration.
        e.g., 
        >> date_range_calc(end_date=datetime(2018, 03, 13), number_of_days=30)
        [
            "11-Feb-2018",
            "28-Feb-2018",
            "13-Mar-2018"
        ]
        
        >> date_range_calc(end_date=datetime(2018, 02, 27), number_of_days=190)
        [
            '21-Aug-2017', 
            '31-Aug-2017', 
            '30-Sep-2017', 
            '31-Oct-2017', 
            '30-Nov-2017', 
            '31-Dec-2017', 
            '31-Jan-2018', 
            '27-Feb-2018'
        ]
        
        :param end_date: datetime
        :param number_of_days: number of days  
        :return: list of dates   
        """
        date_ranges = []
        start_date = DateHelper.add_sub_days(end_date, - number_of_days)
        number_of_months = DateHelper.diff_month(end_date, start_date)
        cursor_date = start_date

        for month_number in range(number_of_months + 1):
            if month_number == 0:
                date_ranges.append(cursor_date.strftime("%d-%b-%Y"))
            elif month_number == number_of_months:
                cursor_date = end_date
                date_ranges.append(cursor_date.strftime("%d-%b-%Y"))
                break
            else:
                cursor_date = DateHelper.add_sub_days(cursor_date, 1)

            month_end_day = monthrange(cursor_date.year, cursor_date.month)[1]
            month_end_date = datetime(cursor_date.year, cursor_date.month, month_end_day)
            date_ranges.append(month_end_date.strftime("%d-%b-%Y"))
            cursor_date = month_end_date

        print(date_ranges)

# DateHelper.date_range_calc(end_date=datetime(2018, 2, 27), number_of_days=190)
