from os import system

name_list = [None] * 5


for index in range(len(name_list)):

    # region get name
    while True:
        name = (input('name :'))
        system("cls")

        if name != "":
            break

        print("error!!")
    # endregion

    name_list[index] = name


# for index in range(len(name_list)):
#     print(name_list[index])

for name in name_list:
    print(name)
