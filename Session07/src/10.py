from os import system


student_number = 3
student_list = [None] * (student_number*6)


for index in range(student_number):

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

    student_list[(index*6) + 0] = name
    student_list[(index*6) + 1] = family
    student_list[(index*6) + 2] = age
    student_list[(index*6) + 3] = gender
    student_list[(index*6) + 4] = class_
    student_list[(index*6) + 5] = adress

print("name family  age gender  class   adrdress")
for index in range(len(student_list)):

    if index % 6 == 0:
        print()

    print(student_list[index], end="\t")
