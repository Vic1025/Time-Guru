from version2.print_tools import print_time_table, print_daily_time_table
from version1.timetable import TimeTable
from version1.arrange_FTA import *
from version1.arrange_VTA import *
from version1.input_tools import *

def set_up_time_table(f):
    # initialize the time_table
    '''
    max_time = int(input("Enter the maximum time you can be effective: "))
    max_study_time = int(input("Enter the maximum time you can study: "))
    num_of_days = int(input("Enter the number of days you want to plan: "))
    '''
    max_time = int(f.readline())
    max_study_time = int(f.readline())
    num_of_days = int(f.readline())

    # Get the time_table object
    time_table1 = TimeTable(max_time, max_study_time, num_of_days)

    # set the sleeping time and eating time
    input_eat(time_table1, "breakfast", f)
    input_eat(time_table1, "lunch", f)
    input_eat(time_table1, "dinner", f)
    input_sleep(time_table1, f)

    return time_table1

def fixed_time_activity(time_table, f):
    '''
    input("Now, you can add your fixed time activities: ")
    input("Those activities are often coming with a begining time spot and an ending time spot, such as a test, a meeting or a lecture: ")
    input("What you need to provide is the name of the activity, the begining time, the ending time and the frequency of it: ")
    input("Enter Q to quit adding fixed time activities when name for a new activity is requested: ")
    '''
    while True:
        act = input_fixed_time_act(f)
        if act.name == "None":
            break
        else:
            arrange_FTA(time_table, act)

def variable_length_activity(time_table, f):   
    '''
    input("Now, you can add your variable length activities: ")
    input("Those activities are often coming with a begining time spot, a deadline and a duration, such as a homework or a project: ")
    input("What you need to provide is the name of the activity, the begining time, the deadline, estimated duration and the frequency of it: ")
    input("Press Q to quit adding variable length activities when name for a new activity is requested: ")
    '''
    while True:
        act = input_variable_time_act(f)
        if act.name == "None":
            break
        else:
            time_table.variable_time_activity_tbl[act.name.strip()] = act
    
    for act in time_table.variable_time_activity_tbl:
        input("activity: " + act)
    
    arrange_VTA_lst(time_table)


def test_slot(time_table1):
    print("0: " + time_table1.day_timetable[0].timetable[0] + "\n")
    print("1: " + time_table1.day_timetable[0].timetable[12] + "\n")
    print("2: " + time_table1.day_timetable[0].timetable[24] + "\n")
    print("3: " + time_table1.day_timetable[0].timetable[35] + "\n")
    print("4: " + time_table1.day_timetable[0].timetable[47] + "\n")
    print("5: " + time_table1.day_timetable[0].timetable[59] + "\n")
    print("6: " + time_table1.day_timetable[0].timetable[71] + "\n")
    print("7: " + time_table1.day_timetable[0].timetable[83] + "\n")
    print("8: " + time_table1.day_timetable[0].timetable[95] + "\n")
    print("9: " + time_table1.day_timetable[0].timetable[107] + "\n")
    print("10: " + time_table1.day_timetable[0].timetable[119] + "\n")
    print("11: " + time_table1.day_timetable[0].timetable[131] + "\n")
    print("12: " + time_table1.day_timetable[0].timetable[143] + "\n")
    print("13: " + time_table1.day_timetable[0].timetable[155] + "\n")
    print("14: " + time_table1.day_timetable[0].timetable[167] + "\n")
    print("15: " + time_table1.day_timetable[0].timetable[179] + "\n")
    print("16: " + time_table1.day_timetable[0].timetable[191] + "\n")
    print("17: " + time_table1.day_timetable[0].timetable[203] + "\n")
    print("18: " + time_table1.day_timetable[0].timetable[215] + "\n")
    print("19: " + time_table1.day_timetable[0].timetable[227] + "\n")
    print("20: " + time_table1.day_timetable[0].timetable[239] + "\n")
    print("21: " + time_table1.day_timetable[0].timetable[251] + "\n")
    print("22: " + time_table1.day_timetable[0].timetable[263] + "\n")
    print("23: " + time_table1.day_timetable[0].timetable[275] + "\n")
    print("\n")
    print("0: " + time_table1.day_timetable[1].timetable[0] + "\n")
    print("1: " + time_table1.day_timetable[1].timetable[12] + "\n")
    print("2: " + time_table1.day_timetable[1].timetable[24] + "\n")
    print("3: " + time_table1.day_timetable[1].timetable[35] + "\n")
    print("4: " + time_table1.day_timetable[1].timetable[47] + "\n")
    print("5: " + time_table1.day_timetable[1].timetable[59] + "\n")
    print("6: " + time_table1.day_timetable[1].timetable[71] + "\n")
    print("7: " + time_table1.day_timetable[1].timetable[83] + "\n")
    print("8: " + time_table1.day_timetable[1].timetable[95] + "\n")
    print("9: " + time_table1.day_timetable[1].timetable[107] + "\n")
    print("10: " + time_table1.day_timetable[1].timetable[119] + "\n")
    print("11: " + time_table1.day_timetable[1].timetable[131] + "\n")
    print("12: " + time_table1.day_timetable[1].timetable[143] + "\n")
    print("13: " + time_table1.day_timetable[1].timetable[155] + "\n")
    print("14: " + time_table1.day_timetable[1].timetable[167] + "\n")
    print("15: " + time_table1.day_timetable[1].timetable[179] + "\n")
    print("16: " + time_table1.day_timetable[1].timetable[191] + "\n")
    print("17: " + time_table1.day_timetable[1].timetable[203] + "\n")
    print("18: " + time_table1.day_timetable[1].timetable[215] + "\n")
    print("19: " + time_table1.day_timetable[1].timetable[227] + "\n")
    print("20: " + time_table1.day_timetable[1].timetable[239] + "\n")
    print("21: " + time_table1.day_timetable[1].timetable[251] + "\n")
    print("22: " + time_table1.day_timetable[1].timetable[263] + "\n")
    print("23: " + time_table1.day_timetable[1].timetable[275] + "\n")
    print("\n")
    print("0: " + time_table1.day_timetable[2].timetable[0] + "\n")
    print("1: " + time_table1.day_timetable[2].timetable[12] + "\n")
    print("2: " + time_table1.day_timetable[2].timetable[24] + "\n")
    print("3: " + time_table1.day_timetable[2].timetable[35] + "\n")
    print("4: " + time_table1.day_timetable[2].timetable[47] + "\n")
    print("5: " + time_table1.day_timetable[2].timetable[59] + "\n")
    print("6: " + time_table1.day_timetable[2].timetable[71] + "\n")
    print("7: " + time_table1.day_timetable[2].timetable[83] + "\n")
    print("8: " + time_table1.day_timetable[2].timetable[95] + "\n")
    print("9: " + time_table1.day_timetable[2].timetable[107] + "\n")
    print("10: " + time_table1.day_timetable[2].timetable[119] + "\n")
    print("11: " + time_table1.day_timetable[2].timetable[131] + "\n")
    print("12: " + time_table1.day_timetable[2].timetable[143] + "\n")
    print("13: " + time_table1.day_timetable[2].timetable[155] + "\n")
    print("14: " + time_table1.day_timetable[2].timetable[167] + "\n")
    print("15: " + time_table1.day_timetable[2].timetable[179] + "\n")
    print("16: " + time_table1.day_timetable[2].timetable[191] + "\n")
    print("17: " + time_table1.day_timetable[2].timetable[203] + "\n")
    print("18: " + time_table1.day_timetable[2].timetable[215] + "\n")
    print("19: " + time_table1.day_timetable[2].timetable[227] + "\n")
    print("20: " + time_table1.day_timetable[2].timetable[239] + "\n")
    print("21: " + time_table1.day_timetable[2].timetable[251] + "\n")
    print("22: " + time_table1.day_timetable[2].timetable[263] + "\n")
    print("23: " + time_table1.day_timetable[2].timetable[275] + "\n")
    print("\n")

def main():
    '''
    print_daily_time_table(time_table1, 0)
    print_time_table(time_table1)
    '''
    f = open("test/VA_test/normal_test_in3.txt", "r")
    time_table1 = set_up_time_table(f)
    #time_table1 = TimeTable(8, 6, 3)
    #input("Now we are going to input your activities. Press any key to continue for every following sentence.")
    #fixed_time_activity(time_table1, f)
    #test_slot(time_table)
    variable_length_activity(time_table1, f)
    f.close()
    print_time_table(time_table1)

    

if __name__ == "__main__":
    main()

    
