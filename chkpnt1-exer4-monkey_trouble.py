#! python3
#CS-1 Checkpoint 1 - Exercise 4 - monkey_trouble
def monkey_trouble(monkey1,monkey2):
    import sys
    try:
        if (monkey1 == 1 and monkey2 == 1):
            print("True")
        elif(monkey1 == 0 and monkey2 == 0):
            print("True")
        else:
            print("False")
    except NameError: 
        print ("Error, please enter type 1 for true, 0 for false")
        sys.exit()
monkey1flag = int(input("monkey1 smiling?(type 1 for true, 0 for false)"))
monkey2flag = int(input("monkey2 smiling?(type 1 for true, 0 for false)"))
monkey_trouble(monkey1flag,monkey2flag)
