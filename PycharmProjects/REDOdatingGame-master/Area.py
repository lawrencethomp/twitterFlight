"""
The Room class uses the names of the rooms as a common link for locations and interaction objects.
Interaction Objects - People, Items, Events.
It is helpful because rooms have people in them.


We have created the rooms, the rooms go into a map.

We need to switch change locations to be the map.

"""

import Player
import DataMaster
import person
import setpiece

class Room:
    """
    constructor for a room - the common link with most items in the game insofar as interactivity.
    rooms will later get descriptions added on to them as well.
    """
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def describeme(self):
        print("You are in the " + self.name + " which is known as " + self.desc + ".")

    def describeit(self):
        return (self.describeme(), "it works")

    def presentItems(self):
        return ("Bro you can win")


class Plains(Room):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class Bar(Room):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


ThePlace = Room("plains", "It's the plains")
wayward_souls = Room("bar", "to alcohol. the cause and solution to all of lifes problems")
theVillage = Room('village', 'the village')
#townSquare

def singleLine(list):
    for item in list:
        print(item, end=" ")

def worldBuilder():
    """
    Linked to the check function. When the player checks the location that they are in, they are given a bit of information about what can be checked.
    :return: a string with all the things linked to a location.

    Changed to reflect the items type.
    Person. You also noticed that " " were around
    Setpiece. You saw the
    """
    # build an array to see what is there
    locationArray = []
    localString = ""
    personString = ""

    for synonymList in DataMaster.DataMaster.object_synonyms:
        for obj in synonymList:
            if obj.location == Player.player.location:
                if type(obj) == person.Person:
                    personString+=str(obj.formattedName + ", ")
                if type(obj) == setpiece.SetPiece:
                    localString+=str(obj.formattedname + ", ")
                    # locationArray.append(obj)
                    # localString+=str(obj.name + ", ")
    # build the string with the things. Iterate

    print("Looking around the " + Player.player.location + ", you noticed that " + personString + "were all in the area. You also noticed that " + localString + "were around too.")
    #print("In the " + Player.player.location + ", you saw " + localString)
'setpiece.SetPiece'
'__main__.Person'


worldBuilder()
    # return the names to the player.

def locationLoader():
    """
    loads the objects in the location into their respective spots so the player is able to easily access array's. Objects will be loaded according to type. This is to save resources.
    :return:
    """
    # explores the objects

    # pushes to an array

    # iterates through an array

class Map:
    """
    consults the roomArray so that we can change rooms and have interactivity.
    """
    roomArray = [ThePlace, wayward_souls, theVillage]
    location_synonym = [wayward_souls.name, ThePlace.name]
    def change_room(request):
        for room in Map.roomArray:
            if Player.player.location in request:
                print("you are already there")
                break
            if room.name in request:
                print(Player.player.location)
                Player.player.location = room.name
                print("TEST: you are now in " + room.name + " which should be the " + Player.player.location)

#
# def locationVerifier(arugment):
#     """
#     Verification to ensure that players are in the same area as their things.
#     :param arugment:
#     :return:
#     """
#     print(arugment)
#     print(Player.player.location)
#     if arugment == Player.player.location:
#         return True
#     else:
#         print("You are not in the same area.")


class Description:
    def __init__(self , desc):
        self.desc = desc

    def describeit(self):
        return (self.describeme(), "it works")

    def presentItems(self):
        return ("Bro you can win")



#Map.change_room("bar")
