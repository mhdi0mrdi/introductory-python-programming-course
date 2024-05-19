

# mutable تغببر پذیر


# imutable
# list

# data = [4, 5, "ilka"]
# data[0] = "mhdi"

# print(data[2])


# data1 = [4, 5, 6]
# data2 = [4, 5, 6]

# data1[0] = "ilka"


# print(id(data1))
# print(id(data2))


# print(id(data1[0]))
# print(id(data2[0]))


# data1 = [4, 5, 6]
# data2 = data1


# data1[0] = "hi"

# print(data1)
# print(data2)


# print(id(data1))
# print(id(data2))


# print(id(data1[0]))
# print(id(data2[0]))


# data1 = [4, 5, "ilka"]
# data2 = data1.copy()

# print(id(data1))
# print(id(data2))


# data1 = ["meisam", "ilka", 32, [12, 15]]
# data2 = data1.copy()


# data1[0] = "mhdi"
# data1[3][0] = 9


from copy import copy, deepcopy

data1 = ["meisam", "ilka", 32, [12, 15]]

# data2 = data1.copy()
# data2 = copy(data1)

data2 = deepcopy(data1)

del data2[2]
