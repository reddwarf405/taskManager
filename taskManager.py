import pickle
import datetime
import waiting


class userTask():
   def __init__(self, name, freq):
      self.name = name
      self.freq = freq
      self.completed = False
   def taskMarked(self): # TODO: work out waiting for this   
    if self.freq == "hourly" and self.completed == True:
       if datetime.datetime.now().minute == 0:
          self.completed = False
    if self.freq == "daily" and self.completed == True:
        if datetime.datetime.now().hour == 0:
          self.completed = False
    if self.freq == "weekly" and self.completed == True:
       if datetime.datetime.weekday() == 0 and datetime.datetime.now().hour == 0:
          self.completed = False  
    if self.freq == "monthly" and self.completed == True:
       if datetime.datetime.now().day == 0 and datetime.datetime.now().hour == 0:
          self.completed = False
       


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
   taskFNum = input("Please select the frequency you wish for your task. You can do this by typing in a corresponding number for the frequency.\n1 Hourly\n2 Daily\n3 Weekly\n4 Monthly\nPlease type the number for the frequency you want for this task: ")
   taskFreq = ""
   while taskFreq == "":
    if taskFNum == "1":
      taskFreq = "hourly"
    elif taskFNum == "2":
      taskFreq = "daily"
    elif taskFNum == "1":
      taskFreq = "weekly"
    elif taskFNum == "1":
      taskFreq = "monthly"
    else:
       taskFNum = input("Please select the frequency you wish for your task. You can do this by typing in a corresponding number for the frequency.\n1 Hourly\n2 Daily\n3 Weekly\n4 Monthly\nPlease type the number for the frequency you want for this task: ")
   return userTask(taskName, taskFreq)


   


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
petName = input("Your pet looks so happy to meet you! Now, please give your pet a name: ")
userInfo["petName"] = petName
print("Great! You'll be able to change this name, if you want, at a later time. You can always type 'help' to find a list of commands you can use.") # TODO: Work out pet renaming
print("Now, start adding new tasks to your to-do list. You can add a new task at any time by typing 'newtask'.")
task1 = addNewTask() #TODO: figure out new task naming conventions and how that will work in code repeats






# TODO: Add help command
# TODO: create task objects and organization system as well as stat updates
# TODO: make sure saves actually work
# TODO: figure out date and time stuff
# TODO: work out reminders for tasks?