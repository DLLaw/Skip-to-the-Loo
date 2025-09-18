'''
DORIAN LAWTON

This code creates the blueprint for the items in "Skip to the Loo"

I certify that this code is mine, and mine alone, in accordance with
GVSU academic honesty policy.

11/15/24
'''

class Item:
    
    # Initalizes the Item class
    def __init__(self, name, description, weight):
        self.__name = name
        self.__description = description
        self.__weight = weight

    # GETTERS

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_weight(self):
        return self.__weight
    
    # SETTERS
    
    def set_name(self, name):
        self.__name = name

    def set_weight(self, weight):
        self.__weight = weight

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return self.__description
