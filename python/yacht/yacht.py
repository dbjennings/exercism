"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Score categories.
# Change the values as you see fit.
YACHT = '66666'
ONES = '1'
TWOS = '2'
THREES = '3'
FOURS = '4'
FIVES = '5'
SIXES = '6'
FULL_HOUSE = '11122'
FOUR_OF_A_KIND = '4444'
LITTLE_STRAIGHT = '12345'
BIG_STRAIGHT = '23456'
CHOICE = '12346'

def score(dice: list, category):
    
    dice.sort()
    dice_as_string = ''.join(str(n) for n in dice)

    if category==YACHT:
        return 50 if min(dice)==max(dice) else 0

    elif int(category)>=1 and int(category)<=6:
        return int(category)*dice_as_string.count(category)

    elif category==FULL_HOUSE:
        bot = dice.count(min(dice))
        top = dice.count(max(dice))
        if bot+top==5 and abs(bot-top)==1:
            return sum(dice)
        return 0

    elif category==FOUR_OF_A_KIND:
        for num in '123456':
            if dice_as_string.count(num)>=4:
                return 4*int(num)
        return 0

    elif category==LITTLE_STRAIGHT:
        return 30 if dice_as_string==LITTLE_STRAIGHT else 0

    elif category==BIG_STRAIGHT:
        return 30 if dice_as_string==BIG_STRAIGHT else 0

    elif category==CHOICE:
        return sum(dice)
    else:
        return -1

p = score([1,5,5,5,5], FIVES)
print(p)