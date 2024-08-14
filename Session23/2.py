
# type hint
from os import system


def get_input(field: str, required: bool):
    
    while True:
        data = input(f"{field} : ")
        system("cls")
        
        if required==True:
            if data == "":
                print(f"{field} is empty")
            else:
                return data
        
        else:
            return data



name = get_input("Name", True)
family = get_input("Family", True)
phone = get_input("Phone number", True)
description = get_input("Description", False)

print("Your fullname : ", name, family)
print("Phone : ", phone)
print("Description : ", description)
