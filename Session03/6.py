
num1 = int(input('num1 :'))
num2 = int(input('num2 :'))


if num1>num2:
    num1, num2 = num2, num1


mul = 1


while num1<=num2:
    mul *= num1
    num1 += 1


print("result : ", mul)
