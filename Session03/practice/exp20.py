num1 = int(input('num1 :'))
num2 = int(input('num2 :'))

if num1 > num2:
    num1, num2 = num2, num1

i = num1
mul = 0

while i <= num2:
    mul += i

    i += 1
print(mul)
