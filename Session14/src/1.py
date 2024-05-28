# # Python code to demonstrate namedtuple()
from collections import namedtuple

# # Declaring namedtuple()
# Contact = namedtuple('Contact', ['name', 'family', 'phone'])

# # # Adding values
# cnt = Contact('Meisam', 'Ilka', '09369230358')
# cnt = Contact(name='Meisam', family='Ilka', phone='09369230358')


# # Access using index
# print("The Contact name using index is : ", end="")
# print(cnt[0])

# # Access using name
# print("The Contact name using keyname is : ", end="")
# print(cnt.name)


# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])
# p = Point(x=1, y=2)
# print(p.x, p.y)


# from collections import namedtuple

# Declaring namedtuple()
# Contact = namedtuple('Contact', ['name', 'family', 'phone'])

# Contact = namedtuple(
#     'Contact', ['name', 'family', 'phone'], defaults=("mrdi", "0"))


# Contact(name="negar")
# print(Contact._field_defaults)


Contact = namedtuple('Contact', ('name', 'family', 'phone'))
# Contact = namedtuple('Contact', 'name family phone')


# Adding values
# cnt = Contact('Meisam', 'Ilka', '09369230358')
# cnt = Contact(name='Meisam', family='Ilka', phone='09369230358')


# # # Access using index
# print(cnt[0])
# print(cnt.name)
# print(getattr(cnt, 'name'))


# # using _asdict() to return an OrderedDict()
# print("The OrderedDict instance using namedtuple is  : ")
# print(cnt._asdict())

# print("All the fields of students are : ")
# print(cnt._fields)


# print(cnt)
# ._replace returns a new namedtuple,
# it does not modify the original
# print("returns a new namedtuple : ")
# new_cnt = cnt._replace(name='Parsa')


# Student.__new__ returns a new instance of Student(name,age,DOB)

cnt1 = Contact(name='Meisam', family='Ilka', phone='09369230358')
# cnt2 = Contact.__new__(Contact, 'Himesh', '19', '26082003')
# cnt3 = Contact._make(["Jane", "25", "1.75"])


print(cnt1.__getnewargs__())
# print(cnt2.__getnewargs__())
