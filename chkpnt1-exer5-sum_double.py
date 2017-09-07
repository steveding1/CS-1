#! python3
#CS-1 Checkpoint 1 - Exercise 5 - sum_double
import sys
try:
    def sum_double(value1,value2):
        v1 = int(value1)
        v2 = int(value2)
        if v1 == v2:
            sum = (v1 + v2)*2
        else:
            sum = v1 + v2
        print(sum)
    
except NameError: 
    print ("Error, please enter 2 intergers")
    sys.exit()
