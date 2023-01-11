from version1.utils import *

def print_daily_time_table(timetable, day_index):
    '''
    This function prints the time_table of a day in a time_table object.
    '''
    print("Day " + str(day_index + 1) + ":")
    for i in range(len(timetable.day_timetable[day_index].timetable)):
        if timetable.day_timetable[day_index].timetable[i] == timetable.day_timetable[day_index].timetable[i - 1]:
            if (i + 1 <= 287):
                if timetable.day_timetable[day_index].timetable[i + 1] != timetable.day_timetable[day_index].timetable[i] and timetable.day_timetable[day_index].timetable[i] != "":
                    print("ends at " + time_index_to_str(i + 1) + "\n")
            continue
        if timetable.day_timetable[day_index].timetable[i] != "":
            print((timetable.day_timetable[day_index].timetable[i]).strip())
            print("begins at: " + time_index_to_str(i))


def print_time_table(timetable):
    '''
    This function prints the time_table of a time_table object.
    '''
    for i in range(len(timetable.day_timetable)):
        print_daily_time_table(timetable, i)