"""
Created by: Daniel Rubin

 Use Case 1:  User quits program
 The user types in the word “quit”.  The program terminates.
 If the command is not recognized, the Controller object prints out
 “unknown command”.
 sendCmd(argument)
 
"""

#Creates a class
class Observer:
    #Defines  _init_ and passes argument
    def __init__(self, name):
        self.name = name

    # Defines update and passes argument
    def update(self, message):
        #prints
        print('{} got message "{}"'.format(self.name, message))

#Creates a class
class controller:
    #Defines  _init_ and passes argument
    def __init__(self):
        knownCMD = ['cmd1', 'cmd2','cmd3']

    # Defines ParseInput and passes argument
    def ParseInput(self,inputSTR):
        # if do this 'conditional'
        if inputSTR == 'quit':
            controller.Quit(self)

    # Defines quit and passes argument
    def Quit(self):
        exit()

class txtState:
    #Defines  _init_ and passes argument
    def __init__(self):
        self.subscribers = set()


    #Defines validateinput and passes argument
    def validateinput(self, message):
        #print
        print('unknown command')

#sets the txt variable to the txtState()
txt = txtState()

#sets the inputTXT to variable to the input() passing the literal parameter of "Enter something: "
inputTXT = input("Enter something: ")

#utilizes conditionals
while inputTXT != "quit":
    txt.validateinput(inputTXT)
    # sets the inputTXT to variable to the input() passing the literal parameter of "Enter something: "
    inputTXT = input("Enter something: ")



