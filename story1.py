from input import *

#Written by Nathan, Chett, and 
def story():
    location1 = getWord(" Enter a location: ")
    temperature1 = getNumber(" Enter a Number: ")
    food1 = getWord (" enter food " )
    pokemon1 =getWord(" enter a pokemon ")
    text = ""
    text += "One day I went to " + location1
    text += ". It was like " + temperature1
    text += " outside."    
    text +=" Then suddenly, a wild " + pokemon1
    text +=" appeared! " 
    text +="While the " + pokemon1
    text+= " ate all of the " + food1
    text +=" We all watched it wondering how it got here."
    text +=" While the pokemon ate the " + pokemon1
    text += "food we continued doing normal things." 
    
    return text
    
