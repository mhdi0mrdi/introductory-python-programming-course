# data = ["meisam", "ali", "meisam", "mahdi", "hosein"]

# for item in range (data.count("meisam")):
#     data.remove("meisam")

# print(data)

# while "meisam" in data:
#     data.remove("meisam")


data = [1, 2, 4, 2, 8, 3, 4, 5, 6, 7, 8, 9, 10]

for item in data.copy():
    if item % 2 == 0:
        data.remove(item)

print(data)
