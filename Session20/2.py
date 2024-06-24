from copy import deepcopy
from os import system
from random import randint
from time import sleep


todo_list = [
    {"title":"task1", "time":"1400", "description":"", "code":"100000", "status":"active"},
    {"title":"task2", "time":"1400", "description":"", "code":"100001", "status":"active"},
    {"title":"task3", "time":"1400", "description":"", "code":"100002", "status":"deactive"},
    {"title":"task4", "time":"1400", "description":"", "code":"100003", "status":"deactive"},
    {"title":"task5", "time":"1400", "description":"", "code":"100004", "status":"active"},
    {"title":"task6", "time":"1400", "description":"", "code":"100005", "status":"deactive"}
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
                        if todo["code"] == plan_code:
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
                        if todo["title"] == title:
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

                    if status in ("active", "deactive"):
                        break

                    print("Error!")
                # endregion

                todo = {
                    "title":title, 
                    "time":time, 
                    "description":description, 
                    "code":code, 
                    "status":status
                }
                todo_list.append(todo)

                sleep(2.5)
                system("cls")

                if input("Do you want to continue (yes-etc) : ") != "yes":
                    system("cls")
                    break

        case "D" | "2":

            if input("Do you want display all column (yes-etc) : ") == "yes":
                system("cls")
                display_key = ("title", "time",
                                  "description", "code", "status")

            else:
                system("cls")

                display_key = []

                for index, column in enumerate(("title", "time", "description", "code", "status")):

                    if input(f"Do you want to display {column} (yes-etc)? ") == "yes":
                        display_key.append(column)

                    system("cls")


            print("Sort", *display_key, sep="\t")
            print("______________________________________________")

            for id_, tdo in enumerate(todo_list, 1):
                print(id_, *[todo[key]  for key in display_key], sep="\t")

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

                if search_menu in ("1", "C", "2", "T", "3", "TI", "4", "S", "5", "E"):
                    break

                print("Error!!")
            # endregion

            if search_menu in ["5", "E"]:
                continue

            value = input("Search value : ")
            system("cls")

            match search_menu:
                case "1" | "C":
                    search_key = "code"
                case "2" | "T":
                    search_key = "title"
                case "3" | "TI":
                    search_key = "time"
                case "4" | "S":
                    search_key = "status"

            for todo in todo_list:
                if todo[search_key] == value:
                    print(*todo, sep="\t")

        case "AC" | "4":

            while True:

                # region display deactive todo
                print(
                    "\n\n------------------------------------------------------------------------")

                for todo in todo_list:
                    if todo["status"] == "deactive":
                        print(f"Title : {todo["title"]}, Time : {todo["time"]}, Description : {
                              todo["description"]}, code : {todo["code"]}, Status : {todo["status"]}")

                print(
                    "------------------------------------------------------------------------")
                # endregion

                code = input("code (exit): ")
                system("cls")

                if code == "exit":
                    break

                for todo in todo_list:
                    if todo["code"] == code:
                        todo["status"] = "active"
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
                    if todo["status"] == "active":
                        print(f"Title : {todo["title"]}, Time : {todo["time"]}, Description : {
                              todo["description"]}, code : {todo["code"]}, Status : {todo["status"]}")

                print(
                    "------------------------------------------------------------------------")
                # endregion

                code = input("code (exit): ")
                system("cls")

                if code == "exit":
                    break

                for todo in todo_list:
                    if todo["code"] == code:
                        todo["status"] = "deactive"
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
                    print(id_, todo["title"], todo["time"], todo["description"], todo["code"], sep="\t")
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

                        if remove_column in ("1", "2", "3", "4"):
                            break

                        print("Error!")
                    # endregion

                    # region set remove index
                    match remove_column:
                        case "1":
                            remove_key = "title"
                        case "2":
                            remove_key = "time"
                        case "3":
                            remove_key = "code"
                        case "4":
                            remove_key = "status"
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
                        if todo[remove_key] == remove_value:
                            check_find = True
                            print(f"Title :{todo['title']}, Time :{todo['time']}, Code :{
                                  todo['code']}, Status :{todo['status']}")

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

                    if edit_base in ("1", "2"):
                        break

                    print("Error!")
                # endregion

                # region show todos
                print("Sort\tTitle\ttime\tDescription\tPlancode")
                print("______________________________________________")
                for id_, tdo in enumerate(todo_list, 1):
                    print(id_, tdo["title"], tdo["time"], tdo["description"], tdo["code"], sep="\t")
                print("_______________________________________________")
                # endregion

                # region get search value
                match edit_base:
                    case "1":
                        search_value = input("\nTitle : ")
                        search_key = "title"
                    case "2":
                        search_value = input("\nCode : ")
                        search_key = "code" 
                # endregion
                system("cls")

                for todo in todo_list:
                    if todo[search_key] == search_value:
                        find_todo = todo
                        break
                else:
                    print(f"{search_value} not found")
                    continue

                while True:
                    print("\nFind todo :")
                    print("---------------------")
                    print(f"Title : {find_todo["title"]}")
                    print(f"Time : {find_todo["time"]}")
                    print(f"Code : {find_todo["code"]}")
                    print(f"Status : {find_todo["status"]}")
                    print(f"Description : {find_todo["description"]}")

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

                            if new_title == find_todo["title"]:
                                break

                            for todo in todo_list:
                                if todo["title"] == new_title:
                                    print(new_title, "exist")
                                    break
                            else:
                                break
                        # endregion
                        find_todo["title"] = new_title

                    elif edit_item == "2":
                        # region new time
                        while True:
                            new_time = input("enter your new time :")
                            system("cls")

                            if new_time != "":
                                break

                            print("error! field is empty")
                        # endregion
                        find_todo["time"] = new_time

                    elif edit_item == "3":
                        # region new status
                        while True:
                            new_status = input("Status (active - deactive) : ")
                            system("cls")

                            if new_status in ("active", "deactive"):
                                break

                            print("Error!")
                        # endregion
                        find_todo["status"] = new_status

                    elif edit_item == "4":
                        new_description = input("description:")
                        system("cls")
                        find_todo["description"] = new_description

                    elif edit_item == "5":
                        break

                    else:
                        print("Error!!!")

        case "8" | "E":
            break

        case _:
            print("Error!")
