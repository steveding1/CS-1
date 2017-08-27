#CS-1 Task 2.2 - Exercise 3 from Steve Ding
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    print ('Pay: ', round(hours*rate,2))
except ValueError: 
    print ("Man, learn to type a number.")