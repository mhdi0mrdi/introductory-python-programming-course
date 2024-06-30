

data = [2, 5, 2, 3, 6, 5, 2, 9, 8, 5, 2, 0, 0, 1, 0, 2, 1, 2, 1, 2, 1]

for item in data.copy():
    while data.count(item) > 1:
        data.remove(item)

# res = list(dict.fromkeys(data))
res = list(set(data))




# data = {1, 2, 3}

# res = list(data)
# res = tuple(data)
# res = dict.fromkeys(data)


# data = [1, 2, 3, 1, 1]
# data = (1, 2, 3, 1, 1)
# data = {1:1, 2:2, 3:3, 4:4}

# res = set(data)



