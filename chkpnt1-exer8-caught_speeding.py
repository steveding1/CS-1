#! python3
#CS-1 Checkpoint 1 - Exercise 8 - caught_speeding
import sys
def caught_speeding(speed,is_birthday):
    try:
        speed1 = int(speed)
        if is_birthday:
            return 0
        else:
            if speed1 <=60:
                return 0
            elif speed1 <=80:
                return 1
            else:
                return 2
            
    except NameError: 
        print ("Error, please enter an interger and True/False")
        sys.exit()
