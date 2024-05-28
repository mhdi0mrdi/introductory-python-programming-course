from collections import namedtuple
from os import system


todo_list = []


while True:
    print("add todo (1)")
    print("show todo (2)")
    print("exittodo (3)")
    menu = input("menu :")
    system("cls")

    match menu:
        case "1":
            # region title
            while True:
                title = input("title :")
                system("cls")

                if title != "":
                    break

                print("error!")
            # endregion

            # region time
            while True:
                time = input("time :")
                system("cls")

                if title != "":
                    break

                print("error!")
            # endregion

            # region active
            while True:
                active = input("active or deactive :")
                system("cls")

                if active in ("active", "deactive"):
                    break

                if title == "":
                    print("error! field is empty")

                else:
                    print("not in active or deactive")
            # endregion

            # region description
            description = input("description :")
            system("cls")
            # endregion

            todo = (title, time, active,
                    description)
            todo_list.append(todo)

        case "2":
            
            print("\tTitle\ttime\tactive\tdescription")
            print("______________________________________________")
            for id_, tdo in enumerate(todo_list, 1):
                print(id_, *tdo, sep="\t")
            print("_______________________________________________")
            
        case "3":
            break
