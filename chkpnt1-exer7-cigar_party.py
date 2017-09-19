#! python3
#CS-1 Checkpoint 1 - Exercise 7 - cigar_party
def cigar_party(cigars,weekend):
    import sys
    try:
        cigars1 = int(cigars)
        if weekend == "True":
            weekend1 = True
        elif weekend == "False":
            weekend1 = False
        else:
            print ("Error, please enter an interger and True/False")
            sys.exit()
        if (cigars1>=40 and cigars1<=60 or weekend1):
            print("True")
        else:
            print("False")
    except NameError: 
        print ("Error, please enter an interger and True/False")
        sys.exit()

cigars_flag=input("input the number of cigars ")
weekend_flag=input("is today weekend?(True or False)")
cigar_party(cigars_flag,weekend_flag)
