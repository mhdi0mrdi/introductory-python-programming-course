num1 = int(input('num1 :'))
num2 = int(input('num2 :'))


if num2 < num1:
    num2, num1 = num1, num2


sum_ = 0
i = num1 + 1


while i < num2:
    sum_ += i
    i += 1


print("result:", sum_)
