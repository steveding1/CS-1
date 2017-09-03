#CS-1 Task 4.2 - Exercise 7 from Steve Ding
def computegrade(score):
    try:
        if (score < 0):
            print ('Bad score')
        elif score < 0.6:
            print ('F')
        elif score < 0.7:
            print ('D')
        elif score < 0.8:
            print ('C')
        elif score < 0.9:
            print ('B')
        elif score <= 1:
            print ('A')
        else:
            print ('Bad score')
    except ValueError: 
        print ("Bad score")
