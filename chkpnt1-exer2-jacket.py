#CS-1 Checkpoint 1 - Exercise 2 - bring different jacket
import sys
try:
    temp = int(input("input the today's temperature: "))
except ValueError: 
    print ("Error, please enter numeric input")
    sys.exit()

if temp < 20:
    print("bring heavy jacket")
elif temp <=30:
    print("bring light jacket")
else:
    print("no need any jacket.")
