from os import system

continue_ = True

while continue_:
    system("cls")

    # region menu
    flag = True

    while flag:
        menu = input("enter menu 1or 2?(mul , sum):")
        system("cls")

        if menu in ("1", "2"):
            menu = int(menu)
            flag = False
        else:
            print("try again")
    # endregion


    if menu == 1:
        i = 1
        mul = 1

        while i <= 5:
            num = int(input('enter number :'))
            system("cls")
            mul *= num
            i += 1

        print("res:", mul)
    else:
        i = 1
        sum_ = 0

        while i <= 5:
            num = int(input('enter number :'))
            system("cls")
            sum_ += num
            i += 1

        print("res:", sum_)


    if input("\n\ndo you want to continue?") != "yes":
        continue_ = False
