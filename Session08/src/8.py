
from os import system


player_list = []


for _ in range(2):

    # region get name
    while True:
        name = input("name : ")
        system("cls")

        if name != "":
            break

        print("Error")
    # endregion

    # region get family
    while True:
        family = input("family : ")
        system("cls")

        if family != "":
            break

        print("Error")
    # endregion

    # region get age
    while True:
        age = int(input("age : "))
        system("cls")

        if age in range(18, 51):
            break

        print("Error")
    # endregion

    player = [name, family, age]
    player_list.append(player)


print("ID\tName\tFamily\tAge")
print("---------------------------")
for id_, player in enumerate(player_list, 1):
    print(id_, *player, sep="\t")
print("---------------------------")
