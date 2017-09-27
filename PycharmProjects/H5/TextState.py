import Controller
import Observer
import Main


######## Use Case 2: User registers observers #######
# User typed in “register observers” into Controller.py.



# This will cause all 3 observers of the TextState class to register
# for notifications of the TextState object.



# Each observer will print out that it is waiting for
    # TextState notifications.



# When registered in this way, all counts inside the
# observers will be reset to their
# starting values.

class TextState:
    observerList = []
    msg = Controller.Controller.inputmessage()
    def notifyobserver():
        if msg == 'ok':
            print('cool')

    # status = 0

    # if status == 0:
        # name 'not registered for notifications.'
    # if status == 1:
        # name 'registered for notifications.'





