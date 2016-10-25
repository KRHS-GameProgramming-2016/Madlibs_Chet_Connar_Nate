from input import *

#Written by 
def story():
    noun1 = getWord (" Enter a Noun: ")
    emotion1 = getWord (" Enter a emotion: ")
    emotion2 = getWord (" Enter a second emotion: ")
    noun2 = getWord (" EEnter a second noun: ")
    
    text =""
    text += " I am a " + noun1
    text += ". You wouldnt think a " + noun1
    text += " could be lonely. "
    text += "I can also be " + emotion1
    text += " but we arent going to talk about that. "
    text += "Every once in a while a " + noun2
    text += " came along to make sure I was " + emotion2
    text += ". " + noun2
    text += " was doing good but sometimes didnt do good and I was very " + emotion2
    text += ". While that happened in a " + noun3
    text += " far far away in a place we dont really understand. "
    text += ""
    return text
