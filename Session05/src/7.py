num = int(input("num : "))
i = 1

print(num, end=" : ")

while i <= num//2:
    if num % i == 0:
        print(i, end="  ")
    i += 1


print(num)