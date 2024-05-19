from os import system
from random import randint
from datetime import datetime
from time import sleep


# region start hint
print("hello and wellcome to this game")
sleep(2)
system("cls")
print("in this game , you first choose the level of this game")
sleep(3)
system("cls")
print("the number of numbers to be guessed by you is based on the selected level")
sleep(3.5)
system("cls")


while True:
    system("cls")
    if input("press enter to continue :") != "":
        continue
    else:
        break
system("cls")
# endregion

# region password
pass_ = True

while pass_:
    user_password = input("password : ")
    system("cls")

    if user_password == "12345":
        pass_ = False
    else:
        print("password is not correct!")
system("cls")
# endregion


while True:
    system("cls")

    # region level
    while True:
        game_level = input("\n\n enter level of the game(4,5,6):")
        system("cls")

        if game_level in ("4", "5", "6"):
            game_level = int(game_level)
            break

        print("Error!!! pls enter level")

    system("cls")
    # endregion

    # region random num
    match game_level:
        case 4:
            chosen_num = randint(1000, 10000)
        case 5:
            chosen_num = randint(10000, 100000)
        case 6:
            chosen_num = randint(100000, 1000000)

    print(chosen_num)
    # endregion

    # region user input
    start_time = datetime.now()
    game_count = 0


    while True:
        gues_number = int(input("gues the number:"))
        game_count += 1
        system("cls")

        if gues_number < chosen_num:
            print(gues_number, " < random num")
            
        elif gues_number > chosen_num:
            print(gues_number, " > random num")

        else:
            end_time = datetime.now()
            break


    system("cls")
    # endregion

    # region resault
    print("\n\nnice!!")
    print("The number was:", chosen_num)
    print("Game count :", game_count)
    print("Game level :", game_level)
    print("Game time :", end_time-start_time)
    sleep(8)
    system("cls")
    # endregion

    if input("\n\nDo you want to continue (yes-etc) :") != "yes":
        break
