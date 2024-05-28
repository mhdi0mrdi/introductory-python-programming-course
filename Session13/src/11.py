# import dis


# def a():
#     x = [1, 2, 3, 4, 5]
#     y = x[2]


# def b():
#     x = (1, 2, 3, 4, 5)
#     y = x[2]


# print(dis.dis(a))
# print("------------------------------------")

# print(dis.dis(b))


#   2           0 LOAD_CONST               1 (1)
#               3 LOAD_CONST               2 (2)
#               6 LOAD_CONST               3 (3)
#               9 LOAD_CONST               4 (4)
#              12 LOAD_CONST               5 (5)
#              15 BUILD_LIST               5
#              18 STORE_FAST               0 (x)

#   3          21 LOAD_FAST                0 (x)
#              24 LOAD_CONST               2 (2)
#              27 BINARY_SUBSCR
#              28 STORE_FAST               1 (y)
#              31 LOAD_CONST               0 (None)
#              34 RETURN_VALUE
# >>> dis.dis(b)
#   2           0 LOAD_CONST               6 ((1, 2, 3, 4, 5))
#               3 STORE_FAST               0 (x)

#   3           6 LOAD_FAST                0 (x)
#               9 LOAD_CONST               2 (2)
#              12 BINARY_SUBSCR
#              13 STORE_FAST               1 (y)
#              16 LOAD_CONST               0 (None)
#              19 RETURN_VALUE


# from timeit import timeit

# # 0.14382770000000278
# print(timeit("(1, 2, 'Apify', 'Crawlee')", number=10_000_000))
# print(timeit("[1, 2, 'Apify', 'Crawlee']", number=10_000_000))
