
data = ["meisam", "ilka", 32, True, 3.14]

# index =>  0,len-1  |   -1,-len

# get
# res = data[0]
# res = data[1]
# res = data[2]
# res = data[3]
# res = data[4]

# res = data[-1]
# res = data[-2]
# res = data[-3]
# res = data[-4]
# res = data[-5]


# res = data[5]  # indexerror
# res = data[-6] # indexerror


# data = ["meisam", "ilka", 32, True, 3.14, "mehdi", "moradi", 19]

# for i in range(8): #0,1,2,3,4,5,6,7
#     print(data[i])

# i = 0

# while i <= 7:
#     print(data[i])
#     i += 1


# data = ["meisam", "ilka", 32, True, 3.14, "mehdi", "moradi", 19]

# for i in range(len(data)):
#     print(data[i])

# i = 0
# while i < len(data):
#     print(data[i])
#     i += 1

# i = len(data)-1
# while i >= 0:
#     print(data[i])
#     i -= 1

# for i in range((len(data)-1), -1, -1):
#     print(data[i])


# iterable
# data = ["meisam", "ilka", 32, True, 3.14, "mehdi", "moradi", 19]

# for item in data:
#     print(item)


# data = [3, 5, 6, 12, 76, 19, 5, 4, 6, 3, 2]

# sum_ = 0

# for item in data:
#     sum_ += item

# print(sum_)


# set

# data = ["meisam", "ilka", 32, True, 3.14, "mehdi", "moradi", 19]

# data[0] = "rozhin"
# data[10] = "rozhin"  #indxeError


# print(data)


# data = [2, 3, 4, 5, 6, 7, 65, 4, 3, 2, 21, 5]


# for index in range(len(data)):
#     print(data[index])

# for item in data:
#     print(item)


# data = ["mahdi", "zohre", "parinaz", "hamid"]

# # for item in data:
# #     print(item)

# for index in range (len(data)):
#     print(data[index])


# data2 = [20 , 45 , 53 , 28]


# for index in range(len(data2)):
#     data2[index] = data2[index] * 5

# print(data2)

# sum_ = 0

# data2 = [20, 45, 53, 28]


# for item in data2:
#     sum_ += item


# print(sum_)



sum_ = 0
data2 = [20, 45, 53, 28]


for item in data2:
    if item%2==0:
        sum_ += item


print(sum_)


