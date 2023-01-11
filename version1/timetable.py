from datetime import date
from version1.dailytimetable import DailyTimeTable


class TimeTable:
    '''
    # Path: time_table/time_table.py
    # 
    # Field: 
    #     max_time(int): maximum time allowed for the day
    #     max_study_time(int): maximum study time allowed for the day
    #     number_of_days(int): number of days in the time table
    #     day_timetable(list): list of daily_timetable objects
    #     fixed_time_activity_tbl(activity): dictionary of activity objects
    #     variable_time_activity_tbl(activity): dictionary of activity objects
    *     starting_date(date): starting date of the time table
    '''

    def __init__(self, max_time, max_study_time, number_of_days, starting_date=date.today()):
        self.max_time = max_time
        self.max_study_time = max_study_time
        self.number_of_days = number_of_days
        self.day_timetable = [DailyTimeTable() for i in range(number_of_days)]
        self.fixed_time_activity_tbl = {}
        self.variable_time_activity_tbl = {}
        self.starting_date = starting_date


