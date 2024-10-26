from os import system


teacher_list = []


while True:
    print("[A]dd teacher (1):")
    print("[S]how list (2):")
    print("[E]xit(3):")
    menu = input("enter menu num :")
    system("cls")

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

            teacher = [name, family, age, gender]
            teacher_list.append(teacher)

        case "2":
            print("#\tName\tFamily\tage\tgender")
            print("____________________________________________")
            for id_, teacher in enumerate(teacher_list):
                print(id_, *teacher, sep="\t")
                print("____________________________________________")

        case "3":
            break
        
        case _:
            print("Error")
