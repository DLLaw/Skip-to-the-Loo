'''
DORIAN LAWTON

This is a code that creates, customizes, and initializes my game "Skip to the Loo" which is a text based game of quest where you are in a mall in chicago
and must find a bathroom before you crap yourself.

I certify that this code is mine, and mine alone, in accordance with
GVSU academic honesty policy.

12/3/2024
'''


import random
import sys
from room import Room
from item import Item
from npc import NPC


class Game:
  def __init__(self):
      self.__previousRoom = None  # Tracks the last visited room for retreat functionality
      self.__inventory = []  # List of items the player is holding
      self.__message = ""  # Message to display to the player
      self.__game_won = False  # Tracks if the game has been won
      self.__moves_remaining = 8  # Number of moves the player has to win
      self.create_world()
      self.__game_lost = False

  # Sets up the game world, including rooms, items, and NPCs
  def create_world(self):

      # Define items
      mutz = Item("Mutz", "mutz, a helpful antacid that gives the user an extra two moves", 2)
      ghoul = Item("Ghoul", "a can of Ghoul (energy drink) covered in fuzz and dust under a bench . It may help energize you, but it looks pretty nasty", 2)
      bathroom_key = Item("Bathroom Key", "the key to the bathroom. Take it and you win!!", 5)
      candy = Item("Unlimited Candy", "unlimited amounts of candy all around you in the candy store", 100000)

      # Define NPCs
      baul_plart = NPC(
          "Baul Plart Mall Cop",
          [
              "Your eyes are turning brown! I thought you were an intruder, but you must be looking for the key. Good luck!",
              "Hey! No running! Need the bathroom key? I'm not sure where it is, but I feel like I saw it earlier...",
              "That room is locked for a reason! You shouldn't be in here. Looking for the key? Oh, alright then."
          ])

      reginald_billingsly = NPC(
          "Reginald Billingsly",
          [
              "Oh dear, what a mess! Avoid the wet floors, they're slippery!",
              "Need the loo? I hope you can find the key!",
              "Careful! The tile is slippery. I just cleaned it, so don't get it all dirty!"
          ])

      # Define rooms
      self.__mall = Room("standing in the main part of the mall. there are several stores to your east\nand west, and to the north, at the end of the hallway, is the bathroom!!")
      self.__canadian_eagle = Room("in Canadian Eagle,  a bright, rustic store known for selling jeans.")
      self.__match_stop = Room("in Match Stop, an electronics store that specializes in video games. The air hums with the sounds of consoles running.")
      self.__cold_topic = Room("in Cold Topic, a dimly lit store with dark walls, lined with edgy band tee shirts, hoodies, and grunge accessories. Loud music is blaring overhead which is not helping you concentrate on holding your bowels.")
      self.__arcade = Room("in a run-down arcade with all of the classics. There's a security guard wandering around somewhere...")
      self.__lululime = Room("in Lululime, a store with a sporty, high-quality feel. You are surrounded by items that cost way too much, but it’s worth looking for something you may need.")
      self.__candy_shop = Room("in The Candy Shop, a wonderland filled with sweet treats. The key may be in here, but the bright colors and sweet smells are very distracting, as well as 50 Cent's 'Candy Shop' blaring over the speakers. Luckily, you have some more pressing matters to attend to, or else you would be stuck in here forever.")
      self.__shoe_circus = Room("in Shoe Circus, a store completely filled with shoes. The store puts on a small circus in the center of the room for the customers to watch while they shop. The air smells of popcorn and cotton candy, but you have an important task at hand. Find the key!!.")
      self.__theater = Room("in a theater that has played the movie Chicken Little 24/7 since 2005. You smell Popcorn in a dark-themed lobby with planet designs on black carpet.")
      #
      self.__mall.set_item(ghoul)


      # Connect rooms based on the map

      # WEST SIDE OF THE MALL
      self.__mall.add_neighbor("west", self.__canadian_eagle)
      self.__canadian_eagle.add_neighbor("east", self.__mall)
      self.__canadian_eagle.add_neighbor("north", self.__cold_topic)
      self.__cold_topic.add_neighbor("south", self.__canadian_eagle)
      self.__cold_topic.add_neighbor("north", self.__lululime)
      self.__cold_topic.add_neighbor("east", self.__mall)
      self.__lululime.add_neighbor("south", self.__cold_topic)
      self.__lululime.add_neighbor("east", self.__mall)
      self.__lululime.add_neighbor("north", self.__shoe_circus)
      self.__shoe_circus.add_neighbor("south", self.__lululime)
      self.__shoe_circus.add_neighbor("east", self.__mall)

      # EAST SIDE OF THE MALL
      self.__mall.add_neighbor("east", self.__match_stop)
      self.__match_stop.add_neighbor("west", self.__mall)
      self.__match_stop.add_neighbor("north", self.__arcade)
      self.__arcade.add_neighbor("south", self.__match_stop)
      self.__arcade.add_neighbor("west", self.__mall)
      self.__arcade.add_neighbor("north", self.__candy_shop)
      self.__candy_shop.add_neighbor("south", self.__arcade)
      self.__candy_shop.add_neighbor("west", self.__mall)
      self.__candy_shop.add_neighbor("north", self.__theater)
      self.__theater.add_neighbor("south", self.__candy_shop)
      self.__theater.add_neighbor("west", self.__mall)


      # Randomly assign the Bathroom Key to a room
      valid_rooms = [
          self.__canadian_eagle, self.__match_stop, self.__cold_topic, self.__arcade,
          self.__lululime, self.__candy_shop, self.__shoe_circus, self.__theater
      ]

      self.__key_room = random.choice(valid_rooms)
      if self.__key_room is not None:  # Ensure the selected room is not None
          self.__key_room.set_item(bathroom_key)

      if self.__key_room != self.__match_stop:
          self.__match_stop.set_item(ghoul)
      if self.__key_room != self.__lululime:
          self.__lululime.set_item(mutz)
      if self.__key_room != self.__candy_shop:
          self.__candy_shop.set_item(candy)
      if self.__key_room != self.__cold_topic:
          self.__cold_topic.set_item(ghoul)
      if self.__key_room != self.__shoe_circus:
          self.__shoe_circus.set_item(candy)
      if self.__key_room != self.__canadian_eagle:
          self.__canadian_eagle.set_item(mutz)
      if self.__key_room  != self.__arcade:
          self.__arcade.set_item(candy)

      # Set NPCs in rooms
      self.__arcade.set_npc(baul_plart)
      self.__mall.set_npc(reginald_billingsly)

      # Set the starting room
      self.__currentRoom = self.__mall

  # Return the current room the player is in.
  def get_current_room(self):
      return self.__currentRoom

  # Main game loop
  def play(self):
      self.set_welcome_message()
      print(self.get_message())
      self.__moves_remaining = 8

      while not self.game_over():
          print(f"Moves remaining: {self.__moves_remaining}")
          command = input("Enter >>> ").strip()
          first, second = self.parse_command(command)

          # Handle user commands
          if first == "quit":
              print("Thanks for playing!")
              break
          elif first == "move":
              self.move(second)
          elif first == "look":
              self.look()
          elif first == "take":
              self.take()
          elif first == "place":
              self.place(second)
          elif first == "speak":
              self.speak()
          elif first == "consume":
              self.consume(second)
          elif first == "retreat":
              self.retreat()
          elif first == "auto_win":
              self.auto_win()
          elif first == 'help':
              self.help()
          elif first == 'items':
              self.items()
          elif first == 'fortnite':
              self.auto_win()
          else:
              self.__message = "Invalid command."

          print(self.get_message())

          # Check for game-winning condition
          if self.__game_won:  # Ensures the winning message only prints once
              break

          # Check for game-losing condition
          if self.__moves_remaining <= 0:
              self.__game_lost = True
              self.print_losing_message()
              break

  # Sets the initial game message
  def set_welcome_message(self):
      self.__message = "=== Welcome to Skip to the Loo!! ===\n\n=== Last night, you ate the best giant wet burrito ever. Now you’re wandering a mall in Chicago, and the after-effects start to hit your stomach. ===\n=== “Skip to the Loo” is a game of quest where you are lost in a mall in Chicago, and you must find the key to the public bathroom in time or else you will fill your britches. ===\n=== To win, you must find the right room to get a key to the bathroom, and you have 8 turns (Entering and exiting rooms is a turn, but retreating is not) to make it. ===\n=== If you lose, you get sent to haunt a waste management facility for the rest of your life. I’ve heard they’re pretty crappy... ===\n=== Type 'help' to view a list of commands that you can use. Use 'look' to see what room you are in at any given moment. ===\n=== Use 'move (direction)' to move around the map and look for the key! You will find several items to help you on your journey. ===\n=== Have Fun!=== \n"

  # Returns the current game message
  def get_message(self):
      return self.__message

  # Moves the player to a neighboring room
  def move(self, direction):
      if self.__game_won:  # If the game is already won, do not let the player take anything further.
          self.__message = "The game is already won! No further actions are allowed."
          return
      next_room = self.__currentRoom.get_neighbor(direction)
      if next_room:
          self.__previousRoom = self.__currentRoom
          self.__currentRoom = next_room
          self.__moves_remaining -= 1
          self.look()
          if self.__moves_remaining <= 0:
              self.__game_lost = True
              self.print_losing_message()
              return
      else:
          self.__message = "You can't go that way."

  # Describes the current room and its contents
  def look(self):
      self.__message = str(self.__currentRoom)

  # Takes an item from the current room and adds it to the users inventory
  def take(self):
      if self.__game_won:  # If the game is already won, do not let the player take anything further.
          self.__message = "The game is already won! No further actions are allowed."
          return
      if self.__currentRoom is None:
          print("error: No current room set.")
          return

      if self.__currentRoom.has_item():
          item = self.__currentRoom.get_item()
          # weight limit for candy
          if item.get_name().lower() == "unlimited candy":
              self.__message = "That is too much candy for you to hold, you can't pick it up!"
              return

          # The part of the function the "picks up" the item
          item = self.__currentRoom.remove_item()
          self.__inventory.append(item)
          self.__message = f"You took {item.get_name()}."

          # Checks to see if the item the player just picked up is the bathroom key
          if item.get_name() == "Bathroom Key":
              self.__game_won = True
              self.print_winning_message()  # Print the winning message if the player picked up the key
              return
      else:
          self.__message = "There is nothing to take."

   # Places an item from the player's inventory into the current room
  def place(self, name):
      #Checks to make sure the user enters an item with place
      if not name or not name.strip():
          self.__message = "Make sure to specify an item to place! Try 'place (item)'."
          return
      # Normalize the input by stripping unnecessary words like "a" or "an"
      normalized_name = name.lower().strip()
      # Remove articles like "a", "an", and "the" from the input
      normalized_name = normalized_name.lstrip('a ').lstrip('an ').lstrip('the ')
      # Now check the inventory and strip articles from the item names there too
      normalized_inventory = [item.get_name().lower().lstrip('a ').lstrip('an ').lstrip('the ')
                              for item in self.__inventory]
      # Check if the normalized name matches any item in the inventory
      if normalized_name in normalized_inventory:
          # Find the corresponding item in the original inventory list
          item_to_place = self.__inventory[normalized_inventory.index(normalized_name)]

          # Makes sure the the item is not None before moving on
          if item_to_place:
            # Place the item in the room
            self.__inventory.remove(item_to_place)
            self.__currentRoom.set_item(item_to_place)
            self.__message = f"You carefully place {item_to_place.get_name()} in the room."
          else:
              self.__message = f"Could not find an item. Make sure you type 'place (item)', not just 'place'"
      else:
          self.__message = f"You are not holding a {name}."

  # Consumes an item in the player's inventory
  def consume(self, item_name):
      if not item_name:
          self.__message = "Make sure to specify an item to consume! Try 'consume (item)'."
          return
      # Search for the item in the inventory, ignoring case
      item = next((i for i in self.__inventory if i.get_name().lower() == item_name.lower()), None)

      if item:  # If the item is found
          self.__inventory.remove(item)  # Remove the item from the inventory
          if item.get_name().lower() == "ghoul":
              if random.random() < 0.1:  # 10% chance of getting sick
                  self.__message = "You got sick from the Ghoul! You lose!"
                  sys.exit()
              else:
                  self.__message = "You feel energized! You gained 2 extra moves."
                  self.__moves_remaining += 2
          elif item.get_name().lower() == "mutz":
              self.__message = "You feel better! You gained 2 extra moves."
              self.__moves_remaining += 2
          elif item.get_name().lower() == "candy":
              self.__message = "This is too much candy for you to carry"
          else:
              self.__message = f"The {item.get_name()} had no noticeable effect."
      else:
          self.__message = f"You don't have {item_name} to consume."

  # Moves the player back to the previous room
  def retreat(self):
      if self.__previousRoom:
          if self.__moves_remaining > 0:
            self.__currentRoom, self.__previousRoom = self.__previousRoom, self.__currentRoom
            self.__message = "You retreated to the previous room."
      else:
          self.__message = "You can't retreat from here."

  #Updates the game's message with either the NPC's phrase or a message indicating no NPC is present
  def speak(self):
      if self.__currentRoom.has_npc():
          npc = self.__currentRoom.get_npc()
          phrase = npc.get_phrase()
          self.__message = f"{npc.get_name()} says: '{phrase[random.randint(0, 2)]}'."
      else:
          self.__message = "There is no one here to speak to."

  # Updates the game’s message with a list of the items that the player is holding, or a message saying their inventory is empty
  def items(self):
      if self.__inventory:  # Check if the player is holding any items
          item_list = "\n".join(
              [f"a {item.get_name()}" for item in self.__inventory])  # Create a formatted list of items
          self.__message = f"You are holding:\n{item_list}"
      else:
          self.__message = "You are not holding any items."

  # Searches the player's inventory for an item by name.
  def search_items(self, name):
      for item in self.__inventory:  # Loop through each item in the player's inventory
          if item.get_name().lower == name.lower():  # Compare item names (case-insensitive)
              return item  # Return the found item
      return None  # If no matching item is found, return None

  # Checks if the game is over
  def game_over(self):
      return self.__game_won

  # Parses the player's input into an action and optional argument
  def parse_command(self, command):
      parts = command.lower().split(maxsplit=1)
      action = parts[0]
      argument = parts[1] if len(parts) > 1 else None
      return action, argument

  # Update the game’s message with hints, suggestions, and reminders
  def help(self):
      self.__message = (
          "You are lost and alone. Find the Bathroom Key and unlock the bathroom to win. "
          "Commands include:\n"
          "- move <direction>: Move to a neighboring room.\n"
          "- look: See the current room's description.\n"
          "- take: Pick up an item in the room.\n"
          "- place <item>: Place an item from your inventory in the room.\n"
          "- consume <item>: Use an item from your inventory.\n"
          "- speak: Talk to any NPC in the room.\n"
          "- retreat: Return to the previous room.\n"
          "- items: Check what you're holding.\n"
          "- quit: Exit the game.")

  # Prints the message the user sees when they win
  def print_winning_message(self):
    self.__message = "\n=== Winning Message ===\n\nCongratulations! You found the key to the bathroom! Unfortunately, you got too excited and relaxed a little too much, so you crapped yourself, but I guess you still won!! Yay!"
    # print(self.__message)

  # Prints the message the user sees when they lose
  def print_losing_message(self):
     self.__message = "\n === GAME OVER ===\n\nYou Lose! You filled your britches and are hereby sentenced to live out your days in a waste management facility! MWAHAHAHA"


  # Demonstrates the sequence of actions to win the game. It simulates a walkthrough and outputs the updated message after each action. Used for testing and verification
  def auto_win(self):
      # Initialize the game state for the test
      print("=== Auto Win Sequence ===")

      # Simulate moving to a room containing the key
      print("\nMoving to the room with the Bathroom Key...")
      self.__currentRoom = self.__key_room
      self.look()
      # Take the key
      self.take()

if __name__  == '__main__':
    g = Game()
    g.play()
