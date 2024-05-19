num1 = int(input('num1 :'))
num2 = int(input('num2 :'))

if num1 > num2:
    num1, num2 = num2, num1

i = num1

while i <= num2:
    print(i)

    i += 1
