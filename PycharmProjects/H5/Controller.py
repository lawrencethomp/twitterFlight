

class Controller:
    msg = ''
    def inputmessage():
        global msg
        msg = input("What is your command? ")
        if msg == 'register observers':
            print('sounds demanding but ok')
        if msg == 'quit':
            print('process is kill')
        if msg == 'status':
            print('we do the status')
        if msg == 'unregister':
            print('messages are unregistered')
        if msg == 'send':
            print('i think we need regExp for this')


# Find something with text entry for Python

'''
 Use Case 1:  User quits program

 The user types in the word “quit”.  The program terminates.
 If the command is not recognized, the Controller object prints out
 “unknown command”.

 sendCmd(argument)

'''

'''

THE JAVA CODE:
    Controller C = new Controller();
    While (!c.terminate())
    {
        input = readln();
        c.parseInput(input);
    }
    

'''


# Find a way to terminate a program

# Create an unknown command

# Use Case 2: User Registers Observers

#   User types in “status”. Each of the three observers of the TextState
#   object return whether they are listening for TextState notifications or
#   not. as per User registers observers, maybe it should have observerList[]
