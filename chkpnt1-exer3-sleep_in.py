#CS-1 Checkpoint 1 - Exercise 3 - sleep in
weekdayflag = input("is it a weekday?(type true/false)")
vacationflag = input("is it a vacation?(type true/false)")

def sleep_in(weekday, vacation):
    if weekday == 'false':
        print ("True")
    else:
        if vacation == 'true':
            print ("True")
        else:
            print ("False")

sleep_in(weekdayflag,vacationflag)
