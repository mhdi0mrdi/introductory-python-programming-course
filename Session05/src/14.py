

# i = 1


# while i<=10:

#     if i==5:
#         break

#     print(i)
#     i += 1





# i = 1


# while i<=10:

#     if i==5:
#         i += 1
#         continue

#     print(i)
#     i += 1


# i = 1


# while i<=10:

#     if i==5 or i==7:
#         i += 1
#         continue

#     print(i)
#     i += 1


# num = int(input("num : "))
# i = 1
# count = 1


# while i<=num//2:
#     if num%i==0:
#         count += 1
#     i += 1


# if count == 2:
#     print("is prime")
# else:
#     print("is not prime")




# num = int(input("num : "))
# i = 2
# flag = True


# while flag and i<=num//2:
#     if num%i==0:
#         flag = False
#     i += 1


# if flag:
#     print("is prime")
# else:
#     print("is not prime")




# num = int(input("num : "))
# i = 2
# flag = True


# while i<=num//2:
#     if num%i==0:
#         flag = False
#         break
#     i += 1


# if flag:
#     print("is prime")
# else:
#     print("is not prime")



num = int(input("num : "))
i = 2

while i<=num//2:

    if num%i==0:
        print("is not prime")
        break

    i += 1
else:
    print("is prime")
