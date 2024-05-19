from copy import deepcopy
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
    print("[R]emove todo (6):")
    print("[ED]it todo (7):")
    print("[E]xit(8):")

 
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

            if input("Do you want display all column (yes-etc) : ") == "yes":
                system("cls")
                dispaly_column = ["title", "time",
                                  "description", "code", "status"]
                dispaly_index = [0, 1, 2, 3, 4]

            else:
                system("cls")

                dispaly_column = []
                dispaly_index = []

                for index, column in enumerate(["title", "time", "description", "code", "status"]):

                    if input(f"Do you want to display {column} (yes-etc)? ") == "yes":
                        dispaly_column.append(column)
                        dispaly_index.append(index)

                    system("cls")

            print("Sort", *dispaly_column, sep="\t")
            print("______________________________________________")
            for id_, tdo in enumerate(todo_list, 1):
                print(id_, end="\t")

                for index in dispaly_index:
                    print(tdo[index], end="\t")
                print()

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

        case "6" | "R":

            while True:
                if input("Are you sure deelete todos (yes-etc) : ") != "yes":
                    system("cls")
                    break

                system("cls")

                # region show todos
                print("Sort\tTitle\ttime\tDescription\tPlancode")
                print("______________________________________________")
                for id_, tdo in enumerate(todo_list, 1):
                    print(id_, *tdo, sep="\t")
                print("_______________________________________________")
                # endregion

                if input("\n\nDo you want to remove all todos (yes, etc) ? ") == "yes":
                    system("cls")
                    todo_list.clear()
                    print("Done!")
                    break

                else:
                    system("cls")

                    # region get remove column
                    while True:
                        remove_column = input(
                            "Select remove column (1.title 2.time 3.plan_code 4.status) : ")
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
                            remove_index = 3
                        case "4":
                            remove_index = 4
                    # endregion

                    # region show todos
                    print("Sort\tTitle\ttime\tDescription\tPlancode")
                    print("______________________________________________")
                    for id_, tdo in enumerate(todo_list, 1):
                        print(id_, *tdo, sep="\t")
                    print("_______________________________________________")
                    # endregion

                    remove_value = input("remove value : ")
                    system("cls")
                    check_find = False

                    for todo in deepcopy(todo_list):
                        if todo[remove_index] == remove_value:
                            check_find = True
                            print(f"Title :{todo[0]}, Time :{todo[1]}, Code :{
                                  todo[3]}, Status :{todo[4]}")

                            if input("Are you sure delete this todo (yes-etc) : ") == "yes":
                                system("cls")
                                todo_list.remove(todo)
                                print("Done!!!")
                            else:
                                system("cls")

                    # if check_find == False:
                    if not check_find:
                        print(f"{remove_value} not found")

        case "7" | "ED":

            while True:
                if input("\nAre you sure edit todos (yes-etc) : ") != "yes":
                    system("cls")
                    break

                system("cls")

                # region get edit base
                while True:
                    edit_base = input(
                        "Select remove column (1.title 2..plan_code) : ")
                    system("cls")

                    if edit_base in ["1", "2"]:
                        break

                    print("Error!")
                # endregion

                # region show todos
                print("Sort\tTitle\ttime\tDescription\tPlancode")
                print("______________________________________________")
                for id_, tdo in enumerate(todo_list, 1):
                    print(id_, *tdo, sep="\t")
                print("_______________________________________________")
                # endregion

                # region get search value
                match edit_base:
                    case "1":
                        search_value = input("\nTitle : ")
                        search_index = 0
                    case "2":
                        search_value = input("\nCode : ")
                        search_index = 3
                # endregion
                system("cls")

                for todo in todo_list:
                    if todo[search_index] == search_value:
                        find_todo = todo
                        break
                else:
                    print(f"{search_value} not found")
                    continue

                while True:
                    print("\nFind todo :")
                    print("---------------------")
                    print(f"Title : {find_todo[0]}")
                    print(f"Time : {find_todo[1]}")
                    print(f"Code : {find_todo[3]}")
                    print(f"Status : {find_todo[4]}")
                    print(f"Description : {find_todo[2]}")

                    edit_item = input(
                        "\n1.Title 2.Time 3.Status 4.Desc 5.Exit : ")
                    system("cls")

                    if edit_item == "1":
                        # region newtitle
                        while True:
                            new_title = input('title :')
                            system("cls")

                            if new_title == "":
                                print("error! field is empty")
                                continue

                            if new_title == find_todo[0]:
                                break

                            for todo in todo_list:
                                if todo[0] == new_title:
                                    print(new_title, "exist")
                                    break
                            else:
                                break
                        # endregion
                        find_todo[0] = new_title

                    elif edit_item == "2":
                        # region new time
                        while True:
                            new_time = input("enter your new time :")
                            system("cls")

                            if new_time != "":
                                break

                            print("error! field is empty")
                        # endregion
                        find_todo[1] = new_time

                    elif edit_item == "3":
                        # region new status
                        while True:
                            new_status = input("Status (active - deactive) : ")
                            system("cls")

                            if new_status in ["active", "deactive"]:
                                break

                            print("Error!")
                        # endregion
                        find_todo[4] = new_status

                    elif edit_item == "4":
                        new_description = input("description:")
                        system("cls")
                        find_todo[2] = new_description

                    elif edit_item == "5":
                        break

                    else:
                        print("Error!!!")

        case "8" | "E":
            break

        case _:
            print("Error!")
