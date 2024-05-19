num = int(input('num :'))
mul = 1
i = 2

while i <= num:
    if num % i == 0:
        mul *= i
    
    i += 2

print(mul)