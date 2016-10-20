from input import *

#Written by Nathan
def story():
    location1 = getWord(" Enter a location: ")
    temperature1 = getNumber(" Enter a Number: ")
    food1 = getWord (" enter food: " )
    pokemon1 =getWord(" enter a pokemon: ")
    adjective1 =getWord (" enter a adjective: ")
    adjective2 = getWord (" enter a second adjective: ")
    mammal1 = getWord (" enter a mammal: ")
    difficulty1 = getWord (" Easy or Hard: ")
    allpowerfulbeing1 = getWord (" Enter an all powerful being: ")
    food2 = getWord (" Enter a second food: ")
    text = ""
    text += "One day I went to " + location1
    text += ". It was like " + temperature1
    text += " outside."    
    text +=" Then suddenly, a wild " + pokemon1
    text +=" appeared! " 
    text +="While the " + pokemon1
    text += " ate all of the " + food1
    text +=" we all watched it wondering how it got here."
    text +=" While the pokemon ate the " + food1
    text += " we continued doing normal things." 
    text += " These things where very " + adjective1
    text += ". While we continue this " + adjective2
    text += " story, some " + mammal1
    text += "'s might actually think, why continue?"
    text += " The answer to that is so " + difficulty1
    text += " to understand that they wonder why they even bothered wondering."
    text += " While thats happening the " + allpowerfulbeing1
    text += " was busy doing his thing."
    text += " Destroying planets if it felt like it."
    text += " also eating " + food2
    text += " because they happened to enjoy the taste. "
    text += "
    
    return text
    
