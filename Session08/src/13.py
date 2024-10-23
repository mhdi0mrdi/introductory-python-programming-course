from os import system


person_list = []


while True:
    # region menu
    print("________________________")
    print("1. Add person")
    print("2. Show person")
    print("3. Exit")
    print("________________________")
    menu = input("menu : ")
    system("cls")
    # endregion


    match menu:
        case "1":
            # region name
            while True:
                name = input("name : ")
                system("cls")

                if name!="":
                    break

                print("Error")
            # endregion

            # region family
            while True:
                family = input("family : ")
                system("cls")

                if family!="":
                    break

                print("Error")
            # endregion
        
            person = [name, family]
            person_list.append(person)

        case "2":
            print("#\tName\tFamily")
            print("____________________________________________")
            for id_, person in enumerate(person_list):
                print(id_, *person, sep="\t")
            print("____________________________________________")

        case "3":
            break
        
        case _:
            print("Error")

        


