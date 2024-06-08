from collections import namedtuple
from os import system
from datetime import  datetime
import calendar


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
                system('cls')

                if title == "":
                    print("error!")
                    continue

                for todo in todo_list:
                    if todo["title"]==title:
                        print(f"Error!!!, {title} exists")
                        break
                else:
                    break
            # endregion

            # region time
            while True:
                cal = calendar.TextCalendar()
                print(cal.formatyear(datetime.now().year))


                time = input("\n\ntime(yy-mm-dd) :")
                system('cls')

                if time != "":
                    break

                print("error!")
            # endregion

            # region status
            while True:
                status = input("active or deactive :")
                system('cls')

                if status in ("active", "deactive"):
                    break

                if status == "":
                    print("error! field is empty")

                else:
                    print("not in active or deactive")
            # endregion

            # region description
            description = input("description :")
            system("cls")
            # endregion

            todo = {
                "title":title,
                "time":time,
                "status":status,
                "description":description
            }

            todo_list.append(todo)

        case "2":
            inst: Todo
            for inst in todo_list:
                print("title :", inst.title, "time :", inst.time,
                      "active :", inst.active, "description :", inst.description)

        case "3":
            pass
