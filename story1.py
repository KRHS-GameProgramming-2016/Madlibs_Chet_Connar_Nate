from input import *

#Written by Mr. Spooner
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getNumber("Enter a Number: ")
    food1 = getword ("enter food" )
    
    text = ""
    text += "One day I went to the " + location1
    text += ". It was like " + temperature1
    text += " degrees  out."    
    text += " I know lets go and eat some " + food1
    text+= "!"
    return text
