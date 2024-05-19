
num1 = float(input("num1 : "))
num2 = float(input("num1 : "))
num3 = float(input("num1 : "))


if num1>=num2 and num1>=num3 and num2>=num3:
    print(num1, num2, num3)

elif num1>=num2 and num1>=num3 and num3>=num2:
    print(num1, num3, num2)

elif num2>=num1 and num2>=num3 and num1>=num3:
    print(num2, num1, num3)

elif num2>=num1 and num2>=num3 and num3>=num1:
    print(num1, num3, num2)

elif num3>=num1 and num3>=num2 and num1>=num2:
    print(num3, num1, num2)

# elif num3>=num1 and num3>=num2 and num2>=num1:
else:
    print(num3, num2, num1)