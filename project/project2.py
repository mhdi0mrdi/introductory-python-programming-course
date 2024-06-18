

from copy import deepcopy
from os import system
from random import randint
from time import sleep


car_list = [("BMW", "528", "blue", "hichi", "1001"),
            ("toyota", "supra", "white", "hichiz", "1002")]

while True:
    # region menu
    print("1. add new car ")
    print("2. show car list ")
    print("3. remove car ")
    print("4. search car ")
    print("5. exit")
    menu = input("enter menu number :")
    # endregion

    match menu:
        case "1":
            while True:
                # region code
                while True:
                    car_code = str(randint(1000, 9999))

                    for car in car_list:
                        if car_code == car[4]:
                            break
                    else:
                        break
                # endregion

                # region car brand
                while True:
                    brand = input("brand :")
                    system('cls')

                    if brand != "":
                        break

                    print("Error! field is empty")
                # endregion

                # region model
                while True:
                    model_ = input("model :")
                    system('cls')

                    if model_ == "":
                        system('cls')
                        print("Error! field is empty")
                        continue

                    for car in car_list:
                        if model_ == car[1]:
                            print(f"{model_} already exist!!")
                            break
                    else:
                        break
                # endregion

                # region color
                while True:
                    color = input("color :")
                    system('cls')

                    if color != "":
                        break

                    print("field is empty")
                # endregion

                # region description
                description = input("discription :")
                system('cls')
                # endregion

                print("done!")
                sleep(2)
                system('cls')

                car = (brand, model_, color, description, car_code)
                car_list.append(car)

                if input("do you want to continue (yes-etc) :") == "yes":
                    system('cls')
                    break

        case "2":

            if input("Do you want to display all column (yes-etc) :") == "yes":
                system('cls')
                display_column = ("brand", "model", "color",
                                  "description", "code")
                display_index = (0, 1, 2, 3, 4)

            else:
                system('cls')

                display_column = []
                display_column = []

                for index, column in enumerate(("brand", "model", "color",
                                                "description", "code")):

                    if input(f"Do you want to display {column} (yes-etc) :") == "yes":
                        display_column.append(column)
                        display_index.count(index)

                    system('cls')

            print("sort", *display_column, sep="\t")
            print("__________________________________________________")
            for id_, car in enumerate(car_list, 1):
                print(id_, end="\t")

                for index in display_index:
                    print(car[index], end="\t")
                print()

            print("___________________________________________________")

        case "3":

            while True:
                if input("are you sure remove cars (yes-etc) :") != "yes":
                    system('cls')
                    break

                system('cls')

                # region show cars
                print("sort\tbrand\tmodel\tcolor\description\tcar code")
                print("__________________________________________________")
                for id_, car in enumerate(car_list, 1):
                    print(id_, *car, sep="\t")
                print("___________________________________________________")
                # endregion

                if input("\n\nDo you want to remove all todos (yes, etc) ? ") == "yes":
                    system("cls")
                    car_list.clear()
                    print("Done!")
                    break

                else:
                    system("cls")

                    # region get remove column
                    while True:
                        remove_column = input(
                            "Select remove column (1.brand 2.model 3.color 4.code) : ")
                        system("cls")

                        if remove_column in ["1", "2", "3", "4"]:
                            break

                        print("Error!")
                    # endregion

                    # region set remove index
                    match remove_column:
                        case "1":
                            remove_index = 0
                        case "2":
                            remove_index = 1
                        case "3":
                            remove_index = 2
                        case "4":
                            remove_index = 4
                    # endregion

                    # region show cars
                    print("sort\tbrand\tmodel\tcolor\description\tcar code")
                    print("__________________________________________________")
                    for id_, car in enumerate(car_list, 1):
                        print(id_, *car, sep="\t")
                    print("___________________________________________________")
                    # endregion

                    remove_value = input("remove value : ")
                    system("cls")
                    check_find = False

                    for car in deepcopy(car_list):
                        if car[remove_index] == remove_value:
                            check_find = True
                            print(f"brand :{car[0]}, brand :{car[1]}, Color :{
                                  car[2]}, code :{car[4]}")

                            if input("Are you sure delete this car (yes-etc) : ") == "yes":
                                system("cls")
                                car_list.remove(car)
                                print("Done!!!")
                            else:
                                system("cls")

                    if not check_find:
                        print(f"{remove_value} not found")

        case "4":
            # region get search menu
            while True:
                print("1. brand")
                print("2. model")
                print("3. color")
                print("4. code")
                print("5. exit")
                search_menu = input("search item :")
                system("cls")

                if search_menu in ["1", "2", "3", "4", "5"]:
                    break

                print("Error!!")
            # endregion

            if search_menu in ["5", "E"]:
                continue

            value = input("Search value : ")
            system("cls")

            match search_menu:
                case "1" :
                    search_index = 0
                case "2":
                    search_index = 1
                case "3" :
                    search_index = 2
                case "4" :
                    search_index = 4

            for car in car_list:
                if car[search_index] == value:
                    print(*car, sep="\t")


        case "5" :
            break

        case _ :
            print("Error!!!")

