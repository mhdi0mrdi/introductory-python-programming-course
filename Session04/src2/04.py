from os import system

continue_ = True

while continue_:
    system("cls")

    # region get menu
    flag = True

    while flag:
        print("1.sub", "2.mul", "3.div", "4.sum")
        menu = input("enter number .. 1,2,3,4:")
        system("cls")

        if menu in ("1", "2", "3", "4"):
            menu = int(menu)
            flag = False
        else:
            print("error")
    # endregion

    num1 = int(input('num1 :'))
    num2 = int(input('num2 :'))
    system("cls")

    if menu == 1:
        print("resault:", num1 - num2)
    elif menu == 2:
        print("resault:", num1 * num2)
    elif menu == 3:
        print("resault:", num1 / num2)
    else:
        print("resault:", num1 + num2)

    if input("\n\nDo you want to continue (yes-etc) :") != "yes":
        continue_ = False
