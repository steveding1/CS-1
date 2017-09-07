#! python3
#CS-1 Checkpoint 1 - Exercise 9 - alarm_clock
import sys
try:
    def alarm_clock(week,boole):
        week1 = int(week)
        if boole is True:
            if week1 in(0,6):
                print("off")     
            elif week1 in(1,2,3,4,5):
                print("10:00")
        else:
            if week1 in(1,2,3,4,5):
                print("7:00")     
            elif week1 in(0,6):
                print("10:00")
    
except NameError:
    print ("Error, please enter an interger and True/False")
    sys.exit()
