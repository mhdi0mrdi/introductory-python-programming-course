# import package.module
# res = package.module.get_input()



# import package.module as pm
# res = pm.get_input()


# from package.module import *
# res = get_input()



# from package.module import get_input
# from package.module import get_input, print_list_of_dict, search_list_dict
# res = get_input()




# from package.module import get_input as gi1, search_list_dict
# from package.module01 import get_input as gi2


# res = gi1()
# res = gi2()






















# from copy import deepcopy
# from os import system
# from random import randint
# from time import sleep

# script


# todo_list = [
#     {"title": "task1", "time": "1400", "description": "",
#         "code": "100000", "status": "active"},
#     {"title": "task2", "time": "1400", "description": "",
#         "code": "100001", "status": "active"},
#     {"title": "task3", "time": "1400", "description": "",
#         "code": "100002", "status": "deactive"},
#     {"title": "task4", "time": "1400", "description": "",
#         "code": "100003", "status": "deactive"},
#     {"title": "task5", "time": "1400", "description": "",
#         "code": "100004", "status": "active"},
#     {"title": "task6", "time": "1400", "description": "",
#         "code": "100005", "status": "deactive"}
# ]


# while True:

#     menu = get_input(
#         "[A]dd plan (1)\n[D]isplay todo (2)\n[S]earch todo (3)\n\nmenu",
#         valid_items=("1", "2", "3", "4", "5", "6", "7", "8",
#                      "AC", "DE", "R", "ED", "E", "A", "S", "D"),
#         err_msg="Menu"
#     )

#     match menu:
#         case "A" | "1":
#             while True:
#                 # region creat code
#                 while True:
#                     plan_code = str(randint(100000, 999999))
#                     search_res = search_list_dict(todo_list, plan_code, "code") 

#                     if not search_res:
#                         break

#                 # endregion

#                 # region title
#                 while True:
#                     title = get_input(
#                         "Please enter todo title", err_msg="Title")
#                     search_res = search_list_dict(todo_list, title, "title") 

#                     if not search_res:
#                         break
                    
#                     print(title, "exist")
#                 # endregion

#                 todo = {
#                     "title": title,
#                     "time": get_input("Plaese enter todo time", err_msg="Time", valid_items=("1400", "1401", "1402")),
#                     "description": get_input("description", required=False),
#                     "code": plan_code,
#                     "status": get_input("Please enter todo status (active,deactive)", err_msg="Status", valid_items=("active", "deactive"))
#                 }
#                 todo_list.append(todo)

#                 sleep(2.5)
#                 system("cls")

#                 if get_input("Do you want to continue (yes-etc)", valid_items=("yes", "no")) == "no":
#                     break

#         case "D" | "2":

#             if get_input("Do you want display all column (yes-etc)", valid_items=("yes", "no")) == "yes":
#                 display_key = ("title", "time",
#                                "description", "code", "status")

#             else:
#                 display_key = []

#                 for index, column in enumerate(("title", "time", "description", "code", "status")):
#                     if get_input(field=f"Do you want to display {column} (yes-etc)", valid_items=("yes", "no")) == "yes":
#                         display_key.append(column)

#                     system("cls")

#             print_list_of_dict(data=todo_list, keys=display_key)

#         case "3" | "S":
#             while True:
#                 search_menu = get_input(
#                     field="[C]ode (1)\n[T]itle (2)\n[TI]ime (3)\n[S]tatus (4)\n[E]xit (5)\n\nsearch item",
#                     err_msg="Search menu",
#                     valid_items=("1", "C", "2", "T", "3", "TI", "4", "S", "5", "E")
#                 )

#                 if search_menu in ["5", "E"]:
#                     break

#                 value = get_input(field="Search value")

#                 match search_menu:
#                     case "1" | "C":
#                         search_key = "code"
#                     case "2" | "T":
#                         search_key = "title"
#                     case "3" | "TI":
#                         search_key = "time"
#                     case "4" | "S":
#                         search_key = "status"

#                 search_res = search_list_dict(todo_list, value, search_key)
#                 print_list_of_dict(search_res, ("title", "time",
#                                                             "description", "code", "status"))
            
#         case "AC" | "4":

#             while True:
#                 search_res = search_list_dict(todo_list, "deactive", "status")
#                 print_list_of_dict(search_res, ("title", "time",
#                                                          "description", "code", "status"))
                
#                 code = get_input(
#                     field="Please enter todo Code (exit)", err_msg="Code")

#                 if code == "exit":
#                     break

#                 for todo in todo_list:
#                     if todo["code"] == code:
#                         todo["status"] = "active"
#                         break
#                 else:
#                     print(code, "does not exist")

#         case "DE" | "5":
#             # region deactive todo
#             while True:
#                 search_res = search_list_dict(todo_list, "active", "status")
#                 print_list_of_dict(search_res, ("title", "time",
#                                                          "description", "code", "status"))


#                 code = get_input(
#                     "Please enter todo code (exit)", err_msg="Code")

#                 if code == "exit":
#                     break

#                 for todo in todo_list:
#                     if todo["code"] == code:
#                         todo["status"] = "deactive"
#                         break
#                 else:
#                     print(code, "does not exist")
#                 # endregion

#         case "6" | "R":

#             while True:
#                 if get_input("Are you sure delete todos (yes-no)", valid_items=("yes", "no")) == "no":
#                     break

#                 print_list_of_dict(data=todo_list, keys=("title", "time",
#                                                          "description", "code", "status"))

#                 if get_input("\n\nDo you want to remove all todos (yes, no)", valid_items=("yes", "no")) == "yes":
#                     todo_list.clear()
#                     print("Done!")
#                     break

#                 else:

#                     remove_column = get_input(
#                         "Select remove column (1.title 2.time 3.plan_code 4.status)",
#                         valid_items=("1", "2", "3", "4")
#                     )

#                     # region set remove index
#                     match remove_column:
#                         case "1":
#                             remove_key = "title"
#                         case "2":
#                             remove_key = "time"
#                         case "3":
#                             remove_key = "code"
#                         case "4":
#                             remove_key = "status"
#                     # endregion

#                     print_list_of_dict(data=todo_list, keys=("title", "time",
#                                                              "description", "code", "status"))

#                     remove_value = get_input("remove value")
#                     check_find = False

#                     for todo in deepcopy(todo_list):
#                         if todo[remove_key] == remove_value:
#                             check_find = True
#                             print(f"Title :{todo['title']}, Time :{todo['time']}, Code :{
#                                   todo['code']}, Status :{todo['status']}")

#                             if get_input("Are you sure delete this todo (yes-etc)", valid_items=("yes", "no")) == "yes":
#                                 todo_list.remove(todo)
#                                 print("Done!!!")

#                     if not check_find:
#                         print(f"{remove_value} not found")

#         case "7" | "ED":

#             while True:
#                 if get_input("Are you sure edit a todos (yes-no)", valid_items=("yes", "no")) != "yes":
#                     break

#                 edit_base = get_input(
#                     "Select remove column (1.title 2..plan_code)",
#                     valid_items=("1", "2")
#                 )

#                 print_list_of_dict(data=todo_list, keys=("title", "time",
#                                                          "description", "code", "status"))

#                 # region get search value
#                 match edit_base:
#                     case "1":
#                         search_value = get_input(
#                             "Please enter todo Title", err_msg="Title")
#                         search_key = "title"
#                     case "2":
#                         search_value = get_input(
#                             "Please enter todo code", err_msg="Code")
#                         search_key = "code"
#                 # endregion

#                 for todo in todo_list:
#                     if todo[search_key] == search_value:
#                         find_todo = todo
#                         break
#                 else:
#                     print(f"{search_value} not found")
#                     continue

#                 while True:
#                     print("\nFind todo :")
#                     print("---------------------")
#                     print(f"Title : {find_todo["title"]}")
#                     print(f"Time : {find_todo["time"]}")
#                     print(f"Code : {find_todo["code"]}")
#                     print(f"Status : {find_todo["status"]}")
#                     print(f"Description : {find_todo["description"]}")

#                     edit_item = get_input(
#                         "1.Title 2.Time 3.Status 4.Desc 5.Exit", valid_items=("1", "2", "3", "4", "5"))

#                     if edit_item == "1":
#                         # region newtitle
#                         while True:
#                             new_title = get_input(
#                                 "Please enter todo new title", err_msg="New title")

#                             for todo in todo_list:
#                                 if todo["title"] == new_title:
#                                     print(new_title, "exist")
#                                     break
#                             else:
#                                 break
#                         # endregion
#                         find_todo["title"] = new_title

#                     elif edit_item == "2":
#                         find_todo["time"] = get_input(
#                             "New time", valid_items=("1400", "1401", "1402"))

#                     elif edit_item == "3":
#                         find_todo["status"] = get_input(
#                             "New status (active - deactive)", valid_items=("active", "deactive"))

#                     elif edit_item == "4":
#                         find_todo["description"] = get_input(
#                             "New description", required=False)

#                     elif edit_item == "5":
#                         break

#         case "8" | "E":
#             break

#         case _:
#             print("Error!")
