from splash import *
from input import *
import story1
import story2
import story3
import story4
import story5

def madlibs():
    print splash()
    raw_input()
    end = False
    while not end:
        print menu()
        option = getMenuOption()
        if option == "q":
            end = True
        elif option == "1":
            print story1.story()
        elif option == "2":
            print story2.story()
        elif option == "3":
            print story3.story()]
        elif option == "4":
            print story4.story()
        elif option == "5":
            print story5.story()
            raw_input()
    print "Good Bye!"
    

    
madlibs()
