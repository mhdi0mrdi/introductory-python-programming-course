from os import system


player_list = []


while True:
    print("\n\n1. [A]dd player")
    print("2. [S]how players")
    print("3. [E]xit")
    menu = input("menu : ")
    system("cls")

    match menu:
        case "1" | "A":

            while True:
                if input("Do you want to add a contact (yes,etc) ? ") != "yes":
                    system("cls")
                    break

                system("cls")

                # region get name
                while True:
                    name = input("name : ")
                    system("cls")

                    if name != "":
                        break

                    print("Error")
                # endregion

                # region get family
                while True:
                    family = input("family : ")
                    system("cls")

                    if family != "":
                        break

                    print("Error")
                # endregion

                # region get age
                while True:
                    age = int(input("age : "))
                    system("cls")

                    if age in range(18, 51):
                        break

                    print("Error")
                # endregion

                # region get ncode
                while True:
                    n_code = input("nationalcode : ")
                    system("cls")

                    if n_code != "":
                        break

                    print("Error")
                # endregion

                player = [name, family, age, n_code]
                player_list.append(player)

        case "2" | "S":
            print("ID\tName\tFamily\tAge\tNcode")
            print("---------------------------")
            for id_, player in enumerate(player_list, 1):
                print(id_, *player, sep="\t")
            print("---------------------------")

        case "3" | "E":
            break

        case _:
            print("Error!!!")
