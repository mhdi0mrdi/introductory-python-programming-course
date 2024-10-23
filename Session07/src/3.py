
# data = [0] * 10
# data = [""] * 10
# data = [None] * 10

# data = [None] * 5

# i = 0

# while i < 5:
#     score = int(input('score :'))
#     data[i] = score

#     i += 1

# print(data)

# data = [None] * 5

# for index in range(len(data)):
#     score = int(input('score :'))
#     data[index] = score


# name_list = [""] * 10


# for index in range(len(name_list)):
#     name_list[index] = input("name : ")


# data = []

# for _ in range(11):
#     score = int(input("score :"))
#     data.append(score)

# print(data)


data = [] * 10
sum_ = 0


for index in range(len(data)):
    data[index] = int(input("score :"))

for item in data:
    sum_ += data
    
print(sum_)
