

# num1 = 12
# num2 = 15.5

# built in container
# list - tuple - dict - set - frozenset - str

data = []
data = list()


data = ["meisam", "ilka", 32, True, 3.14]

res = data.__len__()
res = len(data)
len(res)

res = "meisam" in data
res = "meisamm" in data
res = "meisam" not in data
res = "meisamm" not in data


# res = data.__contains__("meisam")

data1 = ["meisam", "ilka", 32, True, 3.14]
data2 = ["meisam", "ilka", 32, True, 3.14]


res = data1 == data2
res = data1.__eq__(data2)
