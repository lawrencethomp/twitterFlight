"""
Created by: Daniel Rubin
Use Case 4: User unregisters observers.
User types in “unregister”.  All observers of the TextState object unregister themselves.

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
class Observiable:
    #Defines  _init_ and passes argument
    def __init__(self):
        self.subscribers = set()
        self.unsubscribers = set()

    # Defines register and passes argument
    def register(self, who):
        self.subscribers.add(who)
        self.unsubscribers.discard(who)

    # Defines unregister and passes argument
    def unregister(self, who):
        self.subscribers.discard(who)
        self.unsubscribers.add(who)

    # Defines registeredNotification and passes argument
    def registeredNotification(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

    # Defines unregisteredNotification and passes argument
    def unregisteredNotification(self, message):
        #initializes a for loop and a local variable
        for subscriber in self.unsubscribers:
            subscriber.update(message)

#sets the variables to the following
pub = Observiable()
usr1 = Observer("Usr 1")
usr2 = Observer("Usr 2")
usr3 = Observer("Usr 3")
inputTXT = ""

#utilizes conditionals
while inputTXT != "quit":
    inputTXT = input("Enter something: ")
    #if do this
    if inputTXT == 'register observers':
        #registers the user that is passed in the argument
        pub.register(usr1)
        pub.register(usr2)
        pub.register(usr3)
    #elif do this etc...
    elif inputTXT == 'unreg1':
        # unregisters the user that is passed in the argument
        pub.unregister(usr1)
    elif inputTXT == 'uureg2':
        # unregisters the user that is passed in the argument
        pub.unregister(usr2)
    elif inputTXT == 'unreg3':
        # unregisters the user that is passed in the argument
        pub.unregister(usr3)
    elif inputTXT == 'unregister':
        # unregisters the user that is passed in the argument
        pub.unregister(usr1)
        pub.unregister(usr2)
        pub.unregister(usr3)
    #else do this
    else:
        inputTXT == 'status'
        #sets the registered notification as a leteral "Registered"
        pub.registeredNotification("Registered")
        #sets the registered notification as a leteral "Not registered for notifications"
        pub.unregisteredNotification("Not registered for notifications")



