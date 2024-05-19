from os import system

flag = True


while flag:
    age = int(input('age :'))
    system("cls")

    if age in range(1, 121):
        flag = False
    else:
        print("error!!!, ", end="")


print("uour age is:", age)
