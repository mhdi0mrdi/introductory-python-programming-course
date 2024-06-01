
from os import system
from random import randint
from time import sleep


student_list = []

while True:
    # region menu
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
                    student_code = str(randint(1000, 9999))

                    for student in student_list:
                        if student[12] == student_code:
                            break
                    else:
                        break
                # endregion

                # region name
                while True:
                    name = input("name :")
                    system("cls")

                    if name == "":
                        break

                    print("error! field is empty")

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
                    php = float(input("php score :"))
                    system("cls")

                    if 0 <= php <= 100:
                        break

                    print("error! score not in range")
                # endregion

                # region python
                while True:
                    python = float(input("python score :"))
                    system("cls")

                    if 0 <= python <= 100:
                        break

                    print("error! score not in range")
                # endregion

                # region description
                description = input("description :")
                system('cls')
                # endregion

                student = [name, family, gender, age, national_code, phone,
                           address, class_, php, python, description, student_code]
                student_list.append(student)

                sleep(2)
                system("cls")

                if input("Do you want to continue (yes-etc) : ") != "yes":
                    system("cls")
                    break

        case "S" | "2":

            for student in student_list:
                print(f"fullname : {student[0]} {
                      student[1]} - age : {student[3]}")
                print(f"gender :, {student[2]} - phone : {student[5]} ")
                print(f"nationalcode : {student[4]} - stdcode : {student[11]}")
                print(f"address : {student[6]}")
                print(f"class : {student[7]}")
                print(f"description : {student[10]}")
                print(
                    f"php : {student[8]} - python : {student[9]}", end="\n\n\n")

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
