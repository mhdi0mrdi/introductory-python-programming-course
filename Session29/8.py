avj = 0
count = 1


while True:

    # region input
    while True:
        num = int(input("num :"))

        if num not in range(0, 101):
            print("error")
            break
    # endregion
    
    count += 1
    avj += num

    if input("do you want to continue? (yes/ets): ") != "yes":
        break
        
        
print(avj / count)


