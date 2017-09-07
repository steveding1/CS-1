#CS-1 Checkpoint 1 - Exercise 1 - simulating driver's license provision
import sys
try:
    age = int(input("input the age: "))
except ValueError: 
    print ("Error, please enter numeric input")
    age = 0
    sys.exit()

if age < 16:
    print("do not issue license: ")
else:
    hours = int(input("input practice hours: "))
    if hours < 200:
        print("do not issue license: ")
    else:
        print("issue license: ")
