import sys
import time


class Player:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.location = 'None'
        self.game_over = False
        self.health = 100
        self.hasScope = False  # Has item that shows hidden items
        self.numOfItems = 0

    def addPlayerItem(self, item):
        """
        Test documentation
        :param item:
        """
        self.items.append(item)
        self.numOfItems += 1

    def viewHealth(self):
        if self.health == 100:
            return '{} is feeling okay.'.format(self.name)
        elif self.health < 50:
            return '{} is badly hurt. '.format(self.name)
        elif self.health <= 0:
            self.game_over = True
            return '{} is Dead. '.format(self.name)

    def number_of_items(self):
        return self.number_of_items


class GameItem:
    def __init__(self, name, is_key, is_scope, is_trap):
        self.name = name
        self.description = 'description'
        self.is_key = False  # Open room
        self.is_scope = False  # Find hidden items in room
        self.is_trap = False  # Hurt player if chosen

    def trap_activate(self, player):
        player.health -= 30


class Room:
    def __init__(self, name):
        self.name = name
        self.description = 'description'
        self.items = []
        self.hasHiddenItem = False
        self.hiddenItem = ''
        self.numOfItems = 0
        self.key_item = None

    def addRoomItems(self, items):
        for item in items:
            self.items.append(item)
            self.numOfItems += 1

    def removeItem(self, choice):
        return self.items.pop(choice - 1)

    def correctKey(self, choice):
        return choice == self.key_item


class House:
    """docstring for House"""

    def __init__(self):
        self.rooms = []
        self.numOfRooms = 0

    def addRooms(self, rooms):
        for room in rooms:
            self.rooms.append(room)
            self.numOfRooms += 1


#####################################################################


def game():
    while True:
        choice = input("> ")
        if choice.lower() == 'q':
            sys.exit()
        elif choice.lower() == 'r':
            roomChoice()
        elif int(choice) > player1.location.numOfItems:
            print('Please enter a valid command.')
        else:
            pickupItem(int(choice))


def itemPrint(item_list):
    i = 1
    for item in item_list:
        message = '{}. {}'.format(i, item.name)
        systemPrint(message)
        i += 1
    print()
    print('Choose something, type the number')
    print("Type 'r' to view rooms you can travel to")
    print("Type 'q' to exit game")


# print("Type 'i' to view items in your inventory")


def roomCheck(choice):
    room = house1.rooms[choice - 1]
    if room.key is not None:  # Needs a key to enter
        message = "The door to this room is locked would you like to \n" \
                    "try to open it?"
    else:  # Does not need a key
        player1.location = house1.rooms[int(choice) - 1]
        enterRoom()


def open_door():
    items = player1.items
    itemPrint(items)

# -------------------------------------------------------------------------
# Choosing a room to enter
# -------------------------------------------------------------------------


def roomChoice():
    itemPrint(house1.rooms)
    print()
    print('Choose a room to enter.')
    chooseRoom()


def enterRoom():
    room = player1.location
    into_room = '{} walks into {}. {}'.format(player1.name, room.name, room.description)
    systemPrint(into_room)
    itemPrint(room.items)
    game()


def chooseRoom():
    while True:
        choice = input("> ")
        if choice.lower() == 'q':
            sys.exit()
        elif int(choice) > house1.numOfRooms:
            print('Please enter a valid choice. ')
        else:
            player1.location = house1.rooms[int(choice) - 1]
            enterRoom()

# -----------------------------------------------------------------------------

# -------------------------------------------------------------------------
# Common functions
# -------------------------------------------------------------------------


def systemPrint(sentence):
    for word in sentence:
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# Game Step up
# -------------------------------------------------------------------------

# Title Screen for the game


def title_screen():
    print('Welcome to Escape the House! ')
    print()
    print("Type 'Play' to begin the game")
    print("Type 'quit' to exit the game")
    choice = input("> ")
    if choice.lower() == "play":
        setup_game()
    elif choice.lower() == "quit":
        sys.exit()
    while choice.lower() not in ['play', 'quit']:
        print('Please enter a valid command.')
        choice = input('> ')
        if choice.lower() == 'play':
            setup_game()
        elif choice.lower() == 'exit':
            sys.exit()


def setup_game():
    welcome_message = "You wake up in the bedroom feeling like your head\n " \
                      "is about to explode. You feel that something is not\n " \
                      "right. You need to get out of this house."

    objective_message = "Find a key and head to the exit"
    systemPrint(welcome_message)
    systemPrint(objective_message)
    enterRoom()
# -------------------------------------------------------------------------


def pickupItem(choice):
    player = player1
    current_room = player1.location
    item = current_room.removeItem(choice)
    player.addPlayerItem(item)
    pickup_confirm = '{} picked up {}.'.format(player.name, item.name)
    systemPrint(pickup_confirm)
    game()


if __name__ == '__main__':
    player1 = Player('Rob')

    # Create the rooms
    room1 = Room('Living Room')
    room2 = Room('Bed Room')
    room3 = Room('Bathroom')
    room4 = Room('Kitchen')
    room5 = Room('Exit')

    room1.description = "The living room is in disarray, the TV is open\n" \
                        "but only static is on."
    room2.description = 'The bedroom is dimly light with things ' \
                        'sprawled all over the flaw.'
    room3.description = 'The bathroom is surprisingly tidy.'
    room4.description = 'The kitchen looks like a bomb went off.'

    # Create items [name, is_key, is_scope, is_trap]
    item1 = GameItem('Key', True, False, False)
    item2 = GameItem('Moldy bread', False, False, False)
    item3 = GameItem('Hat', False, False, False)
    item4 = GameItem('Guitar', False, False, False)
    item5 = GameItem('Bed Sheets', False, False, False)
    item6 = GameItem('Glasses', False, True, False)
    item7 = GameItem('Mirror', False, False, False)
    item8 = GameItem('Clothes', False, False, False)
    item9 = GameItem('Toilet Paper', False, False, False)
    item10 = GameItem('Tooth Brush', False, False, False)
    item11 = GameItem('Soap', False, False, False)
    item12 = GameItem('Towel', False, False, False)
    item13 = GameItem('Knife', False, False, True)
    item14 = GameItem('Pot', False, False, False)
    item15 = GameItem('Tong', False, False, False)
    item16 = GameItem('Water', False, False, False)

    # Rooms set up
    room1.addRoomItems([item1, item2, item3, item4])
    room2.addRoomItems([item5, item6, item7, item8])
    room3.addRoomItems([item9, item10, item11, item12])
    room4.addRoomItems([item13, item14, item15, item16])
    room5.key_item = item1  # Setting the key for Exit to item1

    # Create the full house
    house1 = House()
    house1.addRooms([room1, room2, room3, room4, room5])
    player1.location = room2
    title_screen()
