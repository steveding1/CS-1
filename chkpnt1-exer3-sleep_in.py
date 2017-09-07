#CS-1 Checkpoint 1 - Exercise 3 - sleep in
try:
    def sleep_in(weekday, vacation):
        if weekday is False:
            print ("True")
        else:
            if vacation is True:
                print ("True")
            else:
                print ("False")
except NameError:
    print ("Error, please enter true or false")
