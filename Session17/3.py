from os import system


student_list = []


while True:

    menu = input("....")

    match menu:
        case "1":

            # region name
            while True:
                name = input("name :")
                system('cls')

                if name != "":
                    break

                print("field is empty")
            # endregion

            # region family
            while True:
                family = input("family :")
                system('cls')

                if family != "":
                    break

                print("field is empty")
            # endregion

            # region gender
            while True:
                gender = input("gender :")
                system('cls')

                if gender in ("male", "female", "other"):
                    break

                if gender == "":
                    print("field is empty")
                else:
                    print(f"{gender} not in male,female,other")
            # endregion

            # region age
            while True:
                age = int(input("age :"))
                system('cls')

                if age in range(1, 121):
                    break

                print("error!!!!!!!")
            # endregion

            # region national code
            while True:
                national_code = input("national code :")
                system('cls')

                if national_code == "":
                    print("field is empty")
                    continue

                for student in student_list:
                    if national_code == student["nationalcode"]:
                        print("national code already exist")
                        break
                else:
                    break
            # endregion

            # region phone
            while True:
                phone = input("phone :")
                system('cls')

                if phone == "":
                    print("field is empty")
                    continue

                for student in student_list:
                    if phone == student["phone"]:
                        print("phone already exist")
                        break
                else:
                    break
            # endregion

            # region address
            address = input("address :")
            system('cls')
            # endregion

            # region class
            while True:
                class_ = input("class :")
                system('cls')

                if class_ in ("A", "B", "C", "D"):
                    break

                if class_ == "":
                    print("field is empty")

                else:
                    print("field not in A B C D")

            # endregion

            # region php
            while True:
                php = float(input("php score:"))
                system('cls')

                if 0 <= php <= 100:
                    break

                print("error php not in range")
            # endregion

            # region python
            while True:
                python = float(input("python score:"))
                system('cls')

                if 0 <= python <= 100:
                    break

                print("error python not in range")
            # endregion

            # region description
            description = input("description :")
            system('cls')
            # endregion

            # region student code
            while True:
                student_code = input("code :")
                system('cls')

                if student_code == "":
                    print("field is empty")
                    continue

                for student in student_list:
                    if student_code == student["stdcode"]:
                        print(f"error !{student_code} slready exist!!")
                        break

                else:
                    break
            # endregion

            student = {"name": name, "family": family, "gender": gender, "age": age,
                       "nationalcode": national_code, "studentcode": student_code, "phone": phone,
                       "class": class_, "php": php, "python": python, "address": address,
                       "description": description}

            student_list.append(student)
