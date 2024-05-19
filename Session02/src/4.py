
# i = 1

# while i <= 100:
#     print(i)
#     i += 1


# i = 100

# while i >=1:
#     print(i)
#     i -= 1


# num = int(input("num : "))
# i = 1

# while i<=num:
#     print(i)
#     i += 1


# i = int(input("num : "))

# while i >= 1:
#     print(i)
#     i -= 1


# num1 = int(input("num : "))
# num2 = int(input("num : "))

# if num1>num2:
#     num1, num2 = num2, num1

# while num1<=num2:
#     print(num1)
#     num1 += 1


# if num1<num2:
#     min_ = num1
#     max_ = num2
# else:
#     min_ = num2
#     max_ = num1


# while min_<=max_:
#     print(min_)
#     min_ += 1


# if num1<=num2:
#     while num1<=num2:
#         print(num1)
#         num1 += 1
# else:
#     while num2<=num1:
#         print(num2)
#         num2 += 1


num1 = int(input("num : "))
num2 = int(input("num : "))

if num2 < num1:
    num2, num1 = num1, num2

num2 -= 1
num1 += 1

while num2 >= num1:
    print(num2)
    num2 -= 1

