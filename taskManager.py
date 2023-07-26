import pickle


def initializeGame():
    global userInfo
    userInfo = {'petName' : '', 'petType' : '', 'petHunger' : 100, 'petEnjoy' : 100, 'petCleanliness' : 100}
    print("Welcome to my task management game! In this game you will keep a pet alive while completing tasks throughout your day. Type 'start' to get started. Type 'help' at any time to see more commands.")

def saveGame(playerInfo):
    with open('playerSave.pickle', 'wb') as handle:
        pickle.dump(playerInfo, handle)

def loadGame():
    with open('filename.pickle', 'rb') as handle:
     return pickle.load(handle)

def tryLoad():
   try: 
      loadGame()
   except:
      initializeGame()

def addNewTask(): # This will create an object for the task that displays the name, the frequency of the task, and whether or not it has been completed for the day.
   taskName = input("To add a new task, please enter the name of the task: ")

# def getHelp():
   










initializeGame()
animalChosen = False
while animalChosen == False:
    animalChoice = input("What type of animal would you like? You may choose: dog, cat, bird.\n")
    if animalChoice.lower() == "dog":
       print("Great! You have selected the dog. Here it is:\n")
       print("     __\n(___()'`;\n/,    /`\n\\\\\"--\\\\" + "\n")
       animalChosen = True
       userInfo["petType"] = "dog"
    if animalChoice.lower() == "cat":
       print("Great! You have selected the cat. Here it is:\n")
       print(" |\__/,|   (`\\\n |_ _  |.--.) )\n ( T   )     /\n(((^_(((/(((_/")
       animalChosen = True
       userInfo["petType"] = "cat"
    if animalChoice.lower() == "bird":
       print("Great! You have selected the bird. Here it is:\n")
       print("  , ___\n`\\/{o,o}\n / /)  )\n/,--\"-\"-")
       animalChosen = True
       userInfo["petType"] = "bird"




# TODO: Add help command
# TODO: create task objects and organization system as well as stat updates
# TODO: make sure saves actually work