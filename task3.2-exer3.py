#CS-1 Task 3.2 - Exercise 3 from Steve Ding
try:
    score = float(input('Enter score: '))
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
