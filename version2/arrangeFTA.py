from datetime import date, datetime, timedelta
import math

from utils import *
from Activity import FixedTimeActivity, VariableTimeActivity
from Planner import Planner


def arrange_fta(planner: Planner, event: FixedTimeActivity):
    """
    This function takes a time_table object and an event object and
    arranges the event in the time_table.

    time_table : time_table object
    event : activity object
    """
    starting_time = event.start_time
    ending_time = event.end_time
    day_index = starting_time.day - planner.begining_date.day

    id_lst = list(range(starting_time.hour * 12 + math.floor(starting_time.minute / 5),
                        ending_time.hour * 12 + math.ceil(ending_time.minute / 5)))
    if not planner.planner_condition(day_index, id_lst) or not planner.max_time_condition(event, day_index):
        print("You cannot add this event at this time")
        return

    planner.fta_lst[event.name] = event
    planner.fill_activity(event, day_index, event.start_time)

    if event.frequency != 0:
        i = day_index + event.frequency
        while i < len(planner.planner_lst):
            planner.fill_activity(event, i, event.start_time)
            i += event.frequency
