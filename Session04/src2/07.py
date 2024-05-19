

# num
# ______________________________________

# 76549     9
# 7654      4
# 765       5
# 76        6
# 7         7
# 0

# num = int(input("num : "))

# while num!=0:
#     print(num%10)
#     num = num//10


num = int(input("num : "))
count = 0


while num != 0:
    num = num//10
    count += 1


print(count)
