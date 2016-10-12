from input import *

#Written by Nathan, Chett, and Connar
def story():
    location1 = getWord("Enter a location: ")
    temperature1 = getNumber("Enter a Number: ")
    food1 = getWord ("enter food" )
    pokemon1 =getWord("enter a pokemon")
    text = ""
    text += "One day I went to the " + location1
    text += ". It was like " + temperature1
    text += " outside."    
    text +=" Then suddenly, a " + pokemon1
    text +=" appeared! " 
    text +=""
    
    return text
    
