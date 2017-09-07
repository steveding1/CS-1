#CS-1 Checkpoint 1 - Exercise 1 from Steve Ding
try:
    age = int(input("input the age: "))
    if age < 16:
        print("do not issue license: ")
    else:
        hours = int(input("input practice hours: "))
        if hours < 200:
            print("do not issue license: ")
        else:
            print("issue license: ")
except ValueError: 
    print ("Error, please enter numeric input")
