count = 0
i = 1


while i <= 5:
    num = int(input('num :'))
    
    if num % 2 == 0:
        count += 1

    i += 1

print("result:", count)
