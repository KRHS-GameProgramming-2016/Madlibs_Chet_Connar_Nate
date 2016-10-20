from input import *

#Written by Nathan
def story():
    location1 = getWord (" Enter a location: ")
    food1 = getWord (" Enter a food: ")
    adjective1 = getWord (" Enter a adjective: ")
    verb1 = getWord (" Enetr a verb: ")
    noun1 = getWord (" Enter a noun: ")
    
    
    text = ""
    text += " I went over to " + location1
    text += " and decided that I had a razy craving for " + food1
    text += ". While eating the " + adjective1
    text += " I decided to start " + verb1
    text += " the " + noun1
    text += ". "
    
    return text
    
