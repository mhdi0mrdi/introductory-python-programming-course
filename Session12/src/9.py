data1 = [1, 2, 3, 4, 5, "mhdi", 20, 6, 7, 8]
data2 = ["mhdi", "moradi", 20]

total_list = data1 + data2
entersection_list = []



for itemlist1 in data1:
    for itemlist2 in data2:
        if itemlist1 == itemlist2:
            entersection_list.append(itemlist1)
        
for item in entersection_list:
    for item2 in total_list:
        if item == item2:
            total_list.remove(item2)

print(total_list)