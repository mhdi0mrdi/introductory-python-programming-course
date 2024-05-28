from collections import namedtuple


Contact = namedtuple(
    'Contact', ['name', 'family', 'phone'], defaults=("", "", ""))


# cnt = Contact(name='Meisam', family='Ilka', phone='09369230358')

# res = cnt.count("Meisam")
# print(res)

# print(cnt.family)
# print(cnt.index("Ilka"))
# print(cnt.index("Ilka", 1))
# print(cnt.index("Ilka", 1, 3))


# print(len(cnt))
# print("Meisam" in cnt)
# print("Meisam" not in cnt)

# cnt1 = Contact(name='Meisam', family='Ilka', phone='09369230358')
# cnt2 = Contact(name='Meisam', family='Ilka', phone='09369230358')
# cnt2 = cnt1

# print(id(cnt1))
# print(id(cnt2))

# print(cnt1 == cnt2)

# print(cnt1 is cnt2)


cnt1 = Contact(name='Meisam', family='Ilka', phone='09369230358')
# cnt2 = cnt1._replace(name = "mhdi")
# cnt2 = Contact._make(("meisam", "ilka", "0936"))
# print(Contact._field_defaults)
print(cnt1._fields)


# print(dir(cnt1))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__match_args__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_asdict', '_field_defaults', '_fields', '_make', '_replace', 'count', 'family', 'index', 'name', 'phone']
