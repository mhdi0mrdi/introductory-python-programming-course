
# i = 1

# while i<=20:
#     print("ilka")
#     i += 1


# if True:
#     print("ilka")

# if False:
#     print("ilka")


# while True:
#     print("ilka")

# print("end")


# while False:
#     print("ilka")

# print("end")


# flag = True

# while flag:
#     print("ilka")

from os import system


flag = True
password = "12345"


while flag:
    user_inp = input("password : ")
    system("cls")

    if user_inp != password:
        print("Error!!!, ", end="")
    else:
        flag = False


print("Hi meisam!!!")
