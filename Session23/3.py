


# def program():
#     for num in range(2, 101):
#         print(num, end=" : ")
        
#         for i in range(1, (num//2)+1):
#             if num%i==0:
#                 print(i, end="  ")
        
#         print(num)

# program()



def divisor(num):
    print(num, end=" : ")
    
    for i in range(1, (num//2)+1):
        if num%i==0:
            print(i, end="  ")
    
    print(num)
    
    

for num in range(2, 101):
    divisor(num)
    