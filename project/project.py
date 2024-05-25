
from os import system
from random import randint


student_list = []

# region menu
while True:
    print("[A]dd student (1) :")
    print("[S]how student (2) :")
    print("[R]emove student (3) :")
    print("[E]dit student (4) :")
    print("[SE]srch student (5) :")
    print("[AC]ctive student (6) :")
    print("[DE]active student (7) :")
    print("[PHP] best (8) :")
    print("[PY]thon best (9) :")
    print("[AVJ] best (10) :")
    print("[EX]it (11) :")

    menu = input("enter menu num :")
    system("cls")
# endregion

    match menu:
        case "A" | "1":
            while True:
                # region creat code
                while True:
                    plan_code = str(randint(1000, 9999))

                    for student in student_list:
                        if student[12] == plan_code:
                            break
                    else:
                        break
                # endregion

                # region name
                while True:
                    name = input("name :")
                    system("cls")

                    if name == "":
                        print("error! field is empty")
                        continue
                    else:
                        break

                # endregion

                # region family
                while True:
                    family = input("family :")
                    system("cls")

                    if family == "":
                        print("error! field is empty ")
                        continue
                    else:
                        break
                # endregion

                # region gender
                while True:
                    gender = input("gender:(male,female,other) :")
                    system("cls")

                    if gender == "":
                        print("error! field is empty")
                        continue

                    elif gender not in ("male", "female", "other"):
                        print("invalid gender!")
                        continue
                    else:
                        break
                # endregion

                # region age
                while True:
                    age = int(input("age :"))
                    system("cls")

                    if age not in range(7, 50):
                        print("error! out of range")
                        continue
                    else:
                        break
                # endregion

                # region national code
                while True:
                    national_code = input("national code:")

                    if national_code == "":
                        system("cls")
                        print("field is empty")
                        continue

                    for student in student_list:
                        if student[4] == national_code:
                            print(f"{national_code} already exist")
                            break
                    else:
                        break
                # endregion

                # region phone
                while True:
                    phone = input("phone:")
                    system("cls")

                    if national_code == "":
                        print("field is empty")
                        continue

                    for student in student_list:
                        if student[5] == phone:
                            print(f"{phone} already exist")
                            break
                    else:
                        break
                # endregion

                # region address
                address = input("address :")
                system("cls")
                # endregion

                # region class
                while True:
                    class_ = input("class :(A,B,C,D)")
                    system("cls")

                    if class_ == "":
                        print("error! field is empty")
                        continue

                    elif class_ not in ("A", "B", "C", "D"):
                        print("error! invalid class")
                        continue
                    else:
                        break
                # endregion

                # region PHP
                while True:
                    php = int(input("php score :"))
                    system("cls")

                    if php not in range(0, 101):
                        print("error! score not in range")
                        continue
                    else:
                        break
                # endregion

                # region python
                while True:
                    python = int(input("python score :"))
                    system("cls")

                    if python not in range(0, 101):
                        print("error! score not in range")
                        continue
                    else:
                        break
                
                # endregion

                # region description
                description = input("description :")
                # endregion


        case "S" | "2":
            pass

        case "R" | "3":
            pass

        case "E" | "4":
            pass

        case "SE" | "5":
            pass

        case "AC" | "6":
            pass

        case "DE" | "7":
            pass

        case "PHP" | "8":
            pass

        case "PY" | "9":
            pass

        case "AVJ" | "10":
            pass

        case "EX" | "11":
            pass

        case _:
            print("error!")
