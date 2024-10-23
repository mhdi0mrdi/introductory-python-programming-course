from os import system


number_of_player = 20
player_list = [None] * (number_of_player*3)

# set
for index in range(number_of_player):

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

    player_list[(index*3) + 0] = name
    player_list[(index*3) + 1] = family
    player_list[(index*3) + 2] = age


for index in range(len(player_list)):
    
    if index%3==0:
        print()

    print(player_list[index], end="\t")


# index= 0  =>  0, 1, 2
# index= 1  =>  3, 4, 5
# index= 2  =>  6, 7, 8

# [meisam, ilka, 32, ahmad, shabani, 35, milad, rabiei, 22]