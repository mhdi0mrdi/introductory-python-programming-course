



# num = int(input('num :'))
# i = 2


# while i<=num//2:

#     if num % i == 0:
#         print(num, "is not prime")
#         break

#     i += 1

# else:
#     print(num, "is prime")




# while condition:
#     statement
#     statement

#     if condition:
#         break

# else:
#     statement
#     statement



num = int(input('num :'))


for i in range(2, (num//2+1)):
    if num % i == 0:
        print(num, "is not prime")
        break
else:
    print(num, "is prime")