from copy import deepcopy
from os import system
from random import randint
from time import sleep

student_list = []


while True:
    print("[A]dd student (1):")
    print("[S]how list (2):")
    print("[SE]arch (3):")
    print("[AC]cept student (4):")
    print("[R]eject student (5):")
    print("[RE]move student (6):")
    print("[ED] it student (7):")
    print("[E]xit (8):")
    menu = input("enter menu num :")
    system("cls")

    match menu:
        case "A" | "1":
            # region create code
            while True:
                student_code = str(randint(1000, 9999))

                for stu in student_list:
                    if student[6] == student_code:
                        break
                    else:
                        break
            # endregion

                # region get name
                while True:
                    name = input('name :')
                    system("cls")

                    if name != "":
                        break

                    print("error")
                # endregion

                # region get family
                while True:
                    family = input('family:')
                    system("cls")

                    if family != "":
                        break

                    print("error")
                # endregion

                # region get age
                while True:
                    age = int(input('age :'))
                    system("cls")

                    if name not in range(18, 121):
                        break

                    print("error")
                # endregion

                # region get gender
                while True:
                    gender = input('gender:')
                    system("cls")

                    if gender in ("male", "female , other"):
                        break
                    elif gender == "":
                        print("error! gender is empty")
                    else:
                        print("error! gender does not in valid range")
                # endregion

                # region get class
                while True:
                    class_ = input("enter your class")
                    system("cls")

                    if class_ in ("a", "b", "c"):
                        break
                    elif class_ == "":
                        print("error! class is empty")
                    else:
                        print("error! unvalid class")
                # endregion

                # region get phone
                while True:
                    phone = input("phone number:")
                    system("cls")

                    if phone != "":
                        break

                    print("error")
                # endregion

                # region status
                while True:
                    status = input("status (accepted-rejected)")
                    system("cls")

                    if status in ["accepted-rejected"]:
                        break

                    print("Error!")

                # endregion

                student = [name, family, age, gender,
                           class_, phone, student_code, status]
                student_list.append(student)

        case "S" | "2":

            print("name\tfamily\tage\tgender\tclass\tphone\tstudent code\tstatus")
            print("---------------------------------------------------")
            for id_, std in enumerate(student_list):
                print(id_, *std, sep="\t")
            print("---------------------------------------------------")

        case "SE" | "3":
            # region search
            while True:
                print("[N]ame (1):")
                print("[F]amily (2):")
                print("[G]ender (3):")
                print("[CL]ass (4):")
                print("[PH]one (5):")
                print("[A]ge (6):")
                print("[S]tatus (7):")
                print("[C]ode (8):")
                print("[E]xit (9) :")
                search = input(" search :")
                system("cls")

                if search in ["N", "F", "G", "CL", "PH", "E", "A", "S", "C" "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    break

                print("error!")
            # endregion

            if search in ["9", "E"]:
                continue

            value = input("search value :")
            system("cls")

            match search:
                case "1" | "N":
                    search_index = 0
                case "2" | "F":
                    search_index = 1
                case "3" | "G":
                    search_index = 3
                case "4" | "C":
                    search_index = 4
                case "5" | "PH":
                    search_index = 5
                case "6" | "A":
                    search_index = 2
                case "7" | "S":
                    search_index = 7
                case "8" | "C":
                    search_index = 6

            for student in student_list:
                if student[search_index] == value:
                    print(*student, sep="\t")

        case "AC" | "4":

            while True:
                # region display rejected students
                print("\n\n------------------------------------------------------")

                for stu in student_list:
                    if student[7] == "rejected":
                        print(f"name : {student[0]}, familly : {student[1]} ,age : {student[2]}, gender : {student[3]},class : {
                              student[4]},phone : {student[5]},student code : {student[6]},status : {student[7]},")
                print("\n\n------------------------------------------------------")
                # endregion

                code = input("code(exit): ")
                system("cls")

                if code == "exit":
                    break

                for student in student_list:
                    if student[6] == code:
                        student[7] = "accepted"
                        break
                else:
                    print(code, "does noy exis")

        case "R" | "5":

            while True:
                # region display accepted students
                print("\n\n------------------------------------------------------")

                for stu in student_list:
                    if student[7] == "rejected":
                        print(f"name : {student[0]}, familly : {student[1]} ,age : {student[2]}, gender : {student[3]},class : {
                              student[4]},phone : {student[5]},student code : {student[6]},status : {student[7]},")
                print("\n\n------------------------------------------------------")
                # endregion

                code = input("code(exit): ")
                system("cls")

                if code == "exit":
                    break

                for student in student_list:
                    if student[6] == code:
                        student[7] = "rejected"
                        break
                else:
                    print(code, "does not exis")

        case "RE" | "6":

            while True:
                if input("Are you sure deelete students (yes-etc) : ") != "yes":
                    system("cls")
                    break

                system("cls")

                # region show students
                print(
                    "Sort\tName\tfamily\tage\tgender\tclass\tphone\tstudent code\tstatus")
                print("______________________________________________")
                for id_, stud in enumerate(student_list, 1):
                    print(id_, *stud, sep="\t")
                print("_______________________________________________")
                # endregion

                if input("\n\nDo you want to remove all students (yes, etc) ? ") == "yes":
                    system("cls")
                    student_list.clear()
                    print("Done!")
                    break

                else:
                    system("cls")

                    # region get remove column
                    while True:
                        remove_column = input(
                            "Select remove column (1.Name 2.family 3.age 4.gender 5.class 6.phone 7.studentcode 8.status) : ")
                        system("cls")

                        if remove_column in ["1", "2", "3", "4", "5", "6", "7", "8"]:
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
                            remove_index = 2
                        case "4":
                            remove_index = 3
                        case "5":
                            remove_index = 4
                        case "6":
                            remove_index = 5
                        case "7":
                            remove_index = 6
                        case "8":
                            remove_index = 7
                    # endregion

                    # region show students
                    print(
                        "Sort\tName\tfamily\tage\tgender\tclass\tphone\tstudent code\tstatus")
                    print("______________________________________________")
                    for id_, stud in enumerate(student_list, 1):
                        print(id_, *stud, sep="\t")
                    print("_______________________________________________")
                    # endregion
                    remove_value = input("remove value : ")
                    system("cls")
                    check_find = False

                    for student in deepcopy(student_list):
                        if student[remove_index] == remove_value:
                            check_find = True
                            print(f"name :{student[0]}, family :{student[1]}, age :{
                                  student[2]}, gender :{student[3]},class_ :{student[4]},phone :{student[5]},student code :{student[6]},status :{student[7]},")

                            if input("Are you sure delete this student (yes-etc) : ") == "yes":
                                system("cls")
                                student_list.remove(student)
                                print("Done!!!")
                            else:
                                system("cls")

                    if not check_find:
                        print(f"{remove_value} not found")

        case "ED" | "7":
            

        case "E" | "8":
            break

        case _:
            print("Error!")
