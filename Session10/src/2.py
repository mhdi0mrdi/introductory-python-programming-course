from os import system
from random import randint
from time import sleep

todo_list = [
    ["task1", "1400", "", "100000", "active"],
    ["task2", "1400", "", "100001", "active"],
    ["task3", "1400", "", "100002", "deactive"],
    ["task4", "1400", "", "100003", "deactive"],
    ["task5", "1400", "", "100004", "active"],
    ["task6", "1400", "", "100005", "deactive"]
]


while True:
    print("[A]dd plan (1):")
    print("[D]isplay todo (2):")
    print("[S]earch todo (3):")
    print("[AC]tive todo (4):")
    print("[DE]active todo (5):")
    print("[E]xit(6):")
    menu = input("enter menu num :")
    system("cls")

    match menu:
        case "A" | "1":
            while True:
                # region creat code
                while True:
                    plan_code = str(randint(100000, 999999))

                    for todo in todo_list:
                        if todo[3] == plan_code:
                            break
                    else:
                        break
                # endregion

                # region title
                while True:
                    title = input('title :')
                    system("cls")

                    if title == "":
                        print("error! field is empty")
                        continue

                    for todo in todo_list:
                        if todo[0] == title:
                            print(title, "exist")
                            break
                    else:
                        break
                # endregion

                # region time
                while True:
                    time = input("enter your time :")
                    system("cls")

                    if time != "":
                        break

                    print("error! field is empty")
                # endregion

                # region description
                description = input("description:")
                system("cls")
                # endregion

                # region status
                while True:
                    status = input("Status (active - deactive) : ")
                    system("cls")

                    if status in ["active", "deactive"]:
                        break

                    print("Error!")
                # endregion

                todo = [title, time, description, plan_code, status]
                todo_list.append(todo)

                sleep(2.5)
                system("cls")

                if input("Do you want to continue (yes-etc) : ") != "yes":
                    system("cls")
                    break

        case "D" | "2":
            print("Sort\tTitle\ttime\tDescription\tPlancode")
            print("______________________________________________")
            for id_, tdo in enumerate(todo_list, 1):
                print(id_, *tdo, sep="\t")
            print("_______________________________________________")

        case "3" | "S":
            # region get search menu
            while True:
                print("[C]ode (1)")
                print("[T]itle (2)")
                print("[TI]ime (3)")
                print("[S]tatus (4)")
                print("[E]xit (5)")
                search_menu = input("search item :")
                system("cls")

                if search_menu in ["1", "C", "2", "T", "3", "TI", "4", "S", "5", "E"]:
                    break

                print("Error!!")
            # endregion

            if search_menu in ["5", "E"]:
                continue

            value = input("Search value : ")
            system("cls")

            match search_menu:
                case "1" | "C":
                    search_index = 3
                case "2" | "T":
                    search_index = 0
                case "3" | "TI":
                    search_index = 1
                case "4" | "S":
                    search_index = 4

            for todo in todo_list:
                if todo[search_index] == value:
                    print(*todo, sep="\t")

        case "AC" | "4":

            while True:

                # region display deactive todo
                print(
                    "\n\n------------------------------------------------------------------------")

                for todo in todo_list:
                    if todo[4] == "deactive":
                        print(f"Title : {todo[0]}, Time : {todo[1]}, Description : {
                              todo[2]}, code : {todo[3]}, Status : {todo[4]}")

                print(
                    "------------------------------------------------------------------------")
                # endregion

                code = input("code (exit): ")
                system("cls")

                if code == "exit":
                    break

                for todo in todo_list:
                    if todo[3] == code:
                        todo[4] = "active"
                        break
                else:
                    print(code, "does not exist")

        case "DE" | "5":
            # region deactive todo
            while True:

                # region display deactive todo
                print(
                    "\n\n------------------------------------------------------------------------")

                for todo in todo_list:
                    if todo[4] == "active":
                        print(f"Title : {todo[0]}, Time : {todo[1]}, Description : {
                              todo[2]}, code : {todo[3]}, Status : {todo[4]}")

                print(
                    "------------------------------------------------------------------------")
                # endregion

                code = input("code (exit): ")
                system("cls")

                if code == "exit":
                    break

                for todo in todo_list:
                    if todo[3] == code:
                        todo[4] = "deactive"
                        break
                else:
                    print(code, "does not exist")
                # endregion
        
        case "6" | "E":
            break

        case _:
            print("Error!")
