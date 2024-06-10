

# data = {"name": "meisam", "family": "ilka", "age": 32}


# data["name"] = "reza"
# mutable


from copy import deepcopy, copy


data1 = {"name": "meisam", "family": "ilka",
         "age": 32, "score": {"php": 12, "java": 19}}

# data2 = {"name": "meisam", "family": "ilka", "age": 32}
# data2 = data1

# data2 = data1.copy()
# data2 = copy(data1)

data2 = deepcopy(data1)


# print(id(data1))
# print(id(data2))


# print(data1 is data2)

# data = [2,5,6]
# res = list(reversed(data))



