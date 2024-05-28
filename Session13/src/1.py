# tuple

# data = ()
# data = tuple()

# print(type(data))

# data = ("meisam", "ilka", 32, True, "male", True, 32)

# print(data)
# res = len(data)
# res = "meisam" in data
# res = "meisamm" not in data
# res = data.__contains__("meisam")
# res = data.__contains__("meisamm")


# data1 = (4, 5, 6)
# data2 = (4, 5, 6)

# res = data1 == data2
# res = data1.__eq__(data2)


# data = ("meisam", "ilka", 32, True, "male", True, 32)

# print(data)


# get
# ********************************************************************
# index => 0, len-1 | -1,-len
# res = data[0]
# res = data[1]
# res = data[2]
# res = data  # indexerror
# res = data[-1]
# res = data[-9] # indexerror


# i = 0

# while i < len(data):
#     print(data[i])
#     i += 1

# data = ("meisam", "ilka", 32, True, "male", True, 32)

# i = 0

# while i < len(data):
#     print(data[i])
#     i += 1


# i = -1

# while i >= -len(data):
#     print(data[i])
#     i -= 1


# for i in range(len(data)):
#     print(data[i])


# for i in range(-1, -len(data)-1, -1):
#     print(data[i])

# iterable
# for item in data:
#     print(item)

# for i in range(len(data)):
#     print(i, data[i])


# for index, item in enumerate(data):
#     print(index, item)


# print(*data, sep=" ** ")


# data = ("meisam", "ilka", 32, True, "male", True, 32)

# set
# data[0] = "sara"


data1 = ("meisam", "ilka", 32, True, "male", True, 32)
data2 = ("meisam", "ilka", 32, True, "male", True, 32)
# data2 = data1

# print(id(data1))
# print(id(data2))


res = data1 is data2
print(res)