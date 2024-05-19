

num = int(input("num : "))


if num>0:
    print(num, "is positive")

    if num%2==0:
        print(num, "is even")
    else:
        print(num, "is odd")

elif num<0:
    print(num, "is negative")

# if num==0:
else:
    print("is zero")