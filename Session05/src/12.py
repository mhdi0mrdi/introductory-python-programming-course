

# break
# continue
# while else


# i = 1

# while i<=10:

#     if i==5:
#         break

#     print(i)
#     i += 1


# pass_ = "12345"
# flag = True

# while flag:
#     password = int(input('password :'))

#     if password == pass_:
#         flag = False
#     else:
#         print("error")


# while True:
#     password = int(input('password :'))

#     if password == "12345":
#         break

#     print("error")


# while True:

#     num1 = int(input('num1 :'))
#     num2 = int(input('num2 :'))

#     print(num1, "+", num2, "=", num1+num2)

#     if input("Do you want to continue (yes-etc) :")!="yes":
#         break


sum_ = 0

while True:

    num = int(input('num :'))

    if num==0:
        break

    sum_ += num


print(sum_)