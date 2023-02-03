order: N
num_of_days: n (int)
max_time: n (int, in hour)
max_study_time: n (int, in hour)
begining_date: yy-mm-dd
fta:
  breakfast:
    start_time: yy-mm-ddThh:mm 
    end_time: yy-mm-ddThh:mm
  lunch (with value same as above)
  dinner
  sleep
  event_name:
    start_time: yy-mm-ddThh:mm 
    end_time: yy-mm-ddThh:mm
    description: str
    frequency: n (int, this event will reoccur every n days)
    study: x (bool, wether or not this event is study-related)
  ...
vta:
  event_name:
    description: str
    start_time: yy-mm-ddThh:mm 
    end_time: yy-mm-ddThh:mm
    frequency: n (int, this event will reoccur every n days)
    study: x (bool, wether or not this event is study-related)
    time_needed: n (int, time needed to finish this event, in minutes)
    priority: x (1, 2 or 3)
    min_timeblock: n (int, minimum decompostion of the given event that make sence, in minutes)
  ...

