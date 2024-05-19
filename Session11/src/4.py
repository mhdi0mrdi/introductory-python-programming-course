
data = [5, 6, 4, 4, 3, 12, "ilka"]

val = 4

for item in data.copy():  # [4, 5, 6, 4, 4, 3, 12, "ilka"]
    if item == val:
        data.remove(item)

print(data)
