'''
DORIAN LAWTON

This code creates the blueprint for the rooms in "Skip to the Loo"

I certify that this code is mine, and mine alone, in accordance with
GVSU academic honesty policy.

11/15/24
'''
from item import Item
from npc import NPC


class Room:


   def __init__(self, desc, thing = None, npc = None):
       self.__desc = desc
       self.__thing = thing
       self.__npc = npc
       self.__neighbor = {}




   def get_item(self):
       return self.__thing


   def get_npc(self):
       return self.__npc


   def get_description(self):
       return self.__desc


   def set_item(self, thing):
       if isinstance(thing, Item) or thing is None:  # Ensure the input is an Item or None
           self.__thing = thing
       else:
           raise TypeError("thing must be an instance of Item or None")


   def set_npc(self, npc):
       if isinstance(npc, NPC) or npc is None:  # Allow NPC to be set to None
           self.__npc = npc
       else:
           raise TypeError("npc must be an instance of NPC or None")


   def set_description(self, desc):
       if isinstance(desc, str):  # Ensure the description is a string
           self.__desc = desc
       else:
           raise TypeError("desc must be a string")


   # Returns True if the room contains an item, otherwise False
   def has_item(self):
       return self.__thing is not None


   def has_npc(self):
       if self.__npc is not None:
           return True
       else:
           return False


   def add_neighbor(self, direction, room):
       self.__neighbor[direction] = room


   def get_neighbor(self, direction):
       return self.__neighbor.get(direction)


   # Removes the item from the Room and returns it. The item instance variable is set to None.
   def remove_item(self):
       if self.__thing is None:
           return None  # No item to remove
       item = self.__thing
       self.__thing = None
       return item


   def __str__(self):
       result = f"You are {self.__desc}\n"
       if self.__thing:
           result += f"\nYou see {self.__thing.get_description()}\n"
       if self.__npc:
           result += f"\nYou meet {self.__npc.get_name()}\n"
       return result
