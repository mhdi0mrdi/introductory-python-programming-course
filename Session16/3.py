person_list = []


for _ in range(20):

    # region get name
    while True:

        name = input("name :")

        if name != "":
            break

        print("Error")
    # endregion

    # region family
    while True:

        family = input("family :")

        if family != "":
            break

        print("Error")
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

    person = {"name": name, "family": family, "age": age, "gender": gender}
    person_list.append(person)



