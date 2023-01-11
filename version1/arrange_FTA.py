from datetime import date
from calendar import monthrange
import math as m

from version1.utils import *
from version1.activity import FixedTimeActivity
from version1.timetable import TimeTable

def arrange_FTA(time_table, event):
    '''
    This function takes a time_table object and an event object and
    arranges the event in the time_table.

    time_table : time_table object
    event : activity object
    '''
    starting_time = event.start_time
    ending_time = event.end_time
    starting_date = str_to_date(starting_time)
    if starting_date < time_table.starting_date.day:
        day_index = starting_date + monthrange(time_table.starting_date.year, time_table.starting_date.month)[1] - time_table.starting_date.day
    else:
        day_index = starting_date - time_table.starting_date.day
    begining_index = str_to_time_index_down(starting_time)
    ending_index = str_to_time_index_up(ending_time)

    id_lst = range(begining_index, ending_index)
    if not time_table_condition_f(time_table, day_index, id_lst, event):
        return

    time_table.fixed_time_activity_tbl[event.name] = event
    fill_activity_f(time_table, event, day_index, begining_index, ending_index)


    if event.frequency != 0:
        #print("This is a recurring event")
        i = day_index + event.frequency
        while i < len(time_table.day_timetable):
            #print("i = ", i)
            fill_activity_f(time_table, event, i, begining_index, ending_index)
            i += event.frequency
            

def arrange_FTA_lst(time_table, event_lst):
    for event in event_lst:
        arrange_FTA(time_table, event)


def input_eat(timetable, strs, f):
    '''
    start_time = input("Enter start time of your %s(hh:mm eg: 16:00): " % strs)
    end_time = input("Enter endtime: ")
    '''
    start_time = f.readline()
    end_time = f.readline()
    today = str(date.today().day) + "/"
    #assert today == "28/"
    act = FixedTimeActivity(strs, "", today + start_time, today + end_time, 0, 1)
    arrange_FTA(timetable, act)
    

def input_sleep(timetable, f):
    '''
    start_time = input("Enter start time of your sleep (hh:mm eg: 16:00): " )
    end_time = input("Enter endtime: ")
    '''
    start_time = f.readline()
    end_time = f.readline()

    today = str((date.today()).day) + "/"
    if int(start_time[:2]) < int(end_time[:2]):
        act = FixedTimeActivity("sleep", "", today + start_time, today + end_time, 0, 1)
        arrange_FTA(timetable, act)
    else:
        sleep1 = FixedTimeActivity("sleep", "", today + "00:00", today + end_time, 0, 1)
        arrange_FTA(timetable, sleep1)
        sleep2 = FixedTimeActivity("sleep", "", today + start_time, today + "23:59", 0, 1)
        arrange_FTA(timetable, sleep2)
