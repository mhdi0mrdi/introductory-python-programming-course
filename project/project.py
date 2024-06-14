
from copy import deepcopy
from os import system
from random import randint
from time import sleep


student_list = [["mahdi", "moradi", "male", "19", "0110523555", "09022333616",
                           "tehran", "A", "89", "76", "moz", "1001", "active"],
                           ["negar", "davoudi", "female", "22", "05432445643", "09051202401",
                           "abazar", "B", "76", "45", "hichi", "1002", "deactive"],
                           ["bahar", "davoudi", "female", "22", "05432445643", "09051287889",
                           "iran", "C", "99", "78", "hichiz", "1003", "deactive"],
                           ["soheil", "ezazi", "male", "18", "0577879090", "09051888900",
                           "marzdaran", "D", "34", "15", "hichiii", "1003", "active"]]
php_list = []
python_list = []

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
    print("[EX]it (10) :")

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
                        if student[11] == student_code:
                            break
                    else:
                        break
                # endregion

                # region name
                while True:
                    name = input("name :")
                    system("cls")

                    if name != "":
                        break
                    else:
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
                    national_code = input("national code :")
                    system("cls")

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
                    phone = input("phone :")
                    system("cls")

                    if phone == "":
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
                    class_ = input("class (A,B,C,D) :")
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

                    if 0 <= php <= 100:
                        break

                    print("error! score not in range")
                # endregion

                # region python
                while True:
                    python = int(input("python score :"))
                    system("cls")

                    if 0 <= python <= 100:
                        break

                    print("error! score not in range")
                # endregion

                # region description
                description = input("description :")
                system('cls')
                # endregion

                # region status
                while True:
                    status = input("Status (active - deactive) : ")
                    system("cls")

                    if status in ["active", "deactive"]:
                        break

                    print("Error!")
                # endregion

                student = [name, family, gender, age, national_code, phone,
                           address, class_, php, python, description, student_code, status]
                student_list.append(student)

                system("cls")
                sleep(2)

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
                    f"php : {student[8]} - python : {student[9]}")
                print(f"status : {student[12]}" "end=\n\n\n")

            display_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

            if input("press enter to continue :") == "":
                system('cls')
                continue

        case "R" | "3":
            while True:
                if input("Are you sure delete all students? (yes,etc) :") == "yes":
                    system("cls")
                    student_list.clear()
                    print("done!")
                    sleep(2)
                    system('cls')
                    break
                else:
                    system('cls')
                    

                # region show students
                for student in student_list:
                    print(f"fullname : {student[0]} {
                        student[1]} - age : {student[3]}")
                    print(f"gender :, {student[2]} - phone : {student[5]} ")
                    print(f"nationalcode : {student[4]} - stdcode : {student[11]}")
                    print(f"address : {student[6]}")
                    print(f"class : {student[7]}")
                    print(f"description : {student[10]}")
                    print(
                        f"php : {student[8]} - python : {student[9]}")
                    print(f"status : {student[12]}" "end=\n\n\n")
                # endregion
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
                            remove_index = 7
                        case "7":
                            remove_index = 11

                        # endregion

                    remove_value = input("remove value :")
                    system("cls")
                    check_find = False

                    for student in deepcopy(student_list):
                        if student[student_list] == remove_value:
                            check_find = True
                            print(f"fullname : {student[0]} {
                                student[1]} - age : {student[3]}")
                            print(f"gender :, {
                                  student[2]} - phone : {student[5]} ")
                            print(f"nationalcode : {
                                  student[4]} - stdcode : {student[11]}")
                            print(f"address : {student[6]}")
                            print(f"class : {student[7]}")
                            print(f"description : {student[10]}")
                            print(
                                f"php : {student[8]} - python : {student[9]}", end="\n\n\n")
                            print(f"status : {student[12]}")

                            if input("Are you sure delete this student (yes-etc) : ") == "yes":
                                system("cls")
                                student_list.remove(student)
                                print("Done!!!")
                            else:
                                system("cls")

                    # if check_find == False:
                    if not check_find:
                        print(f"{remove_value} not found")

        case "E" | "4":
            while True:
                if input("\nAre you sure edit syudents (yes-etc) : ") != "yes":
                    system("cls")
                    break

                system("cls")

                # region get edit base
                while True:
                    edit_base = input(
                        "Select remove column (1.national code 2.phone 3.student code) : ")
                    system("cls")

                    if edit_base in ["1", "2", "3"]:
                        break

                    print("Error!")
                # endregion

                # region show students
                print(f"fullname : {student[0]} {
                      student[1]} - age : {student[3]}")
                print(f"gender :, {student[2]} - phone : {student[5]} ")
                print(f"nationalcode : {student[4]} - stdcode : {student[11]}")
                print(f"address : {student[6]}")
                print(f"class : {student[7]}")
                print(f"description : {student[10]}")
                print(
                    f"php : {student[8]} - python : {student[9]}", end="\n\n\n")
                print(f"status : {student[12]}")
                # endregion

                # region get search value
                match edit_base:
                    case "1":
                        search_value = input("\nnational code ")
                        search_index = 4
                    case "2":
                        search_value = input("\nphone :")
                        search_index = 5
                    case "2":
                        search_value = input("\nstudent code :")
                        search_index = 11
                # endregion
                system('cls')

                for student in student_list:
                    if student[search_index] == search_value:
                        find_student = student
                        break
                else:
                    print(f"{search_value} not found")
                    continue

                while True:
                    print("\nFind student :")
                    print("-----------------------------")
                    print(f"name : {find_student[0]}")
                    print(f"family : {find_student[1]}")
                    print(f"gender : {find_student[2]}")
                    print(f"age : {find_student[3]}")
                    print(f"national code : {find_student[4]}")
                    print(f"phone : {find_student[5]}")
                    print(f"address : {find_student[6]}")
                    print(f"class : {find_student[7]}")
                    print(f"php : {find_student[8]}")
                    print(f"python : {find_student[9]}")
                    print(f"description : {find_student[10]}")
                    print(f"student code : {find_student[11]}")
                    print(f"status : {find_student[12]}")
                    edit_item = input(
                        "\n1.name 2.family 3.gender 4.age 5.national code 6.phone 7.address 8.class 9.php 10.python 11.description 12.status 13.Exit : ")
                    system("cls")

                    if edit_item == "1":
                        # region new name
                        while True:
                            new_name = input('name :')
                            system("cls")

                            if new_name == "":
                                print("error! field is empty")
                                continue

                            if new_name == find_student[0]:
                                break

                            for student in student_list:
                                if student[0] == new_name:
                                    print(new_name, "exist")
                                    break
                            else:
                                break
                        # endregion
                        find_student[0] = new_name

                    elif edit_item == "2":
                        # region new family
                        while True:
                            new_family = input('family :')
                            system("cls")

                            if new_family == "":
                                print("error! field is empty")
                                continue

                            if new_family == find_student[1]:
                                break

                            for student in student_list:
                                if student[1] == new_family:
                                    print(new_family, "exist")
                                    break
                            else:
                                break
                            # endregion
                        find_student[1] = new_family

                    elif edit_item == "3":
                        # region gender
                        while True:
                            new_gender = input('gender :')
                            system("cls")

                            if new_gender == "":
                                print("error! field is empty")
                                continue

                            if gender not in ("male", "female", "other"):
                                print("invalid gender!")
                                continue

                            if new_gender == find_student[2]:
                                break

                            for student in student_list:
                                if student[2] == new_gender:
                                    print(new_gender, "exist")
                                    break
                            else:
                                break
                            # endregion
                        find_student[2] = new_gender

                    elif edit_item == "4":
                        # region new age
                        new_age = int(input("age :"))
                        system("cls")

                        if age not in range(7, 50):
                            print("error! out of range")
                            continue

                        system("cls")
                        # endregion
                        find_student[3] = new_age

                    elif edit_item == "5":
                        # region new national code
                        while True:
                            new_national_code = input("national code:")
                            system("cls")

                            if new_national_code == "":
                                system("cls")
                                print("field is empty")
                                continue

                            for student in student_list:
                                if student[4] == new_national_code:
                                    print(f"{new_national_code} already exist")
                                    break
                            else:
                                break
                        # endregion
                        find_student[4] = new_national_code

                    elif edit_item == "6":
                        # region new phone
                        while True:
                            new_phone = input("phone :")
                            system("cls")

                            if new_phone == "":
                                print("field is empty")
                                continue

                            for student in student_list:
                                if student[5] == new_phone:
                                    print(f"{new_phone} already exist")
                                    break
                            else:
                                break
                        # endregion
                        find_student[5] = new_phone

                    elif edit_item == "7":
                        # region new address
                        new_address = input("address :")
                        system("cls")
                        # endregion
                        find_student[6] = new_address

                    elif edit_item == "8":
                        # region new class
                        while True:
                            new_class_ = input("class :(A,B,C,D)")
                            system("cls")

                            if new_class_ == "":
                                print("error! field is empty")
                                continue

                            elif new_class_ not in ("A", "B", "C", "D"):
                                print("error! invalid class")
                                continue
                            else:
                                break
                        # endregion
                        find_student[7] = new_class_

                    elif edit_item == "9":
                        # region new php
                        while True:
                            new_php = float(input("php score :"))
                            system("cls")

                            if 0 <= new_php <= 100:
                                break

                            print("error! score not in range")
                        # endregion
                        find_student[8] = new_php

                    elif edit_item == "10":
                        # region new python
                        while True:
                            new_python = float(input("python score :"))
                            system("cls")

                            if 0 <= new_python <= 100:
                                break

                            print("error! score not in range")
                        # endregion
                        find_student[9] = new_python

                    elif edit_item == "11":
                        # region new description
                        new_description = input("description :")
                        system('cls')
                        # endregion
                        find_student[10] = new_description

                    elif edit_item == "12":
                        # region new status
                        while True:
                            new_status = input("Status (active - deactive) : ")
                            system("cls")

                            if new_status in ["active", "deactive"]:
                                break

                            print("Error!")
                        # endregion
                        find_student[11] = new_status

                    elif edit_item == "13":
                        break

                    else:
                        print("error!!!")

        case "SE" | "5":
            # region set search menu
            while True:
                print(f"[N]ame (1)")
                print(f"[F]amily (2)")
                print(f"[G]ender (3)")
                print(f"[A]ge (4)")
                print(f"[NA]tional code (5)")
                print(f"[P]hone : (6)")
                print(f"[S]tudent code (7)")
                print(f"[C]lass (8)")
                print(f"[PHP] (9)")
                print(f"[PY]thon (10)")
                print("[E]xit (11)")
                search_menu = input("search item :")
                system('cls')

                if search_menu in ["1", "N", "2", "F", "3", "G", "4", "A",
                                   "5", "NA", "6", "P", "7", "S", "8", "C", "9",
                                   "PHP", "10", "PY", "11", "E"]:
                    break

                print("error!!!")
            # endregion

            if search_menu in ["11", "E"]:
                continue
            
            value = input("Search value : ")
            system("cls")

            match search_menu:
                case "1" | "N":
                    search_index = 0
                case "2" | "F":
                    search_index = 1
                case "3" | "G":
                    search_index = 2
                case "4" | "A":
                    search_index = 3
                case "5" | "NA":
                    search_index = 4
                case "6" | "P":
                    search_index = 5
                case "7" | "S":
                    search_index = 11
                case "8" | "C":
                    search_index = 7
                case "9" | "PHP":
                    search_index = 8
                case "10" | "PY":
                    search_index = 9

            for student in student_list:
                if student[search_index] == value:
                    system('cls')
                    print(f"fullname : {student[0]} {
                      student[1]} - age : {student[3]}")
                    print(f"gender :, {student[2]} - phone : {student[5]} ")
                    print(f"nationalcode : {student[4]} - stdcode : {student[11]}")
                    print(f"address : {student[6]}")
                    print(f"class : {student[7]}")
                    print(f"description : {student[10]}")
                    print(
                        f"php : {student[8]} - python : {student[9]}")
                    print(f"status : {student[12]}" "end=\n\n\n")
                    if input("press enter to continue :") == "":
                        system('cls')
                        break

        case "AC" | "6":
            while True:
                # region show deactivated students
                for student in student_list:
                    if student[12] == "deactive":
                        print(f"fullname : {student[0]} {
                            student[1]} - age : {student[3]}")
                        print(f"gender :, {
                              student[2]} - phone : {student[5]} ")
                        print(f"nationalcode : {
                              student[4]} - stdcode : {student[11]}")
                        print(f"address : {student[6]}")
                        print(f"class : {student[7]}")
                        print(f"description : {student[10]}")
                        print(
                            f"php : {student[8]} - python : {student[9]}")
                        print(f"status : {student[12]}", end="\n\n\n")
                # endregion

                print("1.national code 2.phone 3.code 4.exit")
                active_menu = input("enter active menu :")
                system("cls")

                if active_menu == "4":
                    break

                match active_menu:
                    case "1":
                        nationalcode = input("national code (exit): ")
                        system("cls")

                        if active_menu == "exit":
                            break

                        for student in student_list:
                            if student[4] == nationalcode:
                                student[12] = "active"
                                break
                        else:
                            print(nationalcode, "does not exist")

                    case "2":
                        phonee = input("phone (exit): ")
                        system("cls")

                        if phonee == "exit":
                            break

                        for student in student_list:
                            if student[5] == phonee:
                                student[12] = "active"
                                break
                        else:
                            print(phonee, "does not exist")

                    case "3":
                        code = input("code (exit):")
                        system("cls")

                        if code == "exit":
                            break

                        for student in student_list:
                            if student[11] == code:
                                student[12] = "active"
                                break
                        else:
                            print(code, "does not exist")

        case "DE" | "7":
            while True:
                # region show activated students
                for student in student_list:
                    if student[12] == "active":
                        print(f"fullname : {student[0]} {
                            student[1]} - age : {student[3]}")
                        print(f"gender :, {
                              student[2]} - phone : {student[5]} ")
                        print(f"nationalcode : {
                              student[4]} - stdcode : {student[11]}")
                        print(f"address : {student[6]}")
                        print(f"class : {student[7]}")
                        print(f"description : {student[10]}")
                        print(
                            f"php : {student[8]} - python : {student[9]}")
                        print(f"status : {student[12]}", end="\n\n\n")
                # endregion

                print("1.national code 2.phone 3.code 4.exit")
                deactive_menu = input("enter active menu :")
                system("cls")

                if deactive_menu == "4":
                    break

                match deactive_menu:
                    case "1":
                        nationalcode = input("national code (exit): ")
                        system("cls")

                        if nationalcode == "exit":
                            break

                        for student in student_list:
                            if student[4] == nationalcode:
                                student[12] = "deactive"
                                break
                        else:
                            print(nationalcode, "does not exist")

                    case "2":
                        phonee = input("phone (exit): ")
                        system("cls")

                        if phonee == "exit":
                            break

                        for student in student_list:
                            if student[5] == phonee:
                                student[12] = "deactive"
                                break
                        else:
                            print(phonee, "does not exist")

                    case "3":
                        code = input("code (exit):")
                        system("cls")

                        if code == "exit":
                            break

                        for student in student_list:
                            if student[11] == code:
                                student[12] = "deactive"
                                break
                        else:
                            print(code, "does not exist")

        case "PHP" | "8":
            while True:
                for student in student_list:
                    php_list.append(student[8])
                    system('cls')
                
                print(f"the best php score is {max(php_list)}")

                if input("press enter to continue :") == "":
                        system('cls')
                        break

        case "PY" | "9":
            while True:
                for student in student_list:
                    python_list.append(student[9])
                    system('cls')

                    print(f"the best python score is {max(python_list)}")
                    
                    if input("press enter to continue :") == "":
                        system('cls')
                        break


        case "EX" | "10":
            break

        case _:
            print("error!")
