from datetime import datetime, date
import yaml

from Planner import Planner
from Activity import FixedTimeActivity, VariableTimeActivity
from arrangeFTA import arrange_fta
from arrangeVTA import arrange_vta
from utils import *


def main():
    test = "yaml_test/N_test/regular_N_vta.yaml"
    with open(test, 'r') as stream:
        dic = yaml.safe_load(stream)

    if dic["order"] == "N":
        planner = Planner(dic["num_of_days"], dic["max_time"], dic["max_study_time"],
                          datetime.fromisoformat(dic["begining_date"]))

        for event in dic["fta"]:
            event = event.strip()
            start_time = datetime.fromisoformat(dic["fta"][event]["start_time"])
            end_time = datetime.fromisoformat(dic["fta"][event]["end_time"])
            if not planner.planner_condition(start_time.day - start_time.day,
                                             list(range(datetime_to_idx_dw(start_time),
                                                        datetime_to_idx_up(end_time) + 1))):
                print("Cannot add {} to the planner".format(event))
                return

            if event == "breakfast" or event == "lunch" or event == "dinner":
                act = FixedTimeActivity(event, "", start_time, end_time, 0, 1)

            elif event == "sleep":
                act = FixedTimeActivity(event, "", start_time, end_time, 0, 1)
                if start_time.day != end_time.day:
                    planner.fta_lst[event] = act
                    seperat1 = datetime(start_time.year, start_time.month, start_time.day, 23, 59, 59)
                    act.end_time = seperat1
                    arrange_fta(planner, act)
                    seperat2 = datetime(end_time.year, end_time.month, end_time.day, 0, 0, 0)
                    act2 = FixedTimeActivity(event, "", seperat2, end_time, 0, 1)
                    arrange_fta(planner, act2)
                    continue

            else:
                act = FixedTimeActivity(event, dic["fta"][event]["description"], start_time, end_time,
                                        dic["fta"][event]["study"], dic["fta"][event]["frequency"])

            arrange_fta(planner, act)
            planner.fta_lst[event] = act
        for assignment in dic["vta"]:
            assignment = assignment.strip()
            assi = dic["vta"][assignment]
            start_time = datetime.fromisoformat(assi["start_time"])
            end_time = datetime.fromisoformat(assi["end_time"])
            act = VariableTimeActivity(assignment, assi["description"], start_time, end_time, assi["time_needed"],
                                       assi["priority"], assi["min_timeblock"], assi["study"], assi["frequency"])
            planner.vta_lst[assignment] = act

        arrange_vta(planner)
        planner.print_planner()


if __name__ == "__main__":
    main()
