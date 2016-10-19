from input import *

#Written by Nathan
def story():
    location1 = getWord(" Enter a location: ")
    temperature1 = getNumber(" Enter a Number: ")
    food1 = getWord (" enter food: " )
    pokemon1 =getWord(" enter a pokemon: ")
    adjective1 =getWord (" enter a adjective: ")
    adjective2 = getWord (" enter a seond adjective: ")
    mammal1 = getWord (" enter a mammal: ")
    difficulty1 = getWord (" enter a difficulty: ")
    allpowerfulbeing1 = getWord (" Enter an all powerful being: ")
    text = ""
    text += "One day I went to " + location1
    text += ". It was like " + temperature1
    text += " outside."    
    text +=" Then suddenly, a wild " + pokemon1
    text +=" appeared! " 
    text +="While the " + pokemon1
    text+= " ate all of the " + food1
    text +=" we all watched it wondering how it got here."
    text +=" While the pokemon ate the " + food1
    text += " we continued doing normal things." 
    text += " These things where very " + adjective1
    text += ". While we continue this " + adjective2
    text += " story, some " + mammal1
    text += "'s might actually think, why continue?"
    tet += " The answer to that is so " + difficulty1
    text += " that they wonder why they even bothered wondering."
    text += " While thats happening the " + allpowerfulbeing1
    text += " was busy doing his thing."
    text += " Destroying planets if they felt like it."
    
    return text
    
