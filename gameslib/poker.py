import random
from itertools import groupby


nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = {nine: "9", ten: "10", jack: "J", queen: "Q", king: "K",
         ace: "A"}
player_score = 0
computer_score = 0


def start():
    print("Lets play a game of Poker Dice")
    while game():
        pass
    scores()


def game():
    print("The computer will help you throw your 5 dice")
    throws()
    return play_again()


def throws():
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    for i in range(len(dice)):
        print("Dice", i + 1, ":", names[dice[i]])

    result = hand(dice)
    print("you currently have", result)

    while True:
        rerolls = input("How many dice do you want to throw again? ")
        rerolls = int(rerolls)
        try:
            if rerolls in (1, 2, 3, 4, 5):
                break
        except ValueError:
            pass
        print("Oops!, I didn't understand that. Please enter 1, 2, 3, 4 or 5.")

        if rerolls == 0:
            print("You finish with", result)
        else:
            roll_number = rerolls
            dice_rerolls = roll(roll_number)
            dice_changes = range(rerolls)
            print("Enter the number of dice to reroll: ")
            iterations = 0
            while iterations < rerolls:
                iterations += 1
                while True:
                    selection = input("")
                    try:
                        if selection in (1, 2, 3, 4, 5):
                            break
                    except ValueError:
                        pass
                    print("Oops! I didn't understand that. Please enter 1, 2, 3, 4 or 5")
                dice_changes[iterations-1] = selection-1
                print("You have changed dice", selection)

            iterations = 0
            while iterations < rerolls:
                iterations = iterations + 1
                replacement = dice_rerolls[iterations-1]
                dice[dice_changes[iterations-1]] = replacement

            dice.sort()
            for i in range(len(dice)):
                print("Dice", i+1, ":", names[dice[i]])

            result = hand(dice)
            print("You finish with", result)


def roll(roll_number):
    """
    Args:
        roll_number:
    """
    numbers = range(1, 7)
    roll_number = int(roll_number)
    dice = [*range(0, roll_number, 1)]
    iteration = 0
    while iteration < roll_number:
        iteration += 1
        dice[iteration-1] = random.choice(numbers)
    return dice


def hand(dice):
    """
    Args:
        dice:
    """
    dice_hand = [len(list(group)) for key, group in groupby(dice)]
    dice_hand.sort(reverse=True)
    straight1 = [1, 2, 3, 4, 5]
    straight2 = [2, 3, 4, 5, 6]

    if dice == straight1 or dice == straight2:
        return "a straight!"
    elif dice_hand[0] == 5:
        return "five of a kind!"
    elif dice_hand[0] == 4:
        return "four of a kind!"
    elif dice_hand[0] == 3:
        if dice_hand[1] == 2:
            return "a full house"
        else:
            return "three of a kind"
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return "two pairs"
        else:
            return "one pair"
    else:
        return "a high card"


def play_again():
    answer = input("Would you like to play again? y/n: ")
    if answer in ("Y", "y", "yes", "Yes", "Of course"):
        return answer
    else:
        print("Thanks for playing")


def scores():
    global player_score, computer_score
    print("High Score")
    print("Player", player_score)
    print("Computer", computer_score)


if __name__ == '__main__':
    start()