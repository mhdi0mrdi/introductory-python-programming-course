# name
# family
# age
# gender
# class_
# item
# phone

from os import system


student_list = []


while True:
    print("[A]dd student (1):")
    print("[S]how list (2):")
    print("[E]xit(3):")
    menu = input("enter menu num :")

    match menu:
        case "A" | "1":
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

            student = [name, family, age, gender, class_, phone]
            student_list.append(student)

        case "B" | "2":
            