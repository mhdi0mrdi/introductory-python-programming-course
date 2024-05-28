
# constant value
# GENDER = ("male", "female")


# # data = ["meisam", "ilka", 32, "male"]
# data = ("meisam", "ilka", 32, "male")


# first_name = data[0]
# last_name = data[1]
# age = data[2]
# gender = data[3]

# unpack
# data = ["meisam", "ilka", 32, "male"]
# data = ("meisam", "ilka", 32, "male")


# name, family, age, gender = ["meisam", "ilka", 32, "male"]
# name, family, age, gender = data


# data = ["meisam", "ilka", 32, "male"]
# data = ("meisam", "ilka", 32, "male")


# name, *info, gender = ["meisam", "ilka", 32, "male"]
# name, *info, gender = ("meisam", "ilka", 32, "male")

# print(name)
# print(info)
# print(gender)


# name, *_, gender = ("meisam", "ilka", 32, "male")
name, family, *_ = ("meisam", "ilka", 32, "male")
