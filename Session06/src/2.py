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
    if input("press enter to continue :") == "":
        break
        
system("cls")
# endregion

# region password
while True:
    user_password = input("password : ")
    system("cls")

    if user_password == "12345":
        break
    
    print("password is not correct!")

system("cls")
# endregion

continue_ = True

while continue_:
    system("cls")
# region level
    start_time = datetime.now()
    flag = True
    while flag:
        game_level = input("\n\n enter level of the game(4,5,6):")
        system("cls")

        if game_level in ("4", "5", "6"):
            game_level = int(game_level)
            flag = False
        else:
            print("Error!!! pls enter level")

    system("cls")

    # endregion

# region random num

    if game_level == 4:
        chosen_num = randint(1000, 10000)
    elif game_level == 5:
        chosen_num = randint(10000, 100000)
    else:
        chosen_num = randint(100000, 1000000)
    print(chosen_num)
    # endregion

# region user input

    game_count = 0
    flag = True
    while flag:
        gues_number = int(input("gues the number:"))
        if gues_number < chosen_num:
            print("chosen num < random num")
            game_count += 1
        elif gues_number > chosen_num:
            print("chosen num > random num")
            game_count += 1
        elif gues_number == chosen_num:
            flag = False
    system("cls")

    # endregion

# region resault

    end_time = datetime.now()
    print("\n\nnice!!")
    print("The number was:", chosen_num)
    print("Game count :", game_count)
    print("Game level :", game_level)
    print("Game time :", end_time-start_time)
    sleep(8)
    system("cls")

    # endregion

    if input("\n\nDo you want to continue (yes-etc) :") != "yes":
        continue_ = False
