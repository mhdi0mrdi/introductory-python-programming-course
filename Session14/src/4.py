from collections import namedtuple
from os import system

Todo = namedtuple('Todo', ["title", "time", "active",
                  "description"], defaults=("", "", "", ""))
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

                if title != "":
                    break

                print("error!")
            # endregion

            # region time
            while True:
                time = input("time :")

                if title != "":
                    break

                print("error!")
            # endregion

            # region active
            while True:
                active = input("active or deactive :")

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

            todo = Todo(title=title, time=time, active=active,
                        description=description)
            todo_list.append(todo)

        case "2":
            inst: Todo
            for inst in todo_list:
                print("title :", inst.title, "time :", inst.time,
                      "active :", inst.active, "description :", inst.description)

        case "3":
            pass
