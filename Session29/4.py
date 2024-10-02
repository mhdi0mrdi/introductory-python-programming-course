# even = odd = 0
# i = 1


# while i <= 100:
#     num = int(input("Enter number"))

#     if num %2 == 0:
#         odd += 1
#     elif num %2 == 1:
#         even += 1

#     i += 1

# print("even=" ,even)
# print("odd =" ,odd)


# sum_ = 0
# i = 1

# while i <= 20 :
#     num = int(input("Enter number"))

#     if i % 2 == 0:
#         sum_ += num

#     i += 1


# mul = 1

# i = 1

# while i <= 100:
#     mul *= i

#     i += 1


# min_ = 1

# i = 1

# while i <= 100:
#     num = int(input("Enter number"))
#     if num <= min_:
#         min_ = num

#     i += 1


min_ = max_ = avj = float(input("number : "))
i = 1

while i <= 19:
    num = int(input("Enter number"))
    avj += num

    if num < min_:
        min_ = num
    elif num > max_:
        max_ = num

    i += 1

print("min = ", min_)
print("max = ", max_)
print("avj = ", avj / 20)
