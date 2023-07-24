import pickle

def initializeGame():
    userInfo = {'petName' : '', 'petType' : '', 'petHunger' : 100, 'petEnjoy' : 100, 'petCleanliness' : 100}
    print("Welcome to my task management game! In this game you will keep a pet alive while completing tasks throughout your day. Type 'start' to get started. Type 'help' at any time to see more commands.")
    print("What type of animal would you like? You may choose: dog, cat, bird.")

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

# def getHelp():
   










initializeGame()

# TODO: Add help command
# TODO: create ASCII art for animals
# TODO: make sure saves actually work