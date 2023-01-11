from datetime import date, datetime, timedelta
import math

from utils import *
from Activity import FixedTimeActivity, VariableTimeActivity
from Planner import Planner


def arrange_after_deadline(planner: Planner, act: VariableTimeActivity, day: int, i: int, blank=None):
    """
    This function takes in a planner object, an activity object, an index and a day.
    It deals with the activity that are passed the deadline but remain unfinished.
    """
    if blank is None:
        blank = []

    pivot = i
    swapper = act.time_need - act.time_spent + i
    if swapper > 287:
        swapper = 287

    for i in range(pivot, swapper):
        blank.append(i)

    if act.start_time == planner.begining_date + timedelta(days=day):
        start_time = datetime_to_idx_dw(act.start_time)
    else:
        start_time = 0

    while pivot >= start_time:
        curr_act = planner.planner_lst[day].planner[pivot]
        if type(curr_act) == VariableTimeActivity:
            if curr_act.end_time == planner.begining_date + timedelta(days=day):
                curr_act_dll = datetime_to_idx_up(curr_act.end_time)
            else:
                curr_act_dll = 287

            for s in blank:
                if curr_act_dll < s and planner.planner_condition(day, [s]):
                    planner.fill_activity(curr_act, day, s)
                    planner.delete_activity(day, pivot)
                    blank.remove(s)

                    if idx_in_activity_timeblock(day, pivot, curr_act):
                        planner.fill_activity(act, day, idx_to_time(pivot))
                        if len(blank) == 0:
                            return True
                    else:
                        blank.append(pivot)
        pivot -= 1
    return False


def arrange_vta(planner: Planner):
    """
    This function takes in a planner obejcet and arrange all the variable time activities in the planner.
    """
    activities = []

    for act in planner.vta_lst.values():
        activities.append(act)

    for day in range(len(planner.planner_lst)):
        for i in range(287):
            if planner.planner_condition(day, [i]):
                for lst_idx in range(0, len(activities)):
                    act = activities[lst_idx]
                    if act.end_time < planner.begining_date + timedelta(days=day) + timedelta(minutes=i * 5):
                        if not arrange_after_deadline(planner, act, day, i):
                            print("Activities cannot be properly arranged")
                            return

                    end = i + act.min_timeblock
                    if end > 287:
                        end = 287

                    #input(f"{planner.planner_condition(day, list(range(i, end)))} {planner.max_time_condition(act, day)} {act.activity_condition(day)}")
                    if planner.planner_condition(day, list(range(i, end))) and \
                            planner.max_time_condition(act, day) and act.activity_condition(timedelta(days=day) + planner.begining_date):
                        planner.fill_activity(act, day, idx_to_time(i))
                        if act.time_need <= act.time_spent:
                            delta = timedelta(days=act.frequency)
                            if act.frequency == 0 or (act.start_time + delta).day > (planner.planner_lst[-1].current_day).day:
                                activities.remove(act)
                                if len(activities) == 0:
                                    return True
                            else:
                                act.time_spent = 0
                                act.start_time += delta
                                act.end_time += delta
                        break
                    else:
                        continue
            else:
                continue
