days = int(input("day of the year:"))

if days in range (1,32):
    print("month : 1, day :", days)

elif days in range (32,63):
    print("month : 2, day :", days-31)
