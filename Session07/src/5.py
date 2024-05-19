from os import system

data = [None] * 100

for index in range(len(data)):

    # region get name

    while True:
        name = (input('name :'))

        if name != "":
            break

        print("error!!")

    # endregion

    data[index] = name

for index in range(len(data)):
    print(data[index])
