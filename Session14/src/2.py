from collections import namedtuple
from os import system
# data = ("meisam", "ilka", "0936", "male")

Contact = namedtuple(typename="Contact", field_names=("name", "family", "phone", "gender"))
contact_list = []



while True:
    print("1. Add contact")
    print("2. Show contact")
    print("3. Exit")
    menu = input("\nName : ")
    system("cls")

    match menu:
        case "1":
            
            # region name
            while True:
                name = input("name : ")

                if name!="":
                    break

                print("Error!!!")
            # endregion

            # region family
            while True:
                family = input("family : ")

                if family!="":
                    break

                print("Error!!!")
            # endregion

            # region phone
            while True:
                phone = input("phone : ")

                if phone!="":
                    break

                print("Error!!!")
            # endregion

            # region gender
            while True:
                gender = input("gender : ")

                if gender in ("male", "female", "other"):
                    break

                print("Error!!!")
            # endregion

            cnt = Contact(name=name, family=family, phone=phone, gender=gender)

            contact_list.append(cnt)

        case "2":
            for cnt in contact_list:
                print("Name :", cnt.name, "Family :", cnt.family, "Phone :", cnt.phone, "Gender :", cnt.gender, )
            


        case "3":
            break
        case _:
            print("Error!!!")









