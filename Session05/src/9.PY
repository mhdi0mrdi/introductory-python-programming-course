num = int(input('num :'))
count = 1
i = 1

while i <= num//2:
    if num % i == 0:
        count += 1

    i += 1

print(count)