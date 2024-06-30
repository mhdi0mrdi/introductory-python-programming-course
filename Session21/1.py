
# data = set()


# data = {2, 3, 6, 5, 4, 1}
# data = {1, 2, 3, 1, 1, 1, True}


# data1 = {"meisam", 1, 2, 3, "ilka"}


# get
# for item in data1:
#     print(item, end="   ")

# print(data)


# set
# data1.add(1)

# data1.add(111)


# print(data1)


# mutable
# iterable
# hashable


# data1 = {"meisam", 1, 2, 3, 1, 1, 1}

# res = len(data1)
# res = data1.__len__()

# res = "meisam" in data1
# res = "meisam" not in data1
# res = data1.__contains__("meisam")


# data1 = {1, 2, 3}
# data2 = {3, 2, 1}

# res = data1==data2
# res = data1.__eq__(data2)
# print(res)



from copy import copy, deepcopy


data1 = {1, 2, 3}
# data2 = {1, 2, 3}
# data2 = data1
data2 = data1.copy()

data2 = copy(data1)
data2 = deepcopy(data1)

res = data1 is data2



