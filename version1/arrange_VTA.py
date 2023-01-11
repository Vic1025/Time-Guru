from version1.activity import VariableTimeActivity
from version1.utils import *
import math as m

def arrange_after_deadline(time_table, activity, activities_tbl, current_time, current_date):
    '''
    This function deals with the activities that are passed deadline but not finished.
    '''
    pivot = current_time
    swapper = activity.time_need - activity.time_spent + current_time

    blank_idx_lst = (range(current_time, swapper))

    if str_to_date(activity.start_time) == current_date + time_table.starting_date.day:
        start_time = str_to_time_index_down(activity.start_time)
    else:
        start_time = 0

    if swapper > 287:
        swapper = 287
    
    while pivot >= start_time:
        curr_act = time_table.day_timetable[current_date].timetable[pivot]

        if type(activities_tbl[curr_act]) == VariableTimeActivity:

            if str_to_date(activities_tbl[curr_act].end_time) == current_date + time_table.starting_date.day:
                curr_act_dll = str_to_time_index_up(activities_tbl[curr_act].end_time)
            else:
                curr_act_dll = 287

            s = swapper
            for s in blank_idx_lst:
                if curr_act_dll < s and time_table_condition_v(time_table, current_date, s, 1):
                    # min time block problem
                    fill_activity_v(time_table, current_date, s, activities_tbl[curr_act])
                    delete_activity_v(time_table, current_date, pivot, activities_tbl[curr_act])
                    blank_idx_lst.pop(s)

                    if idx_in_activity_timeblock(current_date, pivot, activities_tbl[curr_act]):
                        fill_activity_v(time_table, current_date, pivot, activity)

                        if len(blank_idx_lst) == 0:
                            return True
                    else:
                        blank_idx_lst.append(pivot)
                        
        pivot -= 1
    return False
                

            

        






'''
def arrange_VTA_lst(time_table):
    This function takes a time_table object and a list of activities
    and arranges the activities in the time_table.
    activities = []

    for act in time_table.variable_time_activity_tbl.values():
        activities.append(act)

    # sort the activities by start time
    activities.sort(key = lambda x: x.start_time)

    swapper = 0
    lst_idx = 0

    date_idx = str_to_date(activities[0].start_time) - time_table.starting_date.day
    input("date_idx: " + str(date_idx))
    while date_idx in range(len(time_table.day_timetable)):

        # each day starts from the first unfinished activity
        lst_idx = swapper

        today = time_table.day_timetable[date_idx]

        i = 0
        while i <= 287:
            #input("i: " + str(i))

            #input("lst_idx: " + str(lst_idx))
            act = activities[lst_idx]
            # if current acitivity's due date is before current time, call arrange_after_deadline
            if str_to_time_index_down(act.end_time) < i and str_to_date(act.end_time) == time_table.starting_date.day + date_idx:
                input("arrange after deadline")
                arrange_after_deadline(time_table, act, activities, i, date_idx)

            #input("%s" %today.timetable[i])
            if today.timetable[i] != "" or str_to_time_index_down(act.start_time) > i or str_to_date(act.start_time) > time_table.starting_date.day + date_idx:
                i += 1
                continue
            
            if time_table_condition_v(time_table, date_idx, i, act) == 1 and activity_condition(time_table, date_idx, act):
                input("arrange")
                i = fill_activity_v(time_table, date_idx, i, act)
                if time_table_resting_regulation(time_table, date_idx, i, act):
                    i = study_rest(time_table, date_idx, i)
                if act.time_spent >= act.time_need:
                    input("current activity finished")
                    if act.frequency != 0 and str_to_date(act.start_time) + act.frequency <= time_table.starting_date.day + time_table.number_of_days:
                        input("frequency != 0")
                        act.time_spent = 0
                        act.start_time = str(int(str_to_date(act.start_time)) + act.frequency) + act.start_time[2:]
                        act.end_time = str(int(str_to_date(act.end_time)) + act.frequency) + act.end_time[2:]
                        activities.pop(lst_idx)
                        for i in range(len(activities)):
                            if str_to_date(activities[i].start_time) > str_to_date(act.start_time) or (str_to_date(activities[i].start_time) == str_to_date(act.start_time) and str_to_time_index_down(activities[i].start_time) > str_to_time_index_down(act.start_time)):
                                activities.insert(i, act)
                                break
                        if act not in activities:
                            activities.append(act)
                    else:
                        input("frequency == 0")
                        temp = act
                        act = activities[swapper]
                        activities[swapper] = temp
                        swapper += 1
                        lst_idx += 1
                        if swapper == len(activities):
                            return
                i += 1
            else:
                if (not activity_condition(time_table, date_idx, act) or (time_table_condition_v(time_table, date_idx, i, act) == 2 and act.study)) and lst_idx != len(activities):
                    lst_idx += 1
                    continue
                elif lst_idx != len(activities):
                    lst_idx += 1
                i += 1
        date_idx += 1
'''


def arrange_VTA_lst(time_table):
    '''
    This function takes a time_table object and a list of activities
    and arranges the activities in the time_table.
    '''
    activities = []

    for act in time_table.variable_time_activity_tbl.values():
        activities.append(act)
        input("act: " + act.name)

    # sort the activities by start time
    #activities.sort(key = lambda x: str_to_date(x.start_time))

    swapper = 0
    lst_idx = 0

    date_idx = str_to_date(activities[0].start_time) - time_table.starting_date.day

    while date_idx in range(len(time_table.day_timetable)):
        input("date_idx: " + str(date_idx))

        lst_idx = swapper
        i = 0

        while i <= 287:
            lst_idx = swapper

            if str_to_time_index_down(act.end_time) < i and str_to_date(act.end_time) == time_table.starting_date.day + date_idx:
                input("arrange after deadline")
                arrange_after_deadline(time_table, act, time_table.variable_time_activity_tbl, i, date_idx)

            if not time_table_condition_v(time_table, date_idx, i, 1):
                #input("not available")
                i += 1
                continue
            else:
                while lst_idx <= len(activities) - 1:
                    #input("lst_idx: " + str(lst_idx))
                    act = activities[lst_idx]

                    if idx_in_activity_timeblock(date_idx + time_table.starting_date.day, i, act):
                        input("in activity timeblock")

                        if time_table_condition_v(time_table, date_idx, i, act.min_timeblock) and activity_condition(time_table, date_idx, act):
                            input("arrange")

                            i = fill_activity_v(time_table, date_idx, i, act)
                            if time_table_resting_regulation(time_table, date_idx, i, act):
                                i = study_rest(time_table, date_idx, i)

                            if act.time_spent >= act.time_need:
                                input("current activity finished")
                                if act.frequency != 0 and str_to_date(act.start_time) + act.frequency <= time_table.starting_date.day + time_table.number_of_days:
                                    input("frequency != 0")
                                    act.time_spent = 0
                                    act.start_time = str(int(str_to_date(act.start_time)) + act.frequency) + act.start_time[2:]
                                    act.end_time = str(int(str_to_date(act.end_time)) + act.frequency) + act.end_time[2:]
                                    activities.pop(lst_idx)
                                    for i in range(len(activities)):
                                        if str_to_date(activities[i].start_time) > str_to_date(act.start_time) or (str_to_date(activities[i].start_time) == str_to_date(act.start_time) and str_to_time_index_down(activities[i].start_time) > str_to_time_index_down(act.start_time)):
                                            activities.insert(i, act)
                                            break
                                    if act not in activities:
                                        activities.append(act)
                                else:
                                    input("frequency == 0")
                                    temp = act
                                    act = activities[swapper]
                                    activities[swapper] = temp
                                    swapper += 1
                                    lst_idx += 1
                                    input("done:? " + str(swapper == len(activities)))
                                    if swapper == len(activities):
                                        return
                            i += 1
                            continue
                    lst_idx += 1
                i += 1
        date_idx += 1   
                            
            

