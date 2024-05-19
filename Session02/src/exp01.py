
month = int(input("month num:"))


if month in range(1, 7):
    day = int(input("day num:"))

    if day in range(1, 32):
        print("days gone :"((month-1) * 31) + day)
    else:
        print("Error")

elif month in range(7, 13):
    days = int(input("day num:"))

    if days in range(1, 31):
        print("days gone :"((month-1) * 30) + days + 6)
    else:
        print("Error")

else:
    print("error")
