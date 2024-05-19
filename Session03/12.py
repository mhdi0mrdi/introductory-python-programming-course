
# num1 = float(input('num1 :'))
# num2 = float(input('num2 :'))

# print(num1, "+", num2, "=", num1+num2)

# from os import system

# flag = True

# while flag:
#     system("cls")

#     #TODO

#     if input("DO you want to continue(yes-etc) ?") != "yes":
#         flag = False



from os import system

flag = True

while flag:
    system("cls")

    num1 = float(input('num1 :'))
    num2 = float(input('num2 :'))
    print(num1, "+", num2, "=", num1+num2)

    if input("\n\nDO you want to continue(yes-etc) ?") != "yes":
        flag = False
