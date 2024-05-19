from os import system


data = [None] * 20


for index in range(len(data)):

    # region get score
    while True:
        score = float(input('score :'))
        system("cls")

        if 0<=score<=100:
            break

        print("Error", end="")
    # endregion

    data[index] = score