
# # player_list = ["meisam", "ilka", 32, "mahdi", "moradi", 19, "sara", "mosavi", 28]


# # player_list = [["meisam", "ilka", 32], ["mahdi", "moradi", 19], ["sara", "mosavi", 28]]


# # # nested list
# # player_list = [
# #     ["meisam", "ilka", 32],
# #     ["mahdi", "moradi", 19],
# #     ["sara", "mosavi", 28]
# # ]


# # res = len(player_list)
# # res = player_list[0]

# # res = player_list[2][1]

# # player_list[2][1] = "rezaei"


# # player_list = [
# #     ["meisam", "ilka", 32],
# #     ["mahdi", "moradi", 19],
# #     ["sara", "mosavi", 28]
# # ]

# from os import system


# player_list = []


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

#     player = [name, family, age]
#     player_list.append(player)


score_list = []

for _ in range(11):

    # region php
    while True:
        php = float(input("php score:"))

        if 0 <= php <= 100:
            break
        print("error")
    # endregion

    # region java
    while True:
        java = float(input("java score:"))

        if 0 <= java <= 100:
            break
        print("error")
    # endregion

    # region python
    while True:
        python = float(input("python score:"))

        if 0 <= python <= 100:
            break
        print("error")
    # endregion

    score = {"php": php, "java": java, "python": python}
    score_list.append(score)



for id_, score in enumerate(score_list, 1):
    print(id_, score["php"], score["java"], score["python"])
