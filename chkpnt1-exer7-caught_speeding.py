#! python3
#CS-1 Checkpoint 1 - Exercise 7 - cigar_party
import sys
def cigar_party(cigars,weekend):
    try:
        cigars1 = int(cigars)
        if (cigars1>=40 and cigars1<=60 or weekend):
            return True
        else:
            return False
    except NameError: 
        print ("Error, please enter an interger and True/False")
        sys.exit()
