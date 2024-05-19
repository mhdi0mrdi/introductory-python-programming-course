
max_count = 0
max_number = 0

num = 2


while num<=1000:

    count = 1
    i = 1

    while i <= num//2:
        if num % i == 0:
            count += 1

        i += 1

    if count>max_count:
        max_count = count
        max_number = num

    num += 1


print(max_number)
print(max_count)