

# data = ("meisam", "ilka", 32, True, "male", True, 32)


# res = data.count(32)
# res = data.count(320)


# res = data.index(32)
# res = data.index(32, 3)
# res = data.index(32, 3, 10)

# val = 3200

# if val in data:
#     res = data.index(3200)


# val= 3200

# if val in data[2:]:
#     res = data.index(3200, 2)


# val= 3200

# if val in data[2:7]:
#     res = data.index(3200, 2, 7)


data = ("meisam", 32, "ilka", 32, True, "male", True, 32)

val = 32

for index in range(len(data)):
    if data[index] == val:
        print(index)
