#CS-1 Task 2.2 - Exercise 5 from Steve Ding
looping = True
while looping:
    try:
        celsius = float(input('\nEnter the Celsius temperature: '))
        print ('Fahrenheit temperature is: ', (celsius*9/5+32))
        ans1 = input('\ncontinue? y/n\n')
        if ans1.upper() in ("NO", "N"):
            looping = False
    except ValueError: 
        print ("Man, learn to type a number.")
