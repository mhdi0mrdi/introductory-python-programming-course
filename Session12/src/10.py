name_list = ["ali", "hosein", "ali", "mhdi",
             "ali", "hosein", "meisam", "mhdi"]
res = []


for item in name_list:
    if name_list.count(item) == 3 and (item not in res):
        res.append(item)


for item in res:
    name_list.remove(item)
    name_list.remove(item)
    name_list.remove(item)


print(name_list)

# for item in res:
#     for i in name_list:
#         if item == i:
#             name_list.remove(item)
# print(name_list)
