data1 = [1, 2, 3, 4, 5, "mhdi", 20, 6, 7, 8]
data2 = ["mhdi", "moradi", 20]
data3 = []

for itemlist1 in data1:
    for itemlist2 in data2:
        if itemlist1 == itemlist2:
            data3.append(itemlist1)

print(data3)