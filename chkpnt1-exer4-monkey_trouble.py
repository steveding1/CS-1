#! python3
#CS-1 Checkpoint 1 - Exercise 4 - monkey_trouble
import sys
def monkey_trouble(monkey1,monkey2):
    try:
        if (monkey1 and monkey2) == True:
            return True
        elif(monkey1 == False and monkey2 == False):
            return True
        else:
            return False
    
    except NameError: 
        print ("Error, please enter \"True\" or \"False")
        sys.exit()
