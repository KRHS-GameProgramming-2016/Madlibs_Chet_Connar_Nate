from input import *

#Written by connar dunn
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getNumber("Enter a Number: ")
    food1 = getword ("enter food" )
    
    text = ""
    text += "One day I went to the " + location1
    text += ". It was like " + temperature1
    text += " outside."    
    text +=" " 
    text +=" " 
    
    return text
    
