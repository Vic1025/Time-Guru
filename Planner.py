import math
from datetime import date, datetime, timedelta, time

from utils import *
from Activity import FixedTimeActivity, VariableTimeActivity


class DailyPlanner:
    def __init__(self, curr_day):
        self.current_day = curr_day
        self.planner = [""] * 288
        self.time_spent = 0
        self.study_time = 0

    def __str__(self):
        return "Planner: %s\nTime spent: %s\nStudy time: %s" % (
            list(x for x in self.planner), self.time_spent, self.study_time)

    def __eq__(self, other: "DailyPlanner"):
        return self.planner == other.planner and self.time_spent == other.time_spent and self.study_time == other.study_time


class Planner:
    def __init__(self, num_of_days: int, max_time: int, max_study_time: int, begining_date: date):
        self.max_time = max_time
        self.max_study_time = max_study_time
        self.begining_date = begining_date
        self.planner_lst = [DailyPlanner(begining_date) for i in range(num_of_days)]
        self.vta_lst = {}
        self.fta_lst = {}

        for i in range(num_of_days):
            self.planner_lst[i].current_day = begining_date + timedelta(days=i)

    def __eq__(self, other: "Planner"):
        return self.max_time == other.max_time and self.max_study_time == other.max_study_time and self.begining_date == \
               other.begining_date and self.planner_lst == other.planner_lst and self.vta_lst == other.vta_lst and self.fta_lst == other.fta_lst

    def planner_condition(self, day_index: int, id_lst: list):
        """
        This function takes in a Planner object, a day_index, a list of id's and an self object
        and returns True if the self can be added to the Planner objectand False otherwise.
        """
        if day_index < 0 or day_index >= len(self.planner_lst):
            print("You cannot add because the day index is out of range")
            return False

        for i in id_lst:
            if self.planner_lst[day_index].planner[i] != "":
                #print("time at %s:%s is not empty" % (i // 12, i % 12 * 5))
                return False

        return True

    def max_time_condition(self, event: "Activity", day_index: int):
        """
        This function takes in an activity object, a day_index, a starting_time and an ending_time
        and returns True if the self can be added to the Planner objectand False otherwise.
        """
        if type(event) == FixedTimeActivity:
            dur_time = datetime_to_idx_dw(event.start_time) - datetime_to_idx_up(event.end_time)
        else:
            dur_time = event.min_timeblock

        if event.study and self.planner_lst[day_index].study_time + dur_time > self.max_study_time * 12:
            print("You cannot add %s at because it will exceed your study time limit" % event.name)
            return False

        if self.planner_lst[day_index].time_spent + dur_time > self.max_time * 12:
            print(f"{self.planner_lst[day_index].time_spent} {self.max_time * 12}")
            print("You cannot add %s because it will exceed your time limit" % event.name)
            return False

        return True

    def fill_activity(self, event: "Activity", day_index: int, start_time: datetime):
        """
        This function takes in an activity object, a day_index, a starting_time and an ending_time
        and fills the planner object with the self object.
        """
        start_idx = datetime_to_idx_dw(start_time)

        if type(event) == FixedTimeActivity:
            end_idx = datetime_to_idx_up(event.end_time)
        else:
            end_idx = start_idx + event.min_timeblock

        for i in range(start_idx, end_idx):
            self.planner_lst[day_index].planner[i] = event.name

        if event.name != "sleep" and event.name != "breakfast" and event.name != "lunch" and event.name != "dinner":
            self.planner_lst[day_index].time_spent += end_idx - start_idx
            if event.study:
                self.planner_lst[day_index].study_time += end_idx - start_idx

        if type(event) == VariableTimeActivity:
            event.time_spent += end_idx - start_idx

    def delete_activity(self, event: "Activity", day_idx: int):
        """
        This function takes in an activity object, a day_index, a starting_time and an ending_time
        and deletes the self object from the planner object.
        """
        start_idx = datetime_to_idx_dw(event.start_time)
        end_idx = datetime_to_idx_up(event.end_time)

        for i in range(start_idx, end_idx):
            if self.planner_lst[day_idx].planner[i] == event.name:
                self.planner_lst[day_idx].planner[i] = ""

        if type(event) == VariableTimeActivity:
            event.time_spent -= event.time_need
            self.vta_lst.pop(event.name)
        else:
            self.fta_lst.pop(event.name)

        self.planner_lst[day_idx].time_spent -= (end_idx - start_idx)

    def print_day(self, day_idx: int):
        """
        This function takes in a Planner object and a day_index and prints out the planner for that day.
        """
        print("%s-%s-%s:\n" % (self.planner_lst[day_idx].current_day.year, self.planner_lst[day_idx].current_day.month,
                               self.planner_lst[day_idx].current_day.day))

        for i in range(287):
            if self.planner_lst[day_idx].planner[i] == self.planner_lst[day_idx].planner[i - 1]:
                if self.planner_lst[day_idx].planner[i] != "" and i != 287:
                    if self.planner_lst[day_idx].planner[i] != self.planner_lst[day_idx].planner[i + 1]:
                        print("ends at %02d:%02d\n" % ((i + 1) // 12, (i + 1) % 12 * 5))
                continue
            if self.planner_lst[day_idx].planner[i] != "":
                print("%s" % self.planner_lst[day_idx].planner[i])
                print("starts at %02d:%02d" % (i // 12, i % 12 * 5))

    def print_planner(self):
        """
        This function takes in a Planner object and prints out the planner for that day.
        """
        for i in range(len(self.planner_lst)):
            self.print_day(i)
            print("")
