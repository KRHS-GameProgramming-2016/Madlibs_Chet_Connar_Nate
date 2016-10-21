from input import *

#Written by Nathan
def story():
    location1 = getWord (" Enter a location: ")
    food1 = getWord (" Enter a food: ")
    adjective1 = getWord (" Enter a adjective: ")
    verb1 = getWord (" Enter a verb: ")
    noun1 = getWord (" Enter a noun: ")
    opponent1 = getWord (" Enter an opponent (who has arms): ")
    adjective2 = getWord (" Enter a second adjective: ")
    bodyofwater1 = getWord (" Enter a body of water: ")
    food2 = getWord (" Enter a second food item: ")
    location2 = getWord (" Enter a second location: ")
    
    
    text = ""
    text += " I went over to " + location1
    text += " and decided that I had a crazy craving for " + food1
    text += ". While eating the " + adjective1
    text += " I decided to start " + verb1
    text += " the " + noun1
    text += ". After I got bored doing that thing, I headed on over to the " + location2
    text += " to start lifting weights and stuff. "
    text += "After I beat " + opponent1
    text += " at arm wrestling I started to look " + adjective2
    text += " at the " + bodyofwater1
    text += " I wondered how in the world I didnt have any " + food2
    text += " left."
    
    return text
    
