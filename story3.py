from input import *

#Written by Connor
def story():
    noun1 = getWord (" Enter a Noun: ")
    myName = getWord (" Enter a Name: ")
    game1 = getWord (" Enter a Game Name: ")
    friendname1 = getWord (" Enter a Name: ")
    classname = getClass (" Enter a titanfall class (Oger, Atlas, or Strider): ")
    
    text =""
    text += " I am a " + noun1 
    text += ".  one day play" + game1
    text += " with my frined, " + friendname1
    text += " and i dead. I the ne-spawned and killed " + friendname1
    text += " I left the game to go play titanfall.  i paly as a " + classname
       
    
    return text
  
