smallest_num = int(input('num :'))
i = 1

while i <= 4:
    num = int(input('num :'))
    if num < smallest_num:
        smallest_num = num

    i += 1

print("resoult:", smallest_num)
