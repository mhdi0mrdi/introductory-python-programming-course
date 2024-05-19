from os import system
from random import randint
from datetime import datetime
from time import sleep

# region start hint

print("hello and wellcome to this game")
sleep(0)
system("cls")
print("in this game , you first choose the level of this game")
sleep(0)
system("cls")
print("the number of numbers to be guessed by you is based on the selected level")
sleep(0)
system("cls")

while True:
    system("cls")
    if input("press enter to continue :") != "":
        continue
    else:
        break


# endregion

# region level
flag = True
while flag:
    game_level = input("\n\n enter level of the game(4,5,6):")
    system("cls")

    if game_level in ("4", "5", "6"):
        game_level = int(game_level)
        flag = False
    else:
        print("Error!!! pls enter level")


# endregion

# region random num




# endregion
