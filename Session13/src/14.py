# 1. Add todo
# 2. display todo
# 3. remove todo
# 4. search todo
# 5. exit


from os import system
from random import randint


todo_list = []

while True:
    print("add todo (1) :")
    print("display todo(2) :")
    print("remove todo (3) :")
    print("search todo (4) :")
    print("exit (5) :")

    menu = int(input("menu ?:"))
    system('cls')

    match menu:
        case 1:
            while True:
                # region code
                while True:
                    code = randint(1000, 9999)

                    for todo in todo_list:
                        if todo[0] == code:
                            print("error!")
                            break
                    else:
                        break
                # endregion

                # region title
                while True:
                    title = input("title :")

                    if title == "":
                        print("error!")
                        continue

                    for todo in todo_list:
                        if todo[1] == title:
                            print("error!")
                            break
                    else:
                        break
                # endregion

                # region time
                while True:
                    time = input("time :")
                    system('cls')

                    if time == "":
                        print("error!")
                        continue
                    if time not in range(2020, 2025):
                        break
                    print("error!")
                # endregion

                # region description
                description = input("description :")
                system('cls')
                # endregion

                todo = (code, title, time, description)
                todo_list.append(todo)

                if input("do you want to add todo again? (yes/etc):") != "yes":
                    break
        case 2:
            # region show
            print("___________________________________________")
            for todo in todo_list:
                print(*todo, sep="\t")
            print("___________________________________________")
            # endregion
        case 3:
            while True:
                # region show todoes
                print("___________________________________________")
                for todo in todo_list:
                    print(*todo, sep="\t")
                print("___________________________________________")
                # endregion

                # region get remove value
                remove_val = int(input("todo code :"))
                system('cls')
                # endregion

                # region show
                for todo in todo_list:
                    if todo[0] == remove_val:
                        print("code :", todo[0])
                        print("title :", todo[1])
                        print("time :", todo[2])
                        print("description :", todo[3])

                        if input("do you want to remove? :") == "yes":
                            system('cls')
                            todo_list.remove(todo)
                # endregion

                if input("do you want to remove todo again? (yes/etc):") != "yes":
                    break

        case 4:
            while True:

                # region get remove value
                search_val = int(input("todo code :"))
                system('cls')
                # endregion

                # region show
                for todo in todo_list:
                    if search_val in todo:
                        print(*todo, sep="\t")
                # endregion
