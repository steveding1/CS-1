#CS-1 Task 4.2 - Exercise 6 from Steve Ding
def computepay(hours,rate):
    try:
        pay = 0
        if hours >40:
            pay = 40*rate+(hours-40)*1.5*rate
        else:
            pay = hours*rate
        print ('Pay: ', round(pay,2))
    except ValueError: 
        print ("Error, please enter numeric input")
