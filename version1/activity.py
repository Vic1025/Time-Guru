from math import ceil


class FixedTimeActivity:
    '''
    # Path: activity/activity.py
    # 
    # Field: 
    #     name(string): name of the activity
    #     description(string): description of the activity
    #     starting_time(datetime): starting time of the activity
    #     ending_time(datetime): ending time of the activity
    #     study(bool): whether the activity is study or not
    #     frequency(int): frequency of the activity
    '''

    def __init__(self, name, description, start_time, end_time, study, frequency=0):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.study = study
        self.frequency = frequency

    def __str__(self):
        return "name: " + self.name + " description: " + self.description + " start_time: " + str(
            self.start_time) + " end_time: " + str(self.end_time) + " study: " + str(self.study) + " frequency: " + str(
            self.frequency)

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description and self.start_time == other.start_time and self.end_time == other.end_time and self.study == other.study and self.frequency == other.frequency


class VariableTimeActivity:
    '''
    # Path: activity/activity.py
    # 
    # Field: 
    #     name(str): name of the activity
    *     description(str): description of the activity
    #     start_time(str): start time of the activity
    #     end_time(str): end time of the activity
    #     time_needed(int): time needed for the activity (in minutes)
    #     time_spent(int): time spent on the activity (in minutes)
    #     priority(int): priority of the activity
    #     min_timeblock(int): minimum time block for the activity (in minutes)
    #     study(bool): whether the activity is study or not
    #     frequency(int): frequency of the activity, repeat every n days
    '''

    def __init__(self, name, description, start_time, end_time, time_needed, priority, min_timeblock, study,
                 frequency=0):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.time_need = ceil(time_needed / 5)
        self.time_spent = 0
        self.priority = priority
        self.min_timeblock = ceil(min_timeblock / 5)
        self.study = study
        self.frequency = frequency

    def __str__(self):
        return "Name: %s, Description: %s, Start time: %s, End time: %s, Time needed: %s, Time spent: %s, Priority: %s, Study: %s, Frequency: %s" % (
        self.name, self.description, self.start_time, self.end_time, self.time_need, self.time_spent, self.priority,
        self.study, self.frequency)

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description and self.start_time == other.start_time and self.end_time == other.end_time and self.time_need == other.time_need and self.time_spent == other.time_spent and self.priority == other.priority and self.study == other.study and self.frequency == other.frequency
