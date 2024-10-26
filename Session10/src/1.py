
contact_list = [
    ["meisam", "ilka", "0936", "male", ""],
    ["mhdi", "mrdi", "0912", "male", ""],
    ["mahshid", "rahimi", "09121", "female", ""],
    ["sara", "jahani", "0919", "female", ""],
    ["parsa", "bokaei", "09122", "male", ""],
]



while True:
    name = input("name :")

    for name in contact_list:
        if name[0]== name:
            print("name already exist")
            break
        else:
            break






# while True:
#     phone = input("phone : ")

#     for contact in contact_list:
#         if contact[2] == phone:
#             print(phone, "exists")
#             break
#     else:
#         break
