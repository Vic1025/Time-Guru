import math as m

from version1.activity import FixedTimeActivity, VariableTimeActivity
from version1.timetable import TimeTable

def str_to_date(str):
    '''
    convert the time string to the index of the date block
    '''
    # str format: dd/hh:mm eg: 13/16:00
    return int(str[:2])

def str_to_time_index_up(str):
    '''
    convert the time string to the index of the time block, time block is rounded up
    '''
    # str format: dd/hh:mm eg: 13/16:00
    hour = int(str[3:5])
    minute = int(str[6:8])
    return hour * 12 + m.ceil(minute / 5)

def str_to_time_index_down(str):
    '''
    convert the time string to the index of the time block, time block is rounded down
    '''
    # str format: dd/hh:mm eg: 13/16:00
    hour = int(str[3:5])
    minute = int(str[6:8])
    return hour * 12 + m.floor(minute / 5)

def time_index_to_str(time_index):
    '''
    convert the index of the time block to the time string
    '''
    hour = time_index // 12
    minute = (time_index % 12) * 5
    return "{:02d}:{:02d}".format(hour, minute)

def date_index_to_int(time_table, date_idx):
    '''
    convert the day index of given time table into date
    '''
    return date_idx + time_table.starting_date.day

def time_table_condition_f(time_table, date_idx, time_idx_lst, activity):
    '''
    This function takes a time_table object and an activity object and
    returns a boolean value indicating whether the activity can be
    arranged in the time_table or not.
    '''
    for time_idx in time_idx_lst:
        # basic condition: every miniute starting from current time_idx until one min_timeblock of the activity is free
        basic_condition = True
        if time_table.day_timetable[date_idx].timetable[time_idx] != "":
            basic_condition = False
            print("You have to do %s at %02d, %s. There's a time conflict with %s, try another time." % (time_table.day_timetable[date_idx].timetable[time_idx], date_index_to_int(time_table, date_idx), time_index_to_str(time_idx), activity.name))
    
    # second condition: up to 6 hours of study time
    condition_two = False
    if (not activity.study) or time_table.day_timetable[date_idx].used_study_time + len(time_idx_lst) <= time_table.max_study_time * 12: 
        condition_two = True
    else:
        print("You have reached maximum studying time while inserting %s, try another time." % activity.name)

        # third condition: up to 8 hours of total time
    condition_three = False
    if time_table.day_timetable[date_idx].used_time + len(time_idx_lst) <= time_table.max_time * 12:
        condition_three = True
    else:
        print("You have reached maximum time while inserting %s, try another time." % activity.name)
    
    return basic_condition and condition_two and condition_three
    
def time_table_condition_v(time_table, date_idx, time_idx, num_of_idx):
    '''
    This function takes a time_table object and an activity object and
    returns a boolean value indicating whether the activity can be
    arranged in the time_table or not.
    '''
    # basic condition: every miniute starting from current time_idx until one min_timeblock of the activity is free
    basic_condition = True
    for i in range(time_idx, time_idx + num_of_idx):
        if i <= 287:
            if time_table.day_timetable[date_idx].timetable[i] != "":
                basic_condition = False
                #input("You have to do %s at %02d, %s, try another time." % (time_table.day_timetable[date_idx].timetable[i], date_index_to_int(time_table, date_idx), time_index_to_str(i)))
                break

    # third condition: up to 8 hours of total time
    condition_three = False
    if time_table.day_timetable[date_idx].used_time + num_of_idx <= time_table.max_time * 12:
        condition_three = True
    #if not condition_three:
        #input("You have reached maximum time at idx %s, try another time." %time_idx)

    return basic_condition and condition_three

def study_max_condition(time_table, date_idx, activity):
    # second condition: up to 6 hours of study time
    condition_two = False
    if not activity.study or time_table.day_timetable[date_idx].used_study_time + activity.min_timeblock <= time_table.max_study_time * 12:
        condition_two = True
    
    return condition_two

def idx_in_activity_timeblock(day, time_idx, activity):
    '''
    determins whether the time block at the given index is in the activity's time block
    '''
    if str_to_date(activity.start_time) > day:
        return False
    elif str_to_date(activity.start_time) <= day and str_to_date(activity.end_time) >= day:
        if str_to_time_index_down(activity.start_time) <= time_idx and str_to_time_index_up(activity.end_time) >= time_idx:
            return True
        else:
            return False

def activity_condition(time_table, date_idx, activity):
    '''
    This function takes a time_table object and an activity object and
    returns a boolean value indicating whether the activity should be
    arranged in the time_table based on the pre-set working pace.
    '''
    activity_date = str_to_date(activity.start_time)
    
    # if the activity is due today, or it's in P1 priority， it should be arranged.
    if activity_date == time_table.starting_date.day + date_idx or activity.priority == 1:
        return True
    
    # if the activity is due within two days, it should be arranged if less than 75% of work is done 
    #   or more than 3 hours' work are left.
    if activity_date == time_table.starting_date.day + date_idx + 1:
        if activity.time_spent / activity.time_need < 0.75 or activity.time_need - activity.time_spent > 3:
            return True
    
    # if the activity is due within three days, it should be arranged if less than 50% of work is done
    #   or more than 6 hours' work are left.
    if activity_date == time_table.starting_date.day + date_idx + 2:
        if activity.time_spent / activity.time_need < 0.5 or activity.time_need - activity.time_spent > 6:
            return True
    
    # if the activity is due more than days, it should be arranged if less than 20% of work is done
    #   or more than 8 hours' work are left.
    if activity_date > time_table.starting_date.day + date_idx + 2:
        if activity.time_spent / activity.time_need < 0.2 or activity.time_need - activity.time_spent > 8:
            return True
    
    return False

def study_rest(time_table, day_idx, time_idx):
    '''
    fill the study rest time blocks into the time_table
    '''
    time_table.day_timetable[day_idx].timetable[time_idx] = "rest for study"
    time_table.day_timetable[day_idx].timetable[time_idx + 1] = "rest for study"
    return time_idx + 2


def time_table_resting_regulation(time_table, day_idx, time_idx, activity):
    '''
    determins whether a resting time block is needed after the time block at the given index
    '''
    study_over_an_hour = True

    if activity.study:
        for t in range(time_idx - 12, time_idx):
            if time_table.day_timetable[day_idx].timetable[t] != "" and time_table.day_timetable[day_idx].timetable[t] in time_table.variable_time_activity_tbl:    
                if not time_table.variable_time_activity_tbl[time_table.day_timetable[day_idx].timetable[t].strip()].study:
                    study_over_an_hour = False
                    break
            else:
                study_over_an_hour = False
                break
    else:
        study_over_an_hour = False
    input("study_over_an_hour: %s" % study_over_an_hour)
    return study_over_an_hour


def fill_activity_v(time_table, date_idx, time_idx, activity):
    '''
    fill the variable time activity into the time_table
    '''
    input("filling %s" % activity.name)
    num_of_idx = activity.min_timeblock
    for i in range(time_idx, time_idx + num_of_idx):
        time_table.day_timetable[date_idx].timetable[i] = activity.name
    
    activity.time_spent += activity.min_timeblock

    if activity.study:
        time_table.day_timetable[date_idx].used_study_time += activity.min_timeblock
    
    time_table.day_timetable[date_idx].used_time += activity.min_timeblock
    return time_idx + num_of_idx


def delete_activity_v(time_table, date_idx, time_idx, activity):
    '''
    delete the variable time activity from the time_table
    '''
    num_of_idx = activity.min_timeblock
    for i in range(time_idx, time_idx + num_of_idx):
        time_table.day_timetable[date_idx].timetable[i] = None
    
    activity.time_spent -= activity.min_timeblock

    if activity.study:
        time_table.day_timetable[date_idx].used_study_time -= activity.min_timeblock / 5
        time_table.day_timetable[date_idx][time_idx + num_of_idx + 1] = None
        time_table.day_timetable[date_idx][time_idx + num_of_idx + 2] = None
    
    time_table.day_timetable[date_idx].used_time -= activity.min_timeblock


def fill_activity_f(time_table, activity, day_idx, begining_index, ending_index):
    '''
    fill the fixed time activity into the time_table
    '''
    for i in range(begining_index, ending_index):
        time_table.day_timetable[day_idx].timetable[i] = activity.name

    if activity.name != "breakfast" and activity.name != "lunch" and activity.name != "dinner" and activity.name != "sleep" and activity.name != "rest for study":
        time_table.day_timetable[day_idx].used_time += (ending_index - begining_index)
        if activity.study:
            time_table.day_timetable[day_idx].used_study_time += (ending_index - begining_index)
    


def delete_activity_f(time_table, day_idx, begining_index, ending_index):
    '''
    delete the fixed time activity from the time_table
    '''
    for i in range(begining_index, ending_index):
        time_table.day_timetable.timetable[day_idx].timetable[i] = None
    
    time_table.day_timetable[day_idx].used_time -= (ending_index - begining_index)


def event_exchange(time_table, day_idx1, time_idx1, day_idx2, time_idx2):
    '''
    exchange the event between two time blocks
    '''
    temp = time_table.TimeTable[day_idx1].timetable[time_idx1]
    time_table.TimeTable[day_idx1].timetable[time_idx1] = time_table.TimeTable[day_idx2].timetable[time_idx2]
    time_table.TimeTable[day_idx2].timetable[time_idx2] = temp


def timeblock_exchange(time_table, day_idx1, time_idx1_begin, time_idx1_end, day_idx2, time_idx2_begin, time_idx2_end):
    '''
    exchange the time blocks between two time blocks
    requires: time_idx1_end - time_idx1_begin == time_idx2_end - time_idx2_begin
    '''
    for i in range(time_idx1_begin, time_idx1_end):
        event_exchange(time_table, day_idx1, i, day_idx2, i)
    
    for i in range(time_idx2_begin, time_idx2_end):
        event_exchange(time_table, day_idx1, i, day_idx2, i)

