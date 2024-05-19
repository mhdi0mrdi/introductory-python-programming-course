num = int(input('num :'))
sum_ = 0
i = 1

while i <= num:
    if num % i == 0:
        sum_ += i
    
    i += 1

print(sum_)