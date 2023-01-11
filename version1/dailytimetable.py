class DailyTimeTable:
    '''
    # Path: daily_timetable/day_tt.py

    Field: 
        used_time(int): time used for the day
        used_study_time(int): study time used for the day
        timetable(list): list of time blocks each representing 5 minutes
    '''

    def __init__(self):
        self.used_time = 0
        self.used_study_time = 0
        self.timetable = ["" for i in range(288)]

    
