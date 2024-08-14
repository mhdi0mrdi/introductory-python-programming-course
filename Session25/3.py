
# type hint
from os import system
from typing import Iterable


def get_input(field: str = "input", required: bool = True, valid_items: Iterable = ()):
    err_msg = list()


    while True:
        data = input(f"{field} : ")
        system("cls")

        if required and  data == "":
            err_msg.append(f"{field} is empty")

        if valid_items and data not in valid_items:
            err_msg.append(f"{field} not in valid range")

        if not err_msg:
            return data
        
        print(*err_msg, sep="\n")
        err_msg.clear()





# gender = get_input("gender", valid_items=("male", "female", "other"))
time = get_input("time", valid_items=(2024,2025,2026))



# data = get_input()
# name = get_input("Name")
# family = get_input("Family")
# phone = get_input("Phone number")
# description = get_input("Description", required=False)

# print("Your fullname : ", name, family)
# print("Phone : ", phone)
# print("Description : ", description)
