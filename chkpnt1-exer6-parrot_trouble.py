#! python3
#CS-1 Checkpoint 1 - Exercise 6 - parrot_troubletry:
def sum_double(boole,hour):
    hour1 = int(hour)
    if (boole and (hour1<7 or hour1>23) is True):
        print ("True")
    else:
        print ("False")

import sys
try:
    boole_flag = input("if the parrot is talking(input True if talking and False if not) ")
    hour_flag = int(input("what hours is now? "))
except ValueError:
    print ("Error, please enter a number as hour")
    sys.exit()
if boole_flag is "True" or True:
    boole_flag1 = True
elif boole_flag is "False" or False:
    boole_flag1 = False
else:
    print ("Error, please enter True or False as if the parrot is talking")
    sys.exit()
sum_double(boole_flag,hour_flag)
