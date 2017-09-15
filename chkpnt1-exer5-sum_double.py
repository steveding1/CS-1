#! python3
#CS-1 Checkpoint 1 - Exercise 5 - sum_double
def sum_double(value1,value2):
    v1 = int(value1)
    v2 = int(value2)
    if v1 == v2:
        sum = (v1 + v2)*2
    else:
        sum = v1 + v2
    print(sum)

import sys
try:
    v1 = int(input("plz input value1 = "))
    v2 = int(input("plz input value2 = "))
except ValueError: 
    print ("plz input intergers only")
    sys.exit()
sum_double(v1,v2)
