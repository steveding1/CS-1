#! python3
#CS-1 Checkpoint 1 - Exercise 5 - sum_double
import sys
try:
    def sum_double(boole,hour):
        hour1 = int(hour)
        if (boole and (hour1<=7 or hour1>=23) is True):
            print ("True")
        else:
            print ("False")
            
    
except ValueError:
    print ("Error, please enter a number as hour")
    sys.exit()
