
from copy import deepcopy
from os import system
from random import randint
from time import sleep


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

                student = [name, family, gender, age, national_code, phone,
                           address, class_, php, python, description, student_code]
                student_list.append(student)

                sleep(2)
                system("cls")

                if input("Do you want to continue (yes-etc) : ") != "yes":
                    system("cls")
                    break

        case "S" | "2":
            display_colomn = [
                "Full name : ", "Age : ", "Gender : ", "Phone : ", "National code : "
                "Student code : " "Class : ", "Description : ", "PHP : ", "Python : "]

            display_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

            print(display_colomn)

        case "R" | "3":
            if input("Are you sure delete all students? (yes,etc)") != "yes":
                system("cls")
                break

            system("cls")

            # region show atudwnts

            # endregion

            if input("\n\nDo you want to remove all students? (yes,etc)") == "yes":
                system("cls")
                student_list.clear()
                print("done!")
                break

            else:
                system("cls")

                # region set remove index
                while True:
                    remove_colomn = input(
                        "select remove colomn (1.name 2.family 3.gender 4.national code 5.phone 6.class 7.student code) :")
                    system("cls")

                    if remove_colomn in ["1", "2", "3", "4", "5", "6", "7"]:
                        break

                    print("error!")
                # endregion
                match remove_colomn:
                    case "1":
                        remove_index = 0
                    case "2":
                        remove_index = 1
                    case "3":
                        remove_index = 2
                    case "4":
                        remove_index = 4
                    case "5":
                        remove_index = 5
                    case "6":
                        remove_index =7
                    case "7":
                        remove_index = 11
                
                    # region show todos``
                    
                    # endregion

                remove_value = input("remove value :")
                system("cls")
                check_find = False

                for student in deepcopy(student_list):
                    if student[student_list] == remove_value:
                        check_find = True


                        student_list.remove(student)
                        system("cls")
                        

        


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
