from input import *

#Written by Nathan
def story():
    noun1 = getWord (" Enter a Noun: ")
    emotion1 = getWord (" Enter a emotion: ")
    emotion2 = getWord (" Enter a second emotion: ")
    noun2 = getWord (" Enter a second noun: ")
    gender1 = getWord (" Enter man or women: ")
    noun3 = getWord (" Enter a third noun: ")
    
    text =""
    text += " I am a " + noun1
    text += ". You wouldnt think a " + noun1
    text += " could be lonely. "
    text += "I can also be " + emotion1
    text += " but we arent going to talk about that. "
    text += "Every once in a while a " + noun2
    text += " came along to make sure I was " + emotion2
    text += ". " + noun2
    text += " was doing good but sometimes didnt do good and I was not very " + emotion2
    text += ". While that happened, in a " + noun3
    text += " far far away in a place we dont really understand. "
    text += "there was nothing, because those kinds of things do not exist. get real " + gender1
    text += ". "
    return text
