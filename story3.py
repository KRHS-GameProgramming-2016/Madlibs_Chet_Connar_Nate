from input import *

#Written by Connor
def story():
    noun1 = getWord (" Enter a Noun: ")
    myName = getWord (" Enter a Name: ")
    game1 = getWord (" Enter a Game Name: ")
    friendname1 = getWord (" Enter a Name: ")
    classname = getClass (" Enter a titanfall class (Oger, Atlas, or Strider): ")
    number1 = getNumber (" Enter a number: ")
    
    text =""
    text += " I am a " + noun1 
    text += ".  one day I play " + game1
    text += " with my friend, " + friendname1
    text += " who killed me. I then re-spawned and killed " + friendname1
    text += " I then left the game to go play some titanfall.  I play as a " + classname
    text += ". I have a " + number1
    text += " to 1 k/d ration. "
    
    return text
  
