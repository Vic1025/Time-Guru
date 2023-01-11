from math import ceil, floor
from datetime import datetime, date, time

from Activity import FixedTimeActivity, VariableTimeActivity


def datetime_to_idx_dw(date_time: datetime):
    return date_time.hour * 12 + floor(date_time.minute / 5)


def datetime_to_idx_up(date_time: datetime):
    return date_time.hour * 12 + ceil(date_time.minute / 5)


def idx_to_time(idx: int):
    return time(hour=idx // 12, minute=(idx % 12) * 5)


def idx_in_activity_timeblock(day: int, time_idx: int, activity: VariableTimeActivity):
    """
    determins whether the time block at the given index is in the activity's time block
    """
    if activity.start_time.day <= day <= activity.end_time.day:
        if datetime_to_idx_dw(activity.start_time) <= time_idx <= datetime_to_idx_up(
                activity.end_time):
            return True
    return False
