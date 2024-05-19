from os import system

# region get password
correct_pass = False

for i in range(3):
    password = input("Password : ")
    system("cls")

    if password == "12345":
        correct_pass = True
        break

    print("Error")
# endregion


if correct_pass:
    print(" Wellcome :) ")
