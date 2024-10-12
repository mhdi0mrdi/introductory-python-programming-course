
# i = 1

# while i <= num:
#     if num % i == 0:
#         count += 1

#     i += 1

# print(count)

# for num in range(2, 101):
#     print (num , end="  :")
#     # region input
#     count = 0

#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1

#     print(count)
#     # endregion


for num in range(2, 101, 2):
    print(num, end="  :")

    # region input
    count = 0

    for i in range(1, num+1):
        if num % i == 0:
            count += 1

    print(count)

    # endregion
