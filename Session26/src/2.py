# def my_sum(num1, num2):
#     sum_ = num1 + num2
#     return sum_


# result = my_sum(2, 5)
# print(result)

# def my_sub(num1, num2, num3):
#     sub = num1 - num2 - num3
#     return sub


# # res = my_sub(1, 2, 3)
# # print(res)

# data1 = float(input("Number"))
# data2 = float(input("Number"))
# data3 = float(input("Number"))

# res = my_sub(data1, data2, data3)
# print(res)

# def my_mul(num1, num2, num3=1):
#     mul = num1 * num2 * num3
#     return mul

# # res = my_mul(2, 3 ,5)


# res = my_mul(num2=2, num3=1, num1=15)
from os import system
from typing import Literal


# def my_function( num1: int|float, num2:int|float, operation: Literal["add", "sub", "mul", "div"] ):
    
#     if operation == "add":
#         value = num1 + num2
#     elif operation == "sub":
#         value = num1 - num2
#     elif operation == "mul":
#         value = num1 * num2
#     elif operation == "div":
#         value = num1 / num2

#     return value
    

    
# # result = my_function(2,3, "add");

# def my_function(message:str , required :bool = True ) -> str:
#     while True:
#         value = input(f"{message} : ")
#         system('cls')

#         if required and value == "":
#             print("data is required")
#             continue

#         return value





# res = my_function("Please enter title" )
# res2 = my_function("Please enter your name",required = False)
# res3 = my_function("Please enter your family")






# def login(username: str, password:str) -> bool:
#     if username == "123" and password == "123":
#         return True
#     else:
#         return False







def my_function(message:str , err_msg:str = "input", required :bool = True ) -> str:
    while True:
        value = input(f"{message} : ")
        system('cls')

        if required and value == "":
            print(f"{message} is required")
            continue

        return value





res = my_function("Please enter title", err_msg="Title")
res2 = my_function("Please enter your name",required = False)
res3 = my_function("Please enter your family", err_msg="Family")