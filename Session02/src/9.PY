from random import randint
from os import system
from datetime import datetime



user_score = 0
pc_score = 0
counter = 0
start_time = datetime.now()

while user_score<3 and pc_score<3:

    # region get input
    user_input = int(input("\n\n1.Rock 2.Paper 3.Scissors : "))
    pc_input = randint(1, 3)
    counter += 1
    system("cls")
    # endregion

    # region check score
    match (user_input, pc_input):
        case (1, 3) | (2, 1) | (3,2):
            user_score += 1
        case (3, 1) | (1, 2) | (2,3):
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
print("Game time :", end_time-start_time)

if user_score==3:
    print("user won")
else:
    print("pc won")

# endregion

