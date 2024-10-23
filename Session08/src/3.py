# from os import system


# player_list = []

# # set
# for _ in range(100):

#     # region get name
#     while True:
#         name = input("name : ")
#         system("cls")

#         if name != "":
#             break

#         print("Error")
#     # endregion

#     # region get family
#     while True:
#         family = input("family : ")
#         system("cls")

#         if family != "":
#             break

#         print("Error")
#     # endregion

#     # region get age
#     while True:
#         age = int(input("age : "))
#         system("cls")

#         if age in range(18, 51):
#             break

#         print("Error")
#     # endregion

#     player_list.append(name)
#     player_list.append(family)
#     player_list.append(age)


# for index in range(len(player_list)):

#     if index % 3 == 0:
#         print()

#     print(player_list[index], end="\t")


# # index= 0  =>  0, 1, 2
# # index= 1  =>  3, 4, 5
# # index= 2  =>  6, 7, 8

# # [meisam, ilka, 32, ahmad, shabani, 35, milad, rabiei, 22]


players = []

for _ in range(21):

    # region get name
    while True:
        name = input("name :")
        if name != "":
            break

        print("error")
    # endregion

    # region get family
    while True:
        family = input("family :")
        if family != "":
            break

        print("error")
    # endregion


    players.append(name)
    players.append(family)
