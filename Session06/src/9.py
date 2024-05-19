

# row = 1

# while row <= 9:
#     column =1

#     while column<=9:
#         print(row, "*", column, "=", row*column, sep="", end="\t")
#         column += 1

#     print()
#     row += 1



for row in range(1, 10):
    for column in range(1, 10):
        print(row, "*", column, "=", row*column, sep="", end="\t")
    print()