from os import system
from random import randint
from datetime import datetime


# region password
while True:
    password = input("password : ")
    system("cls")

    if password == "12345":
        break

    print("Error!!!")
# endregion

# region get level
while True:
    level = input("1.[E]asy 2.[M]edium 3.[H]ard : ")
    system("cls")

    if level in ("1", "E", "2", "M", "3", "H"):
        break

    print("Error")
# endregion

# region cal game round
match level:
    case "1" | "E":
        game_round = 10
    case "2" | "M":
        game_round = 20
    case "3" | "H":
        game_round = 30
# endregion


start_time = datetime.now()
i = 1
user_score = 0


while i <= game_round:

    if randint(0, 1) == 0:
        var1 = True
        var2 = False
    else:
        var1 = False
        var2 = True

    # region get user input
    while True:
        user_input = input("Choose [1] or [2] : ")
        system("cls")

        if user_input in ("1", "2"):
            user_input = int(user_input)
            break

        print("Error,", end=" ")
    # endregion

    # region check score
    match (user_input, var1, var2):
        case (1, True, False) | (2, False, True):
            user_score += 1
    # endregion

    # region show info
    match (user_input, var1, var2):
        case (1, True, False) | (2, False, True):
            print("User won")
        case _:
            print("User lose")
    # endregion

    i += 1


# region show result
system("cls")
end_time = datetime.now()

print("Game time :", end_time-start_time)
print("Game round :", game_round)
print("User score : ", user_score)

if user_score >= (game_round//2):
    print("User Won")
else:
    print("User lose")
# endregion
