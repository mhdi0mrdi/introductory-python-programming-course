sum_ = 0

while True:
    num = int(input("num :"))

    if num % 2 == 0:
        sum_ += num

    if input("do you want to continue? (yes/ets): ") != "yes":
        break


print(sum_)