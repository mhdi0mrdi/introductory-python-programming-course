from random import randint
from os import system
from datetime import datetime
from time import sleep


# region get password
flag = True

while flag:
    user_password = input("password : ")
    system("cls")

    if user_password == "12345":
        flag = False
    else:
        print("Error!!!")
# endregion

# region weelcome
print("Wellcome :) ")
sleep(2)
system("cls")
# endregion


continue_ = True

while continue_:
    system("cls")

    # region get level
    flag = True

    while flag:
        level = input("Level 3,5,7 : ")
        system("cls")

        if level in ("3", "5", "7"):
            level = int(level)
            flag = False
        else:
            print("Error")
    # endregion

    user_score = 0
    pc_score = 0
    counter = 0
    start_time = datetime.now()

    while user_score < level and pc_score < level:

        # region get user input
        flag = True

        while flag:
            user_input = input("\n\n1.Rock 2.Paper 3.Scissors : ")
            system("cls")

            if user_input in ("1", "2", "3"):
                user_input = int(user_input)
                flag = False
            else:
                print("Error!!!")
        # endregion

        pc_input = randint(1, 3)
        counter += 1
        system("cls")

        # region check score
        match (user_input, pc_input):
            case (1, 3) | (2, 1) | (3, 2):
                user_score += 1
            case (3, 1) | (1, 2) | (2, 3):
                pc_score += 1
        # endregion

        # region show info
        match user_input:
            case 1:
                print("User : Rock")
            case 2:
                print("User : Paper")
            case 3:
                print("User : Scissors")

        match pc_input:
            case 1:
                print("PC : Rock")
            case 2:
                print("PC : Paper")
            case 3:
                print("PC : Scissors")

        print("User score :", user_score, ", PC score :", pc_score)
        # endregion

    # region show gane result
    end_time = datetime.now()
    print("\n\nGame count :", counter)
    print("Game level :", level)
    print("Game time :", end_time-start_time)

    if user_score == level:
        print("user won")
    else:
        print("pc won")

    # endregion

    sleep(2)

    if input("\n\nDo you want to continue (yes-etc) :") != "yes":
        continue_ = False
