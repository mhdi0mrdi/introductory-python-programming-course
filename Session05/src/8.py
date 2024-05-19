# 2 :  1  2
# 3 :  1  3
# 4 :  1  2  4
# ...
# 100 : 



num = 2

while num<=100:

    i = 1
    print(num, end=" : ")

    while i <= num//2:
        if num % i == 0:
            print(i, end="  ")
        i += 1

    print(num)

    num += 1



# num = 2
# i = 1
# print(num, end=" : ")

# while i <= num//2:
#     if num % i == 0:
#         print(i, end="  ")
#     i += 1

# print(num)



# num = 3
# i = 1
# print(num, end=" : ")

# while i <= num//2:
#     if num % i == 0:
#         print(i, end="  ")
#     i += 1

# print(num)



# num = 4
# i = 1
# print(num, end=" : ")

# while i <= num//2:
#     if num % i == 0:
#         print(i, end="  ")
#     i += 1

# print(num)