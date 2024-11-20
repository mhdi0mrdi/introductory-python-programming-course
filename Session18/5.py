

from random import randint


teacher_list = []


print("add teacher (1) :")

menu = input("menu :")

while True:
    match menu:

        case 1:
            # region code
            while True:
                id = randint(1000, 9999)

                for teacher in teacher_list:
                    if id == teacher["id"]:
                        break
                else:
                    break
            # endregion

            # region id
            while True:
                code = int(input("code :"))

                for teacher in teacher_list:
                    if code == teacher["code"]:
                        print("error")
                        break
                else:
                    break
            # endregion

            # region name
            while True:
                name = input("name :")

                if name != "":
                    break
                print("error")
            # endregion

            # region family
            while True:
                family = input("family :")

                if family != "":
                    break
                print("error")
            # endregion

            # region age
            while True:
                age = int(input("age :"))

                if age not in range(1, 121):
                    print("age not in range!")
                    break

                print("Error!")
            # endregion

            # region gender
            while True:
                gender = input("gender :")

                if gender not in ("male", "female", "other"):
                    print("gender not in range!")
                    break

                if gender == "":
                    print("error field is empty!")
                else:
                    print("error!")
            # endregion

            teacher = {"name": name, "family": family,
                       "age": age, "gender": gender, "code": code}
            teacher_list.append(teacher)

        case 2:
            print("________________________________")

            for teacher in teacher_list:
                print(*teacher)

            print("__________________________________")

        case 3:
            while True:
                # region show
                print("________________________________")

                for teacher in teacher_list:
                    print(*teacher)

                print("__________________________________")
                # endregion

                # region remove value
                while True:
                    remove_column = input("remove value (code, id) :")

                    if remove_column in ("code", "id"):
                        break
                    print("error")
                # endregion

                # region show
                print("________________________________")

                for teacher in teacher_list:
                    print(*teacher)

                print("__________________________________")
                # endregion

                match remove_column:
                    case 1:
                        value = int(input("code :"))

                    case 2:
                        value = int(input("id :"))

                for teacher in teacher_list:
                    if value == teacher[remove_column]:
                        teacher_list.remove(teacher)

        case 4:
            # region search column
            while True:
                search_column: input(
                    "search value : (name, family, age, gender) :")
                
                if remove_column in ("name" , "family" , "age" , "gender"):
                        break
                print("error")
            # endregion

                match search_column:
                    case "name":
                        value = input("name :")
                    case "family":
                        value = input("family :")
                    case "age":
                        value = int(input("age :"))                        
                    case "gender":
                        value = input("gender :")

                for teacher in teacher_list:
                    if value == teacher[search_column]:
                        print(*teacher)

edit