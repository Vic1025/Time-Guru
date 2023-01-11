from version1.activity import FixedTimeActivity, VariableTimeActivity

def input_fixed_time_act(f):
    '''
    name = input("Enter name of the activity (Enter Q to quit adding): ")
    if name == "Q":
        return fixed_time_activity("None", "None", "None", "None", 0, 0)
    description = input("Enter description of the activity: ")
    start_time = input("Enter start time of the activity(dd/hh:mm eg: 13,16:00): ")
    end_time = input("Enter endtime of the activity: ")
    study = int(input("Enter whether the activity is study or not (1 for yes, 0 for No): "))
    frequency = int(input("Enter frequency of the activity, repeat every n days: "))
    '''
    name = f.readline()
    if name == "Q":
        return FixedTimeActivity("None", "None", "None", "None", 0, 0)
    description = f.readline()
    start_time = f.readline()
    end_time = f.readline()
    study = int(f.readline())
    frequency = int(f.readline())

    return FixedTimeActivity(name, description, start_time, end_time, study, frequency)

def input_variable_time_act(f):
    '''
    name = input("Enter name of the activity (Enter Q to quit adding): ")
    if name == "Q":
        return variable_time_activity("None", "None", "None", "None", "None", 0, 0)
    description = input("Enter description of the activity: ")
    start_time = input("Enter start time of the activity(dd/hh:mm eg: 13,16:00): ")
    duration = int(input("Enter duration of the activity: "))
    deadline = input("Enter deadline of the activity: ")
    min_timeblock = int(input("Enter minimum time block for the activity (in minutes): "))
    priority = int(input("Enter priority of the activity: "))
    study = bool(input("Enter whether the activity is study or not: "))
    frequency = int(input("Enter frequency of the activity, repeat every n days: "))
    '''

    name = f.readline()
    if name.strip() == "Q":
        return FixedTimeActivity("None", "None", "None", "None", 0, 0)
    description = f.readline()
    start_time = f.readline()
    deadline = f.readline()
    duration = int(f.readline())
    priority = int(f.readline())
    min_timeblock = int(f.readline())
    study = int(f.readline())
    frequency = int(f.readline())

    return VariableTimeActivity(name, description, start_time, deadline, duration, priority, min_timeblock, study, frequency)
