def isSwear(word):
    swearList = ["poop",
                 "pee",
                 "peepee",
                 "meme",
                 "penis",
                 "hillary",
                 "hilarry",
                 "trump",
                 "shit",
                 "Chink",
                 "Damn",
                 "fag",
                 "faggot",
                 "gay",
                 "hell",
                 "Math",
                 "PS4",
                 "PS 4",
                 "PS",
                 "PlayStation",
                 "Harambe",
                 "Cecil",
                 "Cecil the lion",
                 "Douchebag",
                 "Ass",
                 "Fuck",
                 "Dick",
                 "Dik",
                 "Dic",
                 "Vagina",
                 "Dingus",
                 "John",
                 "African american",
                 "african americun",
                 "africa amurican",
                 "africa",
                 "Africa",
                 "Ken Bone",
                 "bone",
                 
                 
                 
                 
                 ]
    if word in swearList:
        return True
    else:
        return False

def getMenuOption():
    goodInput = False
    goodResponses = ["1",
                     "2",
                     "3",
                     "q"]
    while not goodInput:
        response = raw_input(" Make a selection: ")
        if response.lower() in goodResponses:
            goodInput = True
        else:
            print " Please make a valid selection! "
    return response.lower()

def getWord(prompt):
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        if isSwear(response):
            goodInput = False
            print " Don't use that kind of language with me! "
    return response

def getNumber(prompt):
    goodInput = False
    numbers = "0123456789."
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        for character in response:
            if character not in numbers:
                goodInput = False
                print " Numbers only please! "
    return response
        
        



















