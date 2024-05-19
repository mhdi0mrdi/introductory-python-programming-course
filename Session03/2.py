

month = int(input("month : "))

if month not in range(1, 13):
    print("Error!!!")

else:
    day = int(input("days : "))

    if 1<=month<=6 and 1<=day<=31:
        print("Result : ", (month-1)*31+day)

    elif 7<=month<=12 and 1<=day<=30:
        print("Result : ", (month-1)*30 + day + 6)
    
    else:
        print("Error!!!")


