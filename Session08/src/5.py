from os import system


student_list = []


for _ in range(2):

    # region get name
    while True:
        name = input("name : ")
        system("cls")

        if name != "":
            break

        print("Error")
    # endregion

    # region get family
    while True:
        family = input("family : ")
        system("cls")

        if family != "":
            break

        print("Error")
    # endregion

    # region get age
    while True:
        age = int(input("age : "))
        system("cls")

        if age in range(18, 120):
            break

        print("Error")
    # endregion

    # region get gender
    while True:
        gender = input("gender(male,female,other):")
        system("cls")

        if gender in ("male", "female", "other"):
            break
    # endregion

    # region get class
    while True:
        class_ = input("class : ")
        system("cls")

        if class_ in ("a", "b", "c"):
            break
    # endregion

    # region get address
    adress = input("enter your address:")
    system("cls")
    # endregion

    students = [name, family, age, gender, class_, adress]
    student_list.append(students)


print("ID\tName\tFamily\tAge\tGender\tClass\tAdrdress")
print("______________________________________________________")
for id_, students in enumerate(student_list, 1):
    print(id_, *students, sep="\t")
print("______________________________________________________")
