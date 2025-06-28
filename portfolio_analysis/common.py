from datetime import datetime, date
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay


def get_latest_working_day() -> date :
    """
    Returns the latest working day, excluding weekends and US federal holidays.

    Returns:
        datetime: The most recent working day
    """
    us_bd = CustomBusinessDay(calendar=USFederalHolidayCalendar())
    today = datetime.now()
    if today.weekday() >= 5:
        latest_working_day = today - us_bd
    else:
        latest_working_day = today.replace(hour=0, minute=0, second=0, microsecond=0)
        if latest_working_day in USFederalHolidayCalendar().holidays():
            latest_working_day = latest_working_day - us_bd
    return latest_working_day.date()
