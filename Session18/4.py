data = {"name": "meisam", "family": "ilka", "age": 32}


# res = data["name"]
# res = data.get("name")


# res = data["fullname"]
# res = data.get("fullname")
# res = data.get("fullname", "")


# res = data.pop("name")
# res = data.pop("ncode", 0)

# res = data.popitem()

new_data = {"name":"mhdi", "family":"mrdi", "gender":"male"}

# res = data.update(new_data)
# res = data.update([("gender","male"), ("name","mehdi")])
# res = data.update((("gender","male"), ("name","mehdi")))
res = data.update(gender="male", ncode="04300", age=19)




print(res)
print(data)
