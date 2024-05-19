from os import system


flag = True


while flag:
    name = input("name : ")
    system("cls")

    if name != "":
        flag = False
    else:
        print("Error!!!,", end="")


print("Your name is : ", name)
