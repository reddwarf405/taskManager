import pickle
import datetime
from threading import Timer
import random

class userTask():
   def __init__(self, name, freq):
      self.name = name
      self.freq = freq
      self.completed = False

   def __str__(self): # For displaytask, shows the user what their tasks are like
      if self.completed == False:
        return self.name + ", " + self.freq + ", not completed."
      elif self.completed == True:
         return self.name + ", " + self.freq + ", completed."

   def taskMarked(self): # Changes the completion status of a task after the clock rolls over.
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

       


def initializeGame(): # Creates the game with some global variables defining the player's settings
    global userInfo
    userInfo = {'petName' : '', 'petType' : '', 'petHunger' : 100, 'petEnjoy' : 100, 'petCleanliness' : 100}
    global taskList
    taskList = []
    print("Welcome to my task management game! In this game you will keep a pet alive while completing tasks throughout your day.")

def saveGame(playerInfo, tasks): # Saves the game with the players info and their tasks
    with open('playerSave.pickle', 'wb') as handle:
        pickle.dump(playerInfo, handle, -1)
        pickle.dump(tasks, handle, -1)

def loadGame(): # Loads the last saved game
    global gameExists
    gameExists = True
    with open('filename.pickle', 'rb') as handle:
     return pickle.load(handle)

def tryLoad(): # Attempts to load the game, upon failure, starts a new one
   
   try: 
      loadGame()
   except:
      global gameExists
      gameExists = False
      initializeGame()

def addNewTask(): # This will create an object for the task that displays the name, the frequency of the task, and whether or not it has been completed for the day.
   taskName = input("To add a new task, please enter the name of the task: ")
   taskFNum = input("Please select the frequency you wish for your task. You can do this by typing in a corresponding number for the frequency.\n1 Hourly\n2 Daily\n3 Weekly\n4 Monthly\nPlease type the number for the frequency you want for this task: ")
   taskFreq = ""
   while taskFreq == "": # Prompts the player until they put in a valid number
    if taskFNum == "1":
      taskFreq = "hourly"
    elif taskFNum == "2":
      taskFreq = "daily"
    elif taskFNum == "3":
      taskFreq = "weekly"
    elif taskFNum == "4":
      taskFreq = "monthly"
    else:
       taskFNum = input("Please select the frequency you wish for your task. You can do this by typing in a corresponding number for the frequency.\n1 Hourly\n2 Daily\n3 Weekly\n4 Monthly\nPlease type the number for the frequency you want for this task: ")
   return userTask(taskName, taskFreq) # Returns these attributes to be placed in a task object

def displayPet(): # Shows the user their animal!
   if userInfo["petType"] == "dog":
      print(userInfo["petName"] + "\n     __\n(___()'`;\n/,    /`\n\\\\\"--\\\\" + "\n")
   elif userInfo["petType"] == "cat":
      print(userInfo["petName"] + "\n |\__/,|   (`\\\n |_ _  |.--.) )\n ( T   )     /\n(((^_(((/(((_/")
   elif userInfo["petType"] == "bird":
      print(userInfo["petName"] + "\n  , ___\n`\\/{o,o}\n / /)  )\n/,--\"-\"-")

def displayStats():
   print("Hunger: " + str(userInfo["petHunger"]) + "\nEnjoyment: " + str(userInfo["petEnjoy"]) + "\nCleanliness: " + str(userInfo["petCleanliness"]))

def getHelp(): # Displays commands the player can use and credits
   print("Type 'newtask' to create a new task.\nType 'rename' to rename your pet.\nType 'save' to save your game.\nType 'tasks' to see your current tasks and their statuses.\n")
   print("All ASCII art credit to its original creators.")
   
def displayTasks(inputList): # Shows the player the tasks they have registered
   for each in inputList:
      print(each.__str__() + "\n")

def decreaseStat():
   selectedStat = random.randint(2, 5)
   userInfo[selectedStat] -= 1





tryLoad() # Start of the game, attempts to load
t = Timer(600, decreaseStat)
t.start()

if gameExists == False: # If a saved game does not exist, the player goes through the start of the game
   animalChosen = False
   while animalChosen == False: # While the player has not entered a valid choice
    animalChoice = input("What type of animal would you like? You may choose: dog, cat, bird.\n")
    if animalChoice.lower() == "dog":
       print("Great! You have selected the dog. Here it is:\n")
       print("     __\n(___()'`;\n/,    /`\n\\\\\"--\\\\" + "\n")
       animalChosen = True
       userInfo["petType"] = "dog"
    elif animalChoice.lower() == "cat":
       print("Great! You have selected the cat. Here it is:\n")
       print(" |\__/,|   (`\\\n |_ _  |.--.) )\n ( T   )     /\n(((^_(((/(((_/")
       animalChosen = True
       userInfo["petType"] = "cat"
    elif animalChoice.lower() == "bird":
       print("Great! You have selected the bird. Here it is:\n")
       print("  , ___\n`\\/{o,o}\n / /)  )\n/,--\"-\"-")
       animalChosen = True
       userInfo["petType"] = "bird"

   petName = input("Your pet looks so happy to meet you! Now, please give your pet a name: ") # Player names their pet
   userInfo["petName"] = petName

   print("Great! You'll be able to change this name, if you want, at a later time. You can always type 'help' to find a list of commands you can use.") # TODO: Work out pet renaming
   print("Now, start adding new tasks to your to-do list. You can add a new task at any time by typing 'newtask'. You may currently add up to five tasks.")
   
   #Executes adding a new task and placing that task in the taskList
   newTask = addNewTask()
   taskList.append(newTask)

   print("Great! Now, type 'tasks'. You can type this at any time to see your tasks and whether or not they've been completed.") # Player sees their list of tasks
   userInput = input(">")
   if userInput.lower() == "tasks":
    displayTasks(taskList)

   print("Wonderful. When you've completed a task, type in 'complete' to register which one you've completed. Completing tasks updates your pet's stats and keeps it happy and healthy.") # TODO: work out task completion
   print("You've completed the tutorial! I hope you enjoy managing your tasks for a more productive and happy life. :) \nYou may quit the program at any time, but make sure you type 'save' first to save your progress.")



while True: 
   displayPet()
   displayStats()
   userInput = input("> ")

   if userInput == "save":
      saveGame(userInfo, taskList)
      print("Saved game.")
   
   elif userInput == "newtask":
      newTask = addNewTask()
      taskList.append(newTask)

   elif userInput == "tasks":
      displayTasks(taskList)
   
   elif userInput == "complete":
      count = 1
      for each in taskList:
         print(str(count) + each.__str__ + "\n")
         count += 1
      userChoice = input("Please type the number of the task you would like to mark as complete.")
      userChoice -= 1
      taskList[userChoice].completed = True
      selectedStat = random.randint(2, 5)
      if taskList[userChoice].freq == "hourly":
         userInfo[selectedStat] += 8
      elif taskList[userChoice].freq == "daily":
         userInfo[selectedStat] += 20
      elif taskList[userChoice].freq == "weekly":
         userInfo[selectedStat] += 50
      elif taskList[userChoice].freq == "daily":
         userInfo[selectedStat] = 100