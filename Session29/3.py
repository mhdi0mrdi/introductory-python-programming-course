num1 = int(input("num1 :"))
num2 = int(input("num2 :"))

if num1 > num2:
    num2, num1 = num1, num2

num1 += 1

while num1 < num2:
    print(num1)
    num1 += 1