from math import ceil
from datetime import date, datetime, timedelta


class Activity:
    def __init__(self, name, description, start_time, end_time, study, frequency=0):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.study = study
        self.frequency = frequency

    def __str__(self):
        return "Activity name: %s\nDescription: %s\nStart time: %s\nEnd time: %s\nStudy: %s\nFrequency: %s" % (
            self.name, self.description, self.start_time.__str__, self.end_time.__str__, self.study, self.frequency)

    def __eq__(self, other: "Activity"):
        return self.name == other.name and self.description == other.description and self.start_time == other.start_time and self.end_time == other.end_time and self.study == other.study and self.frequency == other.frequency

    def idx_in_time_range(self, daytime: datetime):
        if self.start_time <= daytime < self.end_time:
            return True


class FixedTimeActivity(Activity):
    def __init__(self, name, description, start_time, end_time, study, frequency=0):
        super().__init__(name, description, start_time, end_time, study, frequency)


class VariableTimeActivity(Activity):
    def __init__(self, name, description, start_time, end_time, time_needed, priority, min_timeblock, study,
                 frequency=0):
        super().__init__(name, description, start_time, end_time, study, frequency)
        self.time_need = ceil(time_needed / 5)
        self.time_spent = 0
        self.priority = priority
        self.min_timeblock = ceil(min_timeblock / 5)

    def __str__(self):
        return super().__str__() + "\nTime needed: %s\nTime spent: %s\nPriority: %s\nMin time block: %s" % (
            self.time_need, self.time_spent, self.priority, self.min_timeblock)

    def __eq__(self, other: "VariableTimeActivity"):
        return super().__eq__(
            other) and self.time_need == other.time_need and self.time_spent == other.time_spent and self.priority == other.priority and self.min_timeblock == other.min_timeblock

    def activity_condition(self, curr_day: date):
        """
        This function takes in a date object and returns True if the event can be added to the Planner object based on pre-set working pace and False otherwise.
        """
        if self.start_time.month <= curr_day.month <= self.end_time.month and self.start_time.day <= curr_day.day <= self.end_time.day:

            if self.end_time.day == curr_day.day or self.priority == 1:
                return True

            if self.time_spent == 0:
                return True

            if self.end_time.day == curr_day.day + 1:
                if self.time_spent / self.time_need < 0.75 or self.time_need - self.time_spent > 3 * 12:
                    return True

            if self.end_time.day == curr_day.day + 2:
                if self.time_spent / self.time_need < 0.5 or self.time_need - self.time_spent > 6 * 12:
                    return True

            if self.time_spent / self.time_need + 3:
                if self.time_need / self.time_spent < 0.2 or self.time_need - self.time_spent > 8 * 12:
                    return True

        return False
